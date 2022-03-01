from rest_framework import generics
from contacts.models import Contact
from .serializers import ContactSerializer

# Create your views here.
class ContactListView(generics.ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    pass

class ContactCreateView(generics.CreateAPIView):
    pass

class ContactUpdateView(generics.UpdateAPIView):
    pass

class ContactDeleteView(generics.DestroyAPIView):
    pass