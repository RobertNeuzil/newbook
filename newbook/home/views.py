
''' The First "Comments"in the context dic is the key the value is the actual list of comments  min 49'''


from django.shortcuts import render
from django.http import HttpResponse
from .models import Comment

def index(request):
	comments = Comment.objects.order_by("-date_added")

	context = {

	"comments" : comments


	}

	return render(request, "home/index.html", context)

def sign(request):
	return render(request, "home/sign.html")

# Create your views here.
