from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse

# Create your views here.
def index(request):
    try:
        #Create a response 
        response = TemplateResponse(request, 'home.html', {})
        #Return the response
        return response
    except Exception as e:
        return HttpResponse("Erreur")