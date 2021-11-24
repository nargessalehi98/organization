from django.test import TestCase
from django.test import Client
from django.urls import reverse


class testmy(TestCase):

    def test_index_page_loads_ok(self):
        print("hello")
