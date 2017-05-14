# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Label(models.Model):
    Labelname = models.CharField(max_length=20)

    def __str__(self):
        return self.Labelname
