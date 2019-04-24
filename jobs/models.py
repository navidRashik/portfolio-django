from django.db import models

# Create your models here.
class Job(models.Model):
    images = models.ImageField( upload_to='images/')
    summery = models.CharField(max_length=150)
