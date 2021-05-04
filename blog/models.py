from django.db import models

# Create your models here.
class Blog(models.Model):
  title = models.CharField(max_length=255)
  pub_date = models.DateTimeField()
  title = models.CharField(max_length=75, null=True)
  body = models.TextField(null=True)
  image = models.ImageField(upload_to='images/', blank=True)
  title1 = models.CharField(max_length=75, null=True, blank=True)
  body1 = models.TextField( null=True, blank=True)
  image1 = models.ImageField(upload_to='images/',  null=True, blank=True)
  title2 = models.CharField(max_length=75, null=True, blank=True)
  body2 = models.TextField(null=True, blank=True)
  image2 = models.ImageField(upload_to='images/', null=True, blank=True)
  title3 = models.CharField(max_length=75, null=True, blank=True)
  body3 = models.TextField(null=True, blank=True)
  image3 = models.ImageField(upload_to='images/', null=True, blank=True)
  title4 = models.CharField(max_length=75, null=True, blank=True)
  body4 = models.TextField(null=True, blank=True)
  image4 = models.ImageField(upload_to='images/', null=True, blank=True)
  

  # Return titles in admin panel
  def __str__(self):
    return self.title
  # Provide option to display shortened body text to keep styles uniform and consistent
  def summary(self):
    return self.body[:100]
  # Provide option to display date/time in a 'pretty' way
  def pub_date_pretty(self):
    return self.pub_date.strftime('%b %e %Y')