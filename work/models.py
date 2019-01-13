from django.db import models

# Create your models here.
class Work(models.Model):
    image = models.ImageField(upload_to='images/%Y/%m/%d')
    title = models.CharField(max_length=200)
    description = models.TextField()
    highlights_1 = models.CharField(max_length=200, blank=True)
    highlights_2 = models.CharField(max_length=200, blank=True)
    highlights_3 = models.CharField(max_length=200, blank=True)
    highlights_4 = models.CharField(max_length=200, blank=True)
    highlights_5 = models.CharField(max_length=200, blank=True)
    highlights_6 = models.CharField(max_length=200, blank=True)
    highlights_7 = models.CharField(max_length=200, blank=True)
    address = models.CharField(max_length=255, default='www.google.com')
    image_1 = models.ImageField(upload_to='images/%Y/%m/%d', blank=True) 
    address_1 = models.CharField(max_length=255, blank=True) 
    image_2 = models.ImageField(upload_to='images/%Y/%m/%d', blank=True) 
    address_2 = models.CharField(max_length=255, blank=True) 
    image_3 = models.ImageField(upload_to='images/%Y/%m/%d', blank=True) 
    address_3 = models.CharField(max_length=255, blank=True) 