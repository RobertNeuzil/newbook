
''' The First "Comments"in the context dic is the key the value is the actual list of comments  min 49'''


from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Comment
from .forms import CommentForm

def index(request):
	comments = Comment.objects.order_by("-date_added")

	context = {

	"comments" : comments


	}

	return render(request, "home/index.html", context)

def sign(request):

	if request.method == "POST":
		form = CommentForm(request.POST)

		if form.is_valid():

			new_comment = Comment(name=request.POST['name'], comment= request.POST['comment'])
			new_comment.save()
			return redirect ('index')

	
	else:



		form = CommentForm()
	

	context = {
	"form" : form
	}
	
	return render(request, "home/sign.html", context)

# Create your views here.
