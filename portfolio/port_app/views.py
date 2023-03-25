from django.shortcuts import render
from django.http import HttpResponse
from dotenv import load_dotenv

# Create your views here.

def home(request):
    return render(request, 'pages/layout.html')

