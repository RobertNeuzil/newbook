from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	HttpResponse("Hello World")

# Create your views here.
