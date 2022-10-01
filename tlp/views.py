from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse
from tlp.models_Classes.Model_Service import Services_Class
from tlp.models_Classes.Model_equipe import Equipe_Class

# Create your views here.
def index(request):
    try:
        
        services = Services_Class.listServices()
        equipes = Equipe_Class.listEquipe()
        dic = {
            'titre':"TL Partners CONGO SARL",
            'model':services,
            'equipes':equipes
        }

        #Create a response 
        response = TemplateResponse(request, 'index.html', dic)
        #Return the response
        return response
    except Exception as e:
        return HttpResponse("Erreur")