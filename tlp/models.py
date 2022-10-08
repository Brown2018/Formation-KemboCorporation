
from django.db import models
from django.utils import timezone
from django.core.files.storage import FileSystemStorage
from django.conf import settings

fs = FileSystemStorage(location=str(settings.MEDIA_ROOT))

class Services(models.Model):
    Libellé = models.CharField(max_length=20)
    Commentaires = models.TextField()
    
    def __str__(self):
        return self.Libellé
    
class Equipe(models.Model):
    Nom_complet = models.CharField(max_length=30)
    Fonction = models.CharField(max_length=50)
    Expertise = models.CharField(max_length=50)
    Profil = models.ImageField(storage=fs)
    Adresse_mail = models.CharField(max_length=50)
    Lien_fcbk = models.CharField(max_length=70)
    Lien_insta = models.CharField(max_length=70)
    Lien_tweet = models.CharField(max_length=70)
    Lien_whatsapp = models.CharField(max_length=70)
    Lien_linkedin = models.CharField(max_length=70)
    
    def __str__(self):
        return self.Nom_complet
    

class Model_Message(models.Model):
    Nom_complet = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    objet = models.CharField(max_length=50)
    message = models.TextField(max_length=450)
    def __str__(self):
        return self.email
    