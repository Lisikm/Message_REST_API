from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from .models import User, Message


class Tests(APITestCase):
    def test_create_account(self):
        url = reverse('register')
        data = {'username': 'testowy','email':'testowy@test.owy', 'password':'testowy'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, 'testowy')

    def test_view_message(self):
        message = Message.objects.create(content='test')
        url = reverse('message-view', kwargs={'pk': message.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Message.objects.get(pk=message.id).display_count, 1)
        self.assertEqual(response.data, {'content': 'test', 'display_count': 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Message.objects.get(pk=message.id).display_count, 2)
        self.assertEqual(response.data, {'content': 'test', 'display_count': 2})

    def test_create_message(self):
        url = reverse('message-create')
        data = {'content':'test'}
        user = User.objects.create_user(username='testowy', email='testowy@test.owy', password='testowy')
        token = Token.objects.create(user=user)
        self.client.login(username='testowy', password='testowy')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Message.objects.count(), 1)
        self.assertEqual(Message.objects.get().content, 'test')

    def test_update_message(self):
        message = Message.objects.create(content='test')
        view_url = reverse('message-view', kwargs={'pk': message.id})
        response = self.client.get(view_url)
        self.assertEqual(response.data, {'content': 'test', 'display_count': 1})
        put_url = reverse('message-update', kwargs={'pk': message.id})
        data = {'content':'test1'}
        user = User.objects.create_user(username='testowy', email='testowy@test.owy', password='testowy')
        token = Token.objects.create(user=user)
        self.client.login(username='testowy', password='testowy')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response = self.client.put(put_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Message.objects.count(), 1)
        self.assertEqual(Message.objects.get().content, 'test1')
        response = self.client.get(view_url)
        self.assertEqual(response.data, {'content': 'test1', 'display_count': 1})

    def test_destroy_message(self):
        message = Message.objects.create(content='test')
        self.assertEqual(Message.objects.count(), 1)
        url = reverse('message-destroy', kwargs={'pk': message.id})
        user = User.objects.create_user(username='testowy', email='testowy@test.owy', password='testowy')
        token = Token.objects.create(user=user)
        self.client.login(username='testowy', password='testowy')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Message.objects.count(), 0)
