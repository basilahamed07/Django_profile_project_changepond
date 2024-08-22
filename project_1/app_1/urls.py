from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path("",views.home_page),
    path("home",views.home_page, name="home"),
    path("all-post",views.all_post, name="all-post"),
    path("add_post",views.formviews.as_view(),name="add_post"),
    path("feedback",views.feedback.as_view(),name="feedback"),
    path('<str:details>',views.details, name= "details-slug"),
    

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
