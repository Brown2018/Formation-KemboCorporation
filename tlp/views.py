from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse
from tlp.models_Classes.Model_Service import Services_Class
from tlp.models_Classes.Model_equipe import Equipe_Class
from tlp.dao.dao_message import dao_message
# Create your views here.
def index(request):
    try:
        
        services = Services_Class.listServices()
        equipes = Equipe_Class.listEquipe()
        listmessages=dao_message.listMessage()
        dic = {
            'titre':"TL Partners CONGO SARL",
            'model':services,
            'equipes':equipes,
            'listmessages':listmessages
        }

        #Create a response 
        response = TemplateResponse(request, 'index.html', dic)
        #Return the response
        return response
    except Exception as e:
        return HttpResponse("Erreur")


def postMessage(request):
    try:
        if request.method == 'POST':
            
            nom_complet =request.POST['nom_complet']
            email = request.POST['email']
            objet =request.POST['objet']
            message_ =request.POST['message']
            
            obj_message=dao_message.creerMessage(nom_complet,email,objet,message_)
            msg=dao_message.saveMessage(obj_message)
            dic = {
                'titre':"Données Transferées",
                'message':msg
            }

            response = TemplateResponse(request, 'index.html')
            #Return the response
            return response
        else:
            response = TemplateResponse(request, 'index.html')
            #Return the response
            return response
        #return HttpResponse("La méthode utilisée n\'est pas POST")
    except Exception as e:
        print("#### ERREUR",e)
        return HttpResponse("Erreur ",e)