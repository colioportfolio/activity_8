
# Create your tests here.

from django.test import TestCase
from django.urls import resolve
from lists.views import home_page


class SmokeTest(TestCase):

    def test_math(self):
        self.assertEqual(8*8, 34)


class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)