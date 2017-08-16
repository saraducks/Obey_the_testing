from django.test import TestCase
from django.urls import resolve
from lists.views import home_page
from django.http import HttpRequest
from django.template.loader import render_to_string

# Create your tests here.

class SmokeTest(TestCase):
   def test_math(self):
       found = resolve("/")
       self.assertEqual(found.func, home_page)
  
   def test_home_page(self):
       #request = HttpRequest()
       #response = home_page(request)
       #html = response.content.decode('utf-8')
       #result = render_to_string('home.html')
       #self.assertEqual(html, result)
       response = self.client.get('/')
       self.assertTemplateUsed(response, 'home.html')

