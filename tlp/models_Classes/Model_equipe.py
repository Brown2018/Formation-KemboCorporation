from tlp.models import *

class Equipe_Class(object):
    @staticmethod
    def listEquipe():
        try:
            return Equipe.objects.all()
        except Exception as e :
            print(e)
            return None