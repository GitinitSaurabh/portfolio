from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=1000)
    image = models.ImageField(blank=True,upload_to='blog/images/')
    date = models.DateField()
