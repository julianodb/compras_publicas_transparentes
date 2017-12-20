from django.db import models
import requests

def getCompraPublica(code):
    return response

class CompraPublica(models.Model):
    name = models.CharField(max_length=200)
    def __init__(self,code=None,request_method=requests):
        if not code:
            super().__init__()
            return
        response = request_method.get('http://api.mercadopublico.cl/servicios/v1/publico/ordenesdecompra.json?codigo={}&ticket=34EA724F-17C8-462E-B23B-4A92B3A2F622'.format(code)).json()
        self.name = response['Listado'][0]['Nombre']

#    pub_date = models.DateTimeField('date published')
#
#    def was_published_recently(self):
#        now = timezone.now()
#        return now - datetime.timedelta(days=1) <= self.pub_date <= now
#
#    def __str__(self):
#        return self.question_text

