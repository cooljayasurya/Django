from django.http import HttpResponse
from rest_framework.parsers import JSONParser


class CustomerHandler:

    def addSignUpCust(self,request):
        if request.method == 'POST':
            body = JSONParser().parse(request)
            print(body)
            return HttpResponse({'POST SUCCESSFULLY.......'})