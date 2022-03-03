from re import M
from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Contact(models.Model):
    '''Main Contact model that will be used to generate database and perform CRUD operations'''
    name = models.CharField(max_length = 50)
    email = models.EmailField(max_length = 254, unique=True) #EmailField offers automatic validation

    phoneNumberRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$") #Regex responsible for general expression of international phone number
    phone = models.CharField(validators = [phoneNumberRegex], max_length = 16, unique = True)

    def __str__(self):
        return self.name