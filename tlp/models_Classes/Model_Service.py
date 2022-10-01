from tlp.models import *

class Services_Class(object):
    @staticmethod
    def listServices():
        try:
            return Services.objects.all()
        except Exception as e :
            print(e)
            return None