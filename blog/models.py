from django.db import models

# Create your models here.
class Blog(models.Model):
  title = models.CharField(max_length=255)
  pub_date = models.DateTimeField()
  body = models.TextField()
  image = models.ImageField(upload_to='images/')
  

  # Return titles in admin panel
  def __str__(self):
    return self.title
  # Provide option to display shortened body text to keep styles uniform and consistent
  def summary(self):
    return self.body[:100]
  # Provide option to display date/time in a 'pretty' way
  def pub_date_pretty(self):
    return self.pub_date.strftime('%b %e %Y')