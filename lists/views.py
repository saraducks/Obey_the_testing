from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home_page(input_param):
   return render(input_param, 'home.html',{'new_item_text':input_param.POST.get('to-do-text',''),})

