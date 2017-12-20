from django.db import models
import requests

codigo_estado = {
    4: "Enviada a Proveedor",
    6: "Aceptada ",
    9: "Cancelada ",
    12: "Recepción Conforme",
    13: "Pendiente de Recepcionar",
    14: "Recepcionada Parcialmente",
    15: "Recepcion Conforme Incompleta",
}

class CompraPublica(models.Model):
    code = models.CharField(max_length=50)
    name = models.CharField(max_length=200)
    state_code = models.PositiveSmallIntegerField()
    state_name = models.CharField(max_length=100)
    tender_code = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    type_code = models.CharField(max_length=10)
    type_name = models.CharField(max_length=10)
    currency = models.CharField(max_length=10)
    supplier_state_code = models.CharField(max_length=10)
    supplier_state = models.CharField(max_length=100)
    has_items = models.CharField(max_length=10)
    classification_mean = models.FloatField()
    classification_n = models.PositiveSmallIntegerField()
    discounts = models.FloatField()
    charges = models.FloatField()
    total_net = models.FloatField()
    iva = models.FloatField()
    taxes = models.FloatField()
    total = models.FloatField()
    financing = models.CharField(max_length=100)
    country = models.CharField(max_length=10)
    delivery_type = models.CharField(max_length=10)
    payment_type = models.CharField(max_length=10)

    def __init__(self,code=None,request_method=requests):
        if not code:
            super().__init__()
            return
        req_url = 'http://api.mercadopublico.cl/servicios/v1/publico/ordenesdecompra.json?codigo={}&ticket=34EA724F-17C8-462E-B23B-4A92B3A2F622'.format(code)
        response = request_method.get(req_url).json()
        self.code = response['Listado'][0]['Codigo']
        self.name = response['Listado'][0]['Nombre']
        self.state_code = response['Listado'][0]['CodigoEstado']
        self.state_name = response['Listado'][0]['Estado']
        self.tender_code = response['Listado'][0]['CodigoLicitacion']
        self.description = response['Listado'][0]['Descripcion']
        self.type_code = response['Listado'][0]['CodigoTipo']
        self.type_name = response['Listado'][0]['Tipo']
        self.currency = response['Listado'][0]['TipoMoneda']
        self.supplier_state_code = response['Listado'][0]['CodigoEstadoProveedor']
        self.supplier_state = response['Listado'][0]['EstadoProveedor']
        self.has_items = response['Listado'][0]['TieneItems']
        self.classification_mean = response['Listado'][0]['PromedioCalificacion']
        self.classification_n = response['Listado'][0]['CantidadEvaluacion']
        self.discounts = response['Listado'][0]['Descuentos']
        self.charges = response['Listado'][0]['Cargos']
        self.total_net = response['Listado'][0]['TotalNeto']
        self.iva = response['Listado'][0]['PorcentajeIva']
        self.taxes = response['Listado'][0]['Impuestos']
        self.total = response['Listado'][0]['Total']
        self.financing = response['Listado'][0]['Financiamiento']
        self.country = response['Listado'][0]['Pais']
        self.delivery_type = response['Listado'][0]['TipoDespacho']
        self.payment_type = response['Listado'][0]['FormaPago']

#    pub_date = models.DateTimeField('date published')
#
#    def was_published_recently(self):
#        now = timezone.now()
#        return now - datetime.timedelta(days=1) <= self.pub_date <= now
#
#    def __str__(self):
#        return self.question_text

