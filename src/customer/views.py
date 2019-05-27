from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from customer.models import Customer
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from .customerhandler import CustomerHandler


# Create your views here.

def welcome_view(request ,*args, **kwargs):
    print(args, kwargs)
    print(request.user)
    print(request)
    return render(request,"home.html",{})


@csrf_exempt
def customer_Detail(request):
        
        print(request)
        if request.method == 'GET':
                cus = []

                for c in Customer.objects.all():
                        serial = serializers.serialize('json',[c])
                        cus.append(serial)
                return HttpResponse(cus)

        return HttpResponse(request)


@csrf_exempt
def signUpCustomer(request):

    if request.method == 'POST':
        obj = CustomerHandler()
        return HttpResponse(obj.addSignUpCust(request))

