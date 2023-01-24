from django.urls import path

from . import views

urlpatterns = [
    path("hello/", views.say_hello),
    path("helloHtml/", views.say_helloHtml),
    path("users/", views.getUsers)


]
