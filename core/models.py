# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db.models import fields
from django.utils import timezone


class ModelBase(models.Model):
    created_at = fields.DateTimeField(editable=False)
    last_updated_at = fields.DateTimeField(editable=False)

    def save(self, force_insert=False, force_update=False, using=None,

             update_fields=None):

        if not self.id:
            self.created_at = timezone.now()

        self.last_updated_at = timezone.now()
        super(ModelBase, self).save(force_insert, force_update, using,
                                    update_fields)

    class Meta:
        abstract = True


class User(ModelBase):
    email = fields.EmailField(unique=True)

    class Meta:
        indexes = [
            models.Index(fields=['email']),
        ]


class UserProfile(ModelBase):
    first_name = fields.CharField(max_length=127)
    last_name = fields.CharField(max_length=127, null=True, blank=True)
    phone = fields.CharField(max_length=20)

    class Meta:
        indexes = [
            models.Index(fields=['first_name', 'last_name', ]),
        ]