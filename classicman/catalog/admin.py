# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Label, Product

# Register your models here.

admin.site.register(Label)
admin.site.register(Product)