from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from customer.models import Customer
import json
from django.core import serializers
from src.serialization import Serializer
from smtpd import DebuggingServer


# Create your views here.

def welcome_view(request ,*args, **kwargs):
    print(args, kwargs)
    print(request.user)
    print(request)
    return HttpResponse('<h1>Welcome Hacker</h1>')


def getCust(request):
        name='Hacker'
        print('customer class')
        return HttpResponse('{ "name":"' + name + '", "age":31, "city":"New York" }')


   
def customer_Detail(request):

        if request.method == 'GET':
                cus = []
                for c in Customer.objects.all():
                        serial = Serializer.makeSerialize(request,'json',c)
                        cus.append(serial)
                return HttpResponse(cus)
        

