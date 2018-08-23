from django.shortcuts import render

# Create your views here.
from django.http import httpResponse

def index(request):
    return httpResponse("hello world you're at the polls index.")