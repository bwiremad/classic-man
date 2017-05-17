# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.text import slugify

# Create your models here.

class Label(models.Model):
    Labelname = models.CharField(max_length=20)

    def __str__(self):
        return self.Labelname

class Product(models.Model):
	Extra_large = 'XL'
	large = 'lg'
	medium = 'md'
	small = 'sm'

	SIZES_CHOICES = (
		('XL', 'Extra_large'),
		('Lg', 'large'),
		('md', 'medium'),
		('sm', 'small'),
	)


	name = models.CharField(max_length=20)
	price = models.IntegerField(default=0)
	old_price = models.IntegerField(default=0)
	slug = models.SlugField(max_length=60, blank=True)
	size = models.CharField(max_length=2, choices=SIZES_CHOICES, default=medium)
	specifications = models.TextField()
	thumbnail = models.FileField()
	image = models.FileField()
	description = models.TextField()
	Label = models.ForeignKey('Label', on_delete=models.CASCADE)



	def save(self, *args, **kwargs):
		if not self.pk:
			self.slug = slugify(self.specifications)
		super(Product, self).save(*args, **kwargs)

	def __str__(self):
		return self.name