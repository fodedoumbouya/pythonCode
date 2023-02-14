from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

# Create your views here.


def say_hello(request):
    return HttpResponse("hello")


def send_json(request):
    return JsonResponse({
        "name": "fode"
    })
