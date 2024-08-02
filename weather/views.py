from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    API_KEY = open('API_key', "r").read
    