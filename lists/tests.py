
# Create your tests here.

from django.test import TestCase

class SmokeTest(TestCase):

    def test_math(self):
        self.assertEqual(8*8, 34)