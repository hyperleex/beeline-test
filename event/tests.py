import datetime

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from event.models import Event, UserEvent


class EventListTests(APITestCase):
    def setUp(self):
        self.admin = User.objects.create_user(
            username='admin', password='12345', is_staff=True
        )
        self.user = User.objects.create_user(username='user1', password='12345')
        self.url = reverse('event-list')
        self.data = {
            'title': 'TestEvent',
            'description': 'Test description',
            'date': datetime.date.today(),
        }

    def test_create_event(self):
        self.client.force_authenticate(user=self.user)

        response = self.client.post(self.url, self.data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Event.objects.count(), 1)
        self.assertEqual(Event.objects.get().title, self.data['title'])
        self.assertEqual(Event.objects.get().description, self.data['description'])
        self.assertEqual(Event.objects.get().date, self.data['date'])

    def test_create_event_forbidden(self):
        response = self.client.post(self.url, self.data)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Event.objects.count(), 0)

    def test_list_event_has_regestration(self):
        event1 = Event.objects.create(**self.data)
        UserEvent.objects.create(user=self.user, event=event1)

        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0].get('has_registration'), True)

    def test_list_event_has_not_regestration(self):
        Event.objects.create(**self.data)
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0].get('has_registration'), False)


class EventDetailTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='user1', password='12345')
        self.data = {
            'title': 'TestEvent',
            'description': 'Test description',
            'date': datetime.date.today(),
        }
        self.event = Event.objects.create(**self.data)
        self.url = reverse('event-detail', kwargs={'pk': self.event.id})

    def test_event_has_users_empty(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('users'), [])

    def test_event_has_users(self):
        UserEvent.objects.create(user=self.user, event=self.event)
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data.get('users'), [{'username': 'user1', 'email': ''}]
        )

    def test_event_registration(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.post(
            reverse('event-registration', kwargs={'pk': self.event.id})
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.event.users.count(), 1)
