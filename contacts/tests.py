from django.test import TestCase
from contacts.models import Contact
import json
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

# Create your tests here.
class Test_Contact_Model(TestCase):
    '''Testing for the Contact model and string representation'''

    def setUp(self):
        Contact.objects.create(name = 'Johnny Test', email = 'johnny@gmail.com', phone = '0734221453')
        
    def test_str(self):
        contact_johnny = Contact.objects.get(name = 'Johnny Test')
        self.assertEqual(str(contact_johnny), 'Johnny Test')

# Create your tests here.
class ContactViewAllTests(APITestCase):
    '''Testing for view all capabilities'''

    def setUp(self):
        #create dummy contacts
        Contact.objects.create(
            name='Casper', email = 'casper@gmail.com', phone = '1111111111')
        Contact.objects.create(
            name='Jasper', email = 'jasper@gmail.com', phone = '2222222222')
        Contact.objects.create(
            name='Masper', email = 'masper@gmail.com', phone = '3333333333')
        Contact.objects.create(
            name='Fasper', email = 'fasper@gmail.com', phone = '4444444444')

    def test_view_all_contacts(self):
        # get API response
        response = self.client.get(reverse('contacts_api:all'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class ContactCreateTests(APITestCase):
    '''Testing for create functionality'''

    def setUp(self):
        self.valid_payload = {
            'name': 'Muffin',
            'email': 'muffin@gmail.com',
            'phone': '1111111111',
        }
        self.invalid_payload = {
            'name': '',
            'email': 'abs',
            'phone': '1111111111',
        }

    def test_create_valid_contact(self):
        #get API response
        response = self.client.post(
            reverse('contacts_api:contact_create'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        #compare API response to expected 201 code
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_contact(self):
        response = self.client.post(
            reverse('contacts_api:contact_create'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class ContactUpdateTest(TestCase):
    ''' Testing module for updating existing contact record '''

    def setUp(self):
        self.muffin = Contact.objects.create(
            name='Muffin', email = 'muffin@gmail.com', phone = '1111111111')
        self.valid_payload = {
            'name': 'Muffy',
            'email': 'muffin@gmail.com', 
            'phone': '1111111111',
        }
        self.invalid_payload = {
            'name': '',
            'email': 'abs',
            'phone': '1111111111',
        }

    def test_valid_update_contact(self):
        response = self.client.put(
            reverse('contacts_api:contact_update', kwargs={'pk': self.muffin.pk}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_update_contact(self):
        response = self.client.put(
            reverse('contacts_api:contact_update', kwargs={'pk': self.muffin.pk}),
            data=json.dumps(self.invalid_payload),
            content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class ContactDeleteTest(TestCase):
    '''Testing delete functionalities'''

    def setUp(self):
        self.muffin = Contact.objects.create(
            name='Muffin', email = 'muffin@gmail.com', phone = '1111111111')

    def test_valid_delete_contact(self):
        response = self.client.delete(
            reverse('contacts_api:contact_delete', kwargs={'pk': self.muffin.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_contact(self):
        response = self.client.delete(
            reverse('contacts_api:contact_delete', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
