from rest_framework import generics
from contacts.models import Contact
from .serializers import ContactSerializer

# Create your views here.
class ContactListView(generics.ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class ContactCreateView(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class ContactUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class ContactDeleteView(generics.RetrieveDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer