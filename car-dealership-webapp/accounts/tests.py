from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


class RegisterViewTests(TestCase):
    def test_get_register_renders_template(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')

    def test_post_valid_register_creates_user_and_redirects_to_login(self):
        response = self.client.post(
            reverse('register'),
            data={
                'username': 'newuser',
                'password1': 'StrongPass123!',
                'password2': 'StrongPass123!',
            },
            follow=False,
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login'))
        self.assertTrue(User.objects.filter(username='newuser').exists())

    def test_post_invalid_register_rerenders_form(self):
        response = self.client.post(
            reverse('register'),
            data={
                'username': 'baduser',
                'password1': 'abc',
                'password2': 'def',
            },
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')
        self.assertFalse(User.objects.filter(username='baduser').exists())


class LoginViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='john', password='StrongPass123!')

    def test_get_login_renders_template(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_post_valid_login_redirects_to_cars_list(self):
        response = self.client.post(
            reverse('login'),
            data={'username': 'john', 'password': 'StrongPass123!'},
            follow=False,
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('cars_list'))

        follow_response = self.client.get(reverse('new_car'))
        self.assertNotEqual(follow_response.status_code, 302)

    def test_post_invalid_login_rerenders_form(self):
        response = self.client.post(
            reverse('login'),
            data={'username': 'john', 'password': 'WrongPass!'},
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')


class LogoutViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='jane', password='StrongPass123!')
        self.client.login(username='jane', password='StrongPass123!')

    def test_logout_redirects_to_cars_list_and_session_cleared(self):
        response = self.client.get(reverse('logout'), follow=False)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('cars_list'))

        follow_response = self.client.get(reverse('new_car'))
        self.assertEqual(follow_response.status_code, 302)
        self.assertIn(reverse('login'), follow_response.url)
