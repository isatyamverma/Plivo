# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from . import models as core_models

admin.site.register(core_models.User)
admin.site.register(core_models.UserProfile)