from rest_framework import viewsets
from contacts.models import Contact
from contacts.serializers import ContactSerializer

# Create your views here.
class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
