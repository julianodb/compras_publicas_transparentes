from django.db import models
import requests

class CompraPublica(models.Model):
    STATE_CODE_CHOICES = ( (4, "Enviada a Proveedor"),
                           (6, "Aceptada"),
                           (9, "Cancelada"),
                           (12, "Recepción Conforme"),
                           (13, "Pendiente de Recepcionar"),
                           (14, "Recepcionada Parcialmente"),
                           (15, "Recepcion Conforme Incompleta"),
                         )
    TYPE_CODE_CHOICES = ( ("1","OC - Automática"),
                          ("2",("D1 - Trato directo que genera Orden de Co"
                                "mpra por proveedor único")),
                          ("3",("C1 - Trato directo que genera Orden de Co"
                                "mpra por emergencia, urgencia e imprevist"
                                "o")),
                          ("4",("F3 - Trato directo que genera Orden de Co"
                                "mpra por confidencialidad")),
                          ("5",("G1 - Trato directo que genera Orden de Co"
                                "mpra por naturaleza de negociación")),
                          ("6","R1 - Orden de compra menor a 3UTM"),
                          ("7","CA - Orden de compra sin resolución."),
                          ("8","SE - Sin emisión automática"),
                          ("9","CM - Convenio Marco"),
                          ("10","FG"),
                          ("11","TL"),
                        )
    CURRENCY_CHOICES = ( ("CLP","Peso Chileno"),
                         ("CLF","Unidad de Fomento"),
                         ("USD","Dólar Americano"),
                         ("UTM","Unidad Tributaria Mensual"),
                         ("EUR","Euro"),
                       )
    DELIVERY_TYPE_CHOICES = ( ("7", "Despachar a Dirección de envío"),
                              ("9", "Despachar según programa adjuntado"),
                              ("12", "Otra Forma de Despacho, Ver Instruc"),
                              ("14", "Retiramos de su bodega"),
                              ("20", ("Despacho por courier o encomienda a"
                                      "érea")),
                              ("21", ("Despacho por courier o encomienda t"
                                      "errestre")),
                              ("22", "A convenir"),
                            )
    PAYMENT_TYPE_CHOICES = ( ("1", ("15 días contra la recepción de la fac"
                                    "tura")),
                             ("2", ("30 días contra la recepción de la fac"
                                    "tura")),
                             ("39", "Otra forma de pago"),
                             ("46", ("50 días contra la recepción de la fa"
                                     "ctura")),
                             ("47", ("60 días contra la recepción de la fa"
                                     "ctura")),
                           )
    code = models.CharField(max_length=50)
    name = models.CharField(max_length=200)
    state_code = models.PositiveSmallIntegerField(choices=STATE_CODE_CHOICES)
    state_name = models.CharField(max_length=100)
    tender_code = models.CharField(max_length=50,null=True)
    description = models.CharField(max_length=500)
    type_code = models.CharField(max_length=2,choices=TYPE_CODE_CHOICES)
    type_name = models.CharField(max_length=10)
    currency = models.CharField(max_length=3,choices=CURRENCY_CHOICES)
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
    delivery_type = models.CharField(max_length=2,
                                     choices=DELIVERY_TYPE_CHOICES)
    payment_type = models.CharField(max_length=10,
                                    choices=PAYMENT_TYPE_CHOICES)

    @classmethod
    def create(cls,code=None,request_method=requests):
        if not code:
            return cls()
        try:
            return cls.objects.get(code=code)
        except cls.DoesNotExist:
            new_object = cls()
            req_url = 'http://api.mercadopublico.cl/servicios/v1/publico/ordenesdecompra.json?codigo={}&ticket=34EA724F-17C8-462E-B23B-4A92B3A2F622'
            req_url = req_url.format(code)
            response = request_method.get(req_url).json()
            for _ in range(5):
                while 'Codigo' in response:
                    response = request_method.get(req_url).json()
            new_object.code = response['Listado'][0]['Codigo']
            new_object.name = response['Listado'][0]['Nombre']
            new_object.state_code = response['Listado'][0]['CodigoEstado']
            new_object.state_name = response['Listado'][0]['Estado']
            new_object.tender_code = response['Listado'][0]['CodigoLicitacion']
            new_object.description = response['Listado'][0]['Descripcion']
            new_object.type_code = response['Listado'][0]['CodigoTipo']
            new_object.type_name = response['Listado'][0]['Tipo']
            new_object.currency = response['Listado'][0]['TipoMoneda']
            new_object.supplier_state_code = response['Listado'][0]['CodigoEstadoProveedor']
            new_object.supplier_state = response['Listado'][0]['EstadoProveedor']
            new_object.has_items = response['Listado'][0]['TieneItems']
            new_object.classification_mean = response['Listado'][0]['PromedioCalificacion']
            new_object.classification_n = response['Listado'][0]['CantidadEvaluacion']
            new_object.discounts = response['Listado'][0]['Descuentos']
            new_object.charges = response['Listado'][0]['Cargos']
            new_object.total_net = response['Listado'][0]['TotalNeto']
            new_object.iva = response['Listado'][0]['PorcentajeIva']
            new_object.taxes = response['Listado'][0]['Impuestos']
            new_object.total = response['Listado'][0]['Total']
            new_object.financing = response['Listado'][0]['Financiamiento']
            new_object.country = response['Listado'][0]['Pais']
            new_object.delivery_type = response['Listado'][0]['TipoDespacho']
            new_object.payment_type = response['Listado'][0]['FormaPago']
            new_object.save()
            return new_object

    @classmethod
    def get_last_five(cls,request_method=requests):
        req_url = 'http://api.mercadopublico.cl/servicios/v1/publico/ordenesdecompra.json?estado=todos&ticket=34EA724F-17C8-462E-B23B-4A92B3A2F622'
        response = request_method.get(req_url).json()
        result = []
        for candidate in response['Listado'][:5]:
            result.append(CompraPublica.create(candidate['Codigo']))

        return result
    
    def __repr__(self):
        result = 'CompraPublica('
        for k,v in vars(self).items():
            if not k.startswith('_'):
                result += '{}={!r},'.format(k,v)
        return result[:-1] + ')'


        #return response['Listado'][:5]

#    pub_date = models.DateTimeField('date published')
#
#    def was_published_recently(new_object):
#        now = timezone.now()
#        return now - datetime.timedelta(days=1) <= new_object.pub_date <= now
#
#    def __str__(new_object):
#        return new_object.question_text

