from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=50)
    body = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='blog/images/')
