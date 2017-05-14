# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Label

# Create your views here.

def catalog(request):
	label = Label.objects.all()
	return render(request, 'catalog/base.html', {'label':label})