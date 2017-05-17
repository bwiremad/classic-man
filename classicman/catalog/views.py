# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Label, Product

# Create your views here.

def catalog(request):
	label = Label.objects.all()
	product = Product.objects.all()
	context = {'label':label, 'product':product}
	return render(request, 'catalog/base.html', context)