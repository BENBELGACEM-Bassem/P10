#! usr/bin/env python3
# -*- Coding: UTF-8 -*-

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

admin.site.register(User, UserAdmin)
