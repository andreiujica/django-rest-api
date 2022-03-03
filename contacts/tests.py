import json
from django.test import TestCase
from contacts.models import Contact
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from contacts.serializers import ContactSerializer

# Create your tests here.


class TestContactModel(APITestCase):
    '''Testing for the Contact model and string representation'''

    def setUp(self):
        casper = {
            'name': 'Casper',
            'email': 'casper@gmail.com',
            'phone': '+40743261772'
        }
        Contact.objects.create(**casper)

    def test_str(self):
        contact_johnny = Contact.objects.get(name='Casper')
        self.assertEqual(str(contact_johnny), 'Casper')

# Create your tests here.


class TestListContacts(APITestCase):
    '''Testing for view all capabilities'''

    def setUpTest(self):
        #create dummy contacts
        casper = {
            'name': 'Casper',
            'email': 'casper@gmail.com',
            'phone': '+40743261772'
        }

        jasper = {
            'name': 'Jasper',
            'email': 'jasper@gmail.com',
            'phone': '+40771562752'
        }
        Contact.objects.create(**casper)
        Contact.objects.create(**jasper)

    def test_view_all_contacts(self):
        # get API response

        url = reverse('contacts:contacts-list')
        response = self.client.get(url, format='json')

        contacts = Contact.objects.all()
        serializer = ContactSerializer(contacts, many=True)

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TestCreateContact(APITestCase):
    '''Testing for create functionality'''

    @classmethod
    def setUpTestData(self):
        self.valid_casper = {
            'name': 'Casper',
            'email': 'casper@gmail.com',
            'phone': '+40743261772'
        }

        self.invalid_casper = {
            'name': '',
            'email': 'jasper@gmail.com',
            'phone': '+40771562752'
        }

    def test_create_valid_contact(self):
        #get API response
        response = self.client.post(
            reverse('contacts:contacts-list'),
            data=json.dumps(self.valid_casper),
            content_type='application/json'
        )
        #compare API response to expected 201 code
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        #check that email is unique and item is added to database
        email_query = Contact.objects.filter(email=self.valid_casper['email'])
        self.assertEqual(email_query.count(), 1)

    def test_create_invalid_contact(self):
        response = self.client.post(
            reverse('contacts:contacts-list'),
            data=json.dumps(self.invalid_casper),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class TestUpdateContact(APITestCase):
    ''' Testing module for updating existing contact record '''

    @classmethod
    def setUpTestData(self):
        self.valid_casper = {
            'name': 'Casper',
            'email': 'casper@gmail.com',
            'phone': '+40743261772'
        }

        self.initial_casper = {
            'name': 'Initial Casper',
            'email': 'casper@gmail.com',
            'phone': '+40743261772'
        }

        self.invalid_casper = {
            'name': '',
            'email': 'jasper@gmail.com',
            'phone': '+40771562752'
        }
        self.casper = Contact.objects.create(**self.initial_casper)

    def test_valid_update_contact(self):
        response = self.client.put(
            reverse('contacts:contacts-detail', kwargs={'pk': self.casper.pk}),
            data=json.dumps(self.valid_casper),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_update_contact(self):
        response = self.client.put(
            reverse('contacts:contacts-detail', kwargs={'pk': self.casper.pk}),
            data=json.dumps(self.invalid_casper),
            content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class TestDeleteContact(APITestCase):
    '''Testing delete functionalities'''

    def setUp(self):
        casper_data = {
            'name': 'Casper',
            'email': 'casper@gmail.com',
            'phone': '+40743261772'
        }
        self.casper = Contact.objects.create(**casper_data)

    def test_valid_delete_contact(self):
        response = self.client.delete(
            reverse('contacts:contacts-detail', kwargs={'pk': self.casper.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_contact(self):
        response = self.client.delete(
            reverse('contacts:contacts-detail', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
