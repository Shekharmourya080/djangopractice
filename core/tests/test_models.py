from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import  get_resolver

class Djangotest(TestCase):

    def test_urls(self):
        print(get_resolver().url_patterns)

    def Test_create_user_with_email_sucessful(self):
        """ Test creating a new user with an email is sucessful"""
        email='test@ranchi.com'
        passwordinp='testpass123'
        user=get_user_model().objects.create_user(
            email=email,
            password=passwordinp
        )
        self.assertEqual(user.email,email)
        self.assertTrue(user.check_password(passwordinp))