import re
from django.conf import settings


class Paginator:

    def __init__(self, queryset, serializer, **kwargs):
        page_size = kwargs.get('page_size', None)
        page_number = kwargs.get('page_number', None)

        self.page_number, self.page_size = self.validate(page_number, page_size)

        self.queryset = queryset
        self.max = self.queryset.count()
        self.serializer = serializer

    def validate(self, page_number, page_size):
        try:
            page_size = int(page_size)
        except:
            page_size = settings.DEFAULT_PAGE_SIZE

        try:
            page_number = int(page_number)
        except:
            page_number = 1

        if page_size <= 0:
            page_size = settings.DEFAULT_PAGE_SIZE

        if page_number < 0:
            page_number = 1

        return page_number, page_size

    def paginate(self, queryset, page_number, page_size):
        bottom = (page_number - 1) * page_size

        top = bottom + page_size

        if top > self.max:
            top = self.max

        if bottom > self.max:
            bottom = self.max

        filtered_objects = queryset[bottom:top]

        return filtered_objects

    def get_page(self, object_list, page_number, page_size):
        response = {}

        response['data'] = object_list
        response['page'] = self.page_number
        response['size'] = len(object_list)

        return response


    @property
    def data(self):

        object_list = self.paginate(self.queryset, self.page_number, self.page_size)
        serializer = self.serializer(object_list, many=True)

        data = serializer.data
        response = self.get_page(data, self.page_number, self.page_size)

        return response


class FieldValidators:

    def __init__(self, value, type):
        
        self.validate_type = {
            'string': self.validate_text,
            'integer': self.validate_int,
            'email': self.validate_email
        }

        self.value = value
        self.found_error = False
        self.error = ""
        self.type = type

    def validate_text(self):
        return str(self.value), self.found_error

    def validate_int(self):

        try:
            self.value = int(self.value)
        except:
            self.found_error = True

        if self.found_error:
            self.error = "Not an integer"


    def validate_email(self):

        match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', self.value)

        if match == None:
            self.found_error = True
            self.error = "Email id is not correct"

    @property
    def validate(self):

        validate_method = self.validate_type[self.type]
        validate_method()

        return self.value, self.found_error, self.error

