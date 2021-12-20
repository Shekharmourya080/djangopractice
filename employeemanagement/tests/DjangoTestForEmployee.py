from django.test import TestCase
from django.urls import  get_resolver

class Djangotest(TestCase):

    def tests_urls(self):
        print(get_resolver().reverse_dict.keys())