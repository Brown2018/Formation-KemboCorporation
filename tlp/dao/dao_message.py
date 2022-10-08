from tlp.models import Model_Message

class dao_message(object):
    nom_complet =""
    email = ""
    objet =""
    message_ =""
    @staticmethod
    def creerMessage(nom_complet,email,objet,message_):
        try:
            message=dao_message()
            message.nom_complet=nom_complet
            message.email=email
            message.objet=objet
            message.message_=message_ 
            return message
        except Exception as e :
            print(e)
            return None
        
    @staticmethod
    def saveMessage(objectMessage):
        try:
            message=Model_Message()
            message.Nom_complet=objectMessage.nom_complet
            message.email=objectMessage.email
            message.objet=objectMessage.objet
            message.message=objectMessage.message_ 
            message.save()
            return "Enregistrement Reussi"
        except Exception as e :
            return "Enregistrement echoué",e

    @staticmethod
    def deleteMessage(id):
        try:
            val=Model_Message.objects.get(pk=id)
            val.delete()
        except Exception as e :
            print(e)
            return None
        
    @staticmethod
    def listMessage():
        try:
            return Model_Message.objects.all()
        except Exception as e :
            print(e)
            return None