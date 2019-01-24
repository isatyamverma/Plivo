# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from . import models as contactapp_models


admin.site.register(contactapp_models.Contact)
admin.site.register(contactapp_models.ContactBook)