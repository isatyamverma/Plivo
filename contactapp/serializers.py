from rest_framework import serializers
from contactapp.models import Contact
from core.resources import FieldValidators


class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = ('id', 'contact_book', 'email', 'first_name', 'last_name', 'phone', 'address')


'''
I am not using it. Just created a post validator to display
'''
class CustomSerializer:

    def validate_field(self, field_name, type):
        value = self.input_data[field_name]

        value, found_error, error = FieldValidators(value, type)

        if found_error:
            self.error_dict[field_name] = error
            self.error = True

        return value

    def __init__(self, data):
        self.error_dict = {}
        self.error = False
        self.input_data = data

        self.validate_field('email', 'email')
        self.validate_field('first_name', 'string')
        self.validate_field('last_name', '')
        self.validate_field('phone', 'integer')
        self.validate_field('address', 'string')
