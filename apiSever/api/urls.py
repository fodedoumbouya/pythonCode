from django .urls import path

from . import views

urlpatterns = [
    path('users/', views.getUsers),
    path('hello/', views.getHello),
    path('inv/', views.getInvitations),
    path('user/', views.getUser),


]
