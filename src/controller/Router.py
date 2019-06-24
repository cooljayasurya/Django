from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import requests

class Router:
    
    def __init__(self, request):
        self.request = request
    
    
    def routerConfig(self):
        print(dir(self))
        if self.method == "POST":
            return HttpResponse({"POST call......."})
        return HttpResponse({"LoginSuccessFully"})
    
