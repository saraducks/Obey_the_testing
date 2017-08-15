from django.test import TestCase

# Create your tests here.

class SmokeTest(TestCase):
   def test_math(self):
       self.assertEqual(2,7-3)

