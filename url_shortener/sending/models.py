from django.db import models
# Create your models here.
class Url(models.Model):
    url = models.URLField(max_length=200,default=None)
    random_string = models.CharField(max_length=12,default=None)
    