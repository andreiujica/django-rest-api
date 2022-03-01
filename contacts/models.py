from re import M
from django.db import models

# Create your models here.
class Contact(models.Model):
    '''Main Contact model that will be used to generate database and perform CRUD operations'''
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254) #EmailField offers automatic validation
    phone = models.CharField(max_length=15) # CharField used for simplicity, better implementation could use RegexField
    objects = models.Manager()

    def __str__(self):
        return self.name