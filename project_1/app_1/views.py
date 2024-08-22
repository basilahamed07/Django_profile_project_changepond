from django.shortcuts import render
from django.views import View
from django.views.generic.edit import CreateView
from .models import Posts, feedback
# Create your views here.

def home_page(request):
    posts = Posts.objects.all().order_by("-time").values()[0:3]
    return render(request,"app_1/landing.html",{"data":posts})

def all_post(request):
    posts = Posts.objects.all()
    return render(request,"app_1/all_post.html",{"data":posts})

def details(request,details):
    posts = Posts.objects.get(slug=details)
    return render(request,"app_1/post_details.html",{"post":posts})

class formviews(CreateView):
    model = Posts
    template_name = "app_1/forms.html"
    success_url = "/add_post"
    exclude = ('slug')
    fields = "__all__"

class feedback(CreateView):
    model = feedback
    template_name = "app_1/feedback.html"
    success_url = "/feedback"
    fields = "__all__"