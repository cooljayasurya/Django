from django.shortcuts import render
from django.http import HttpResponse

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
    

    