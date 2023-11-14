from django.db import models
import random
import string
# Create your models here.
class Url(models.Model):
    url = models.URLField(max_length=200,default=None)
    
    def random_string(self):
        letters = string.ascii_lowercase 
        random_string = ''.join(random.choice(letters) for i in range(8))
        return random_string 
    
    