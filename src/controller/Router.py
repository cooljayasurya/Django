from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from turtle import switchpen

class Router:
    
    csrf_exempt
    def routerConfig(self):
        print(self)
        return HttpResponse({'message': "LoginSuccessFully"})
        
    