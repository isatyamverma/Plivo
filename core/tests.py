
from django.test import TestCase

from core.resources import Paginator
from .models import User
from core.serializers import UserSerializer
from django.conf import settings


class PaginatorTestCase(TestCase):
    def setUp(self):
        USER_COUNT = 10

        for index in range(0, USER_COUNT):
            email = "satyam.verma" + str(index) + '@gmail.com'
            User.objects.create(email=email)
            self.all_users_queryset = User.objects.all()

    def test_paginated_response_is_returned_with_proper_size_and_number(self):
        page_size = 5
        page_number = 1

        paginator = Paginator(self.all_users_queryset, UserSerializer, page_number=page_number, page_size=page_size)

        data_length = len(paginator.data['data'])

        self.assertEqual(data_length, page_size)

    def test_return_default_size_on_negative_page_size(self):
        page_size = -3
        page_number = 1

        paginator = Paginator(self.all_users_queryset, UserSerializer, page_number=page_number, page_size=page_size)

        paginated_length = len(paginator.data['data'])

        self.assertEqual(paginated_length, settings.DEFAULT_PAGE_SIZE)

    def test_return_first_page_on_negative_page_number(self):
        page_size = 3
        page_number = -1

        paginator = Paginator(self.all_users_queryset, UserSerializer, page_number=page_number, page_size=page_size)

        page_number = paginator.data['page']

        self.assertEqual(page_number, 1)
