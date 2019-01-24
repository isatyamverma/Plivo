# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db.models import fields
from core.models import ModelBase


class ContactBook(ModelBase):
    name = fields.CharField(max_length=127)
    description = models.TextField(blank=True, null=True)

    class Meta:
        indexes = [
            models.Index(fields=['name']),
        ]


class Contact(ModelBase):
    contact_book = models.ForeignKey(ContactBook)
    email = fields.EmailField(unique=True, null=False, blank=False)
    first_name = fields.CharField(max_length=127)
    last_name = fields.CharField(max_length=127, null=True, blank=True)
    phone = fields.CharField(max_length=20, null=True, blank=True)
    address = models.TextField(blank=True, null=True)

    class Meta:
        indexes = [
            models.Index(fields=['first_name', 'last_name', ]),
            models.Index(fields=['email']),
        ]