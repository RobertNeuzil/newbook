from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return render(request, "home/index.html")

def sign(request):
	return render(request, "home/sign.html")

# Create your views here.
