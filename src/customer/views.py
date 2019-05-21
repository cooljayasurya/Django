from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from customer.models import Customer
import json
from django.core import serializers
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
                customer = Customer.objects.all()
                print(customer)
                for c in customer:
                        serial = serializers.serialize('json',[c])
                        cus.append(serial)
                # serialObj = serializers.serialize('json',[cus])
                print(cus)
                return HttpResponse(cus)
        

