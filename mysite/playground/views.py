from django.shortcuts import render

from django.http import HttpResponse
from . import models
from django.http import JsonResponse

# Create your views here.


def say_hello(request):
    return HttpResponse("hello you")


def say_helloHtml(request):
    return render(request, "hello.html")


def getUsers(request):
    users = models.Users.objects.all()
# // User.objects.all()
    data = {'users': list(users.values())}
    return JsonResponse(data)
