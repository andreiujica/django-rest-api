from rest_framework import serializers
from contacts.models import Contact

class ContactSerializer(serializers.ModelSerializer):
    '''Helps convert model instances to Python datatypes 
       that can be easily rendered into JSON'''
    class Meta:
        '''Automatically generates fields based on the model'''
        model = Contact
        fields = ('id', 'name', 'email', 'phone')
