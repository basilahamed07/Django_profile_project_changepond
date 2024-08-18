from django.urls import path
from . import views
urlpatterns = [
    path("",views.home_page),
    path("home",views.home_page),
    path("all-post",views.all_post, name="all-post"),
    path('<str:details>',views.details, name= "details-slug")
]
