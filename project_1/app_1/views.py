from django.shortcuts import render
from .models import *
# Create your views here.

def home_page(request):
    introduction_data = Introduction.objects.all()[0]
    print(introduction_data.first_name)
    posts = Posts.objects.all().order_by("time")[0:3]
    counts_landing = posts.count()
    count_1 = 1
    count_2 = 2
    count_3 = 3
    print(posts)

    return render(request,"app_1/landing.html",{"introduction_data":introduction_data,
                                                "three_data":posts,
                                                "landing_count":counts_landing,
                                                "count1":count_1,
                                                "count2":count_2,
                                                "count3":count_3,
                                                
                                                })

def all_post(request):
    posts = Posts.objects.all()
    return render(request,"app_1/all_post.html",{"post":posts})

def details(request,details):
    posts = Posts.objects.get(slug=details)
    return render(request,"app_1/post_details.html",{"post":posts})