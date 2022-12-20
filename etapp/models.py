from django.db import models
import string
import random

def generete_code():
    length = 6
    
    while True:
        code = ''.join(random.choices(string.ascii_uppercase, k=length))
        if item.objects.filter(code=code).count() == 0:
            break
    return code
# Create your models here.
class item(models.Model):
    code = models.CharField(max_length=6, default="", null=True, blank=True)
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    city = models.CharField(max_length=300, null=True, blank=True)