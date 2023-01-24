from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse


from . import models

# Create your views here.


def getUsers(request):
    users = models.Users.objects.all()
#     resp = {
#         "users": list(users.values)
#     }
    resp = {"users": list(users.values())}
    return JsonResponse(resp)


def getUser(request):
    id: str = request.GET.get('id')
    user = models.Users.objects.get(userid=id)
#     print(user.)
    resp = {
        'userid': user.userid,
        'number': user.number,
        'name': user.name,
        'dialCode': user.dialcode,
        'superUser': user.superuser,
        'deviceId': user.deviceid,
        'url': user.url,
        'tag': user.tag,
        'create': user.created,



    }
    return JsonResponse(resp)


def getInvitations(request):
    contact = models.Invitations.objects.all()
    res = {'invi': list(contact.values())}
    return JsonResponse(res)


def getHello(request):
    return HttpResponse("hello")
