from django.test import TestCase
from contacts.models import Contact

# Create your tests here.
class Test_Contact_Model(TestCase):
    '''Testing for the Contact model and string representation'''

    def setUp(self):
        Contact.objects.create(name = 'Johnny Test', email = 'johnny@gmail.com', phone = '0734221453')
        
    def test_str(self):
        contact_johnny = Contact.objects.get(name = 'Johnny Test')
        self.assertEqual(str(contact_johnny), 'Johnny Test')
