# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.test.client import Client
from django.conf import settings
from contactapp.models import Contact, ContactBook


class ContactModelTest(TestCase):
    def setUp(self):
        ContactBook.objects.create(name="ContactBookTest")
        self.contact_book = ContactBook.objects.all()[0]


    def test_contact_model_for_nullable_fields(self):
        contact_lentgh = Contact.objects.count()

        Contact.objects.create(contact_book=self.contact_book, email="satyam.verma22@gmail.com", first_name="satyam")

        new_contact_length = Contact.objects.count()

        self.assertEqual(new_contact_length, contact_lentgh+1)

    def test_contact_model_for_email_field_with_correct_input(self):
        contact_lentgh = Contact.objects.count()

        Contact.objects.create(contact_book=self.contact_book, email="satyam.verma22@gmail.com", first_name="satyam")

        new_contact_length = Contact.objects.count()

        self.assertEqual(new_contact_length, contact_lentgh+1)

    def test_contact_model_for_email_field_with_wrong_input(self):
        contact_lentgh = Contact.objects.count()

        Contact.objects.create(contact_book=self.contact_book, email="satyam.verma22gmail.com", first_name="satyam")

        new_contact_length = Contact.objects.count()

        self.assertEqual(new_contact_length, contact_lentgh)

class ContactApiTestCase(TestCase):
    def setUp(self):
        CONTACT_COUNT = 10
        FIRST_NAME = "satyam"

        ContactBook.objects.create(name="ContactBookTest")

        self.contact_book = ContactBook.objects.all()[0]

        for index in range(0, CONTACT_COUNT):
            email = 'satyam.verma' + str(index) + "@gmail.com"
            Contact.objects.create(contact_book = self.contact_book, email=email, first_name=FIRST_NAME)

        Contact.objects.create(contact_book=self.contact_book, email="somethingelse@gmail.com", first_name="somethingelse")

    def test_get_default_size_of_contacts_with_no_params_passed(self):
        client = Client()
        response_data = client.get('/api/v1/contacts/')
        contact_length = len(response_data['data'])

        self.assertEqual(contact_length, settings.DEFAULT_PAGE_SIZE)


    def test_json_data_format(self):
        pass

    def test_api_filter_on_name(self):
        pass

    def test_api_filter_on_email(self):
        pass