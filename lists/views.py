from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home_page(input_param):
   return HttpResponse('<html><title>TO-DO lists</title></html>')

