from django.db import models

# Create your models here.
class Work(models.Model):
    image = models.ImageField(upload_to='images/')
    highlights = models.CharField(max_length=200)
    description = models.TextField() 