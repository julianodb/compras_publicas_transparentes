"""Unittest module for mercadopublico_api"""
from django.test import TestCase
from django.utils import timezone

from .models import CompraPublica, APIItem, APIList

from contextlib import contextmanager

#TODO: handle when response is: {'Codigo': 10500,
 #'Mensaje': 'Lo sentimos. Hemos detectado que existen peticiones simultáneas.'}

class FakeRequest():
    """imitates requests module functionality for mocking

    Implements the get() method, which returns a FakeResponse object, and
    has a json() method.
    """
    alt_response=False
    called_url = ''
    @classmethod
    def get(cls, url):
        cls.called_url = url
        return FakeResponse(cls.alt_response)

    @classmethod
    @contextmanager
    def change_response(cls):
        cls.alt_response = True
        try:
            yield
        finally:
            cls.alt_response = False

class FakeResponse():
    """imitates requests.get() response for mocking

    Provides a hard-coded example extracted from mercadopublico api
    """
    def __init__(self, change_response=False):
        if change_response:
            self.codigo_estado = 5
        else:
            self.codigo_estado = 6
        
    def json(self):
        return {
            "Cantidad":1,
            "FechaCreacion":"2017-12-20T13:22:22.64",
            "Version":"v1",
            "Listado":[{
                "Codigo":"2097-241-SE14",
                "Nombre":"Insumos dentales especialidades",
                "CodigoEstado":self.codigo_estado,
                "Estado":"Aceptada",
                "CodigoLicitacion":"2097-165-L113",
                "Descripcion": (
                    "Insumos dentales especialidades DESDE 2097-165-L113\r"
                    "\nDENTAL ESPECIALIDADES"),
                "CodigoTipo":"8",
                "Tipo":"SE",
                "TipoMoneda":"CLP",
                "CodigoEstadoProveedor":4,
                "EstadoProveedor":"Aceptada",
                "Fechas":{"FechaCreacion":"2014-01-30T09:00:01.96",
                          "FechaEnvio":"2014-01-30T09:36:28",
                          "FechaAceptacion":"2014-02-02T23:58:56.63",
                          "FechaCancelacion":None,
                          "FechaUltimaModificacion":"2014-01-30T09:11:00"},
                "TieneItems":"1",
                "PromedioCalificacion":3.9333333333333331,
                "CantidadEvaluacion":6,
                "Descuentos":0.0,
                "Cargos":0.0,
                "TotalNeto":35000.0,
                "PorcentajeIva":19.0,
                "Impuestos":6650.0,
                "Total":41650.0,
                "Financiamiento":"",
                "Pais":"CL",
                "TipoDespacho":"7",
                "FormaPago":"2",
                "Comprador":{
                    "CodigoOrganismo":"7398",
                    "NombreOrganismo":"Hospital Arauco",
                    "RutUnidad":"61.602.209-1",
                    "CodigoUnidad":"3092",
                    "NombreUnidad":"Hospital Arauco",
                    "Actividad":"",
                    "DireccionUnidad":"Caupolican S/N",
                    "ComunaUnidad":"Arauco",
                    "RegionUnidad":"Región del Biobío ",
                    "Pais":"CL",
                    "NombreContacto":"Yohana Lidia Maldonado Medina",
                    "CargoContacto":"Administrativo Abastecimiento",
                    "FonoContacto":"56-41-2725940",
                    "MailContacto":"maldonadoyohana1@gmail.com"},
                "Proveedor":{
                    "Codigo":"1316979",
                    "Nombre":"COMERCIALIZADORA ILHABELLA EIRL",
                    "Actividad":("VENTA AL POR MAYOR DE OTROS PRODUCTOS N"
                                 ".C.P.| VENT"),
                    "CodigoSucursal":"717107",
                    "NombreSucursal":"COMERCIALIZADORA ILHABELLA EIRL",
                    "RutSucursal":"76.242.192-5",
                    "Direccion":"AV. PAUL HARRIS 1464",
                    "Comuna":"Las Condes",
                    "Region":"Región Metropolitana de Santiago",
                    "Pais":"CL",
                    "NombreContacto":"MARLENE BEATRIZ FLORES PATIÑO",
                    "CargoContacto":"SANTIAGO",
                    "FonoContacto":"56-2-2122966",
                    "MailContacto":"marlenebeatrizflores@gmail.com"},
                "Items":{
                    "Cantidad":1,
                    "Listado":[{
                        "Correlativo":1,
                        "CodigoCategoria":30201900,
                        "Categoria":(
                            "Artículos para estructuras,obras y construcci"
                            "ones / Estructuras prefabricadas / Construcci"
                            "ones médicas prefabricadas"),
                        "CodigoProducto":30201903,
                        "Producto":"Unidades dentales",
                        "EspecificacionComprador":"Ultracal",
                        "EspecificacionProveedor":(
                            " Ultracal.ULTRADENT. PRODUCTO AMERICANO. JERI"
                            "NGA 3 GRS. KIT X 4 UNIDADES.  FECHA DE VENCIM"
                            "IENTO 2018. SE ADJUNTA CATALOGO DE PRODUCTO. "
                            "INCLUY FLETE. DESPACHO 24 HRS. PUESTO EN BODE"
                            "GAS DE HOSPITAL DE ARAUCO."),
                        "Cantidad":1.0,
                        "Unidad":None,
                        "Moneda":"CLP",
                        "PrecioNeto":35000.0,
                        "TotalCargos":0.0,
                        "TotalDescuentos":0.0,
                        "TotalImpuestos":0.0,
                        "Total":35000.0}]}}]}

class FakeRequestList():
    """imitates requests module functionality for lists petitions
    
    Implements the get() method, which returns a FakeResponseList object, 
    and has a json() method.
    """
    alt_response=False
    called_url = ''
    @classmethod
    def get(cls, url):
        cls.called_url = url
        return FakeResponseList(cls.alt_response)

    @classmethod
    @contextmanager
    def change_response(cls):
        cls.alt_response = True
        try:
            yield
        finally:
            cls.alt_response = False

class FakeResponseList():
    """imitates requests.get() response for lists petitions

    Provides with a hard-coded example extracted from mercadopublico api
    when the request is estado=todos
    """
    def __init__(self, change_response=False):
        if change_response:
            self.codigo_estado = 5
        else:
            self.codigo_estado = 4
    def json(self):
        return {'Cantidad': 6,
                'Version': 'v1',
                'FechaCreacion': '2017-12-21T00:37:06.397',
                'Listado': [{'CodigoEstado': self.codigo_estado,
                             'Codigo': '1816-1026-CM17',
                             'Nombre': 'CARNES'},
                            {'CodigoEstado': 4,
                             'Codigo': '1816-1028-CM17',
                             'Nombre': 'CARNES'},
                            {'CodigoEstado': 9,
                             'Codigo': '3265-837-SE17',
                             'Nombre': ('Adquisición de Cajas - Dirección '
                                        'de Transito')},
                            {'CodigoEstado': 5,
                             'Codigo': '4686-1709-SE17',
                             'Nombre': 'DESRATIZACION Y DESINFECCION'},
                            {'CodigoEstado': 4,
                             'Codigo': '5857-43-SE17',
                             'Nombre': ('Servicio de impresión recetarios '
                                        'Adultos mayores')},
                            {'CodigoEstado': 6,
                             'Codigo': '617807-7419-SE17',
                             'Nombre': ('HOSLA COMPRA DE SERVICIOS PROFESI'
                                        'ONALES')}]}


class APIListModelTests(TestCase):
    """APIList Model unit tests"""
    def test_create_no_arguments(self):
        """Trying to create APIList with no arguments raises error"""
        with self.assertRaises(TypeError):
            APIList.create()

    def test_create_missing_is_licitacion(self):
        """Calling APIList.create without is_licitacion raises error"""
        with self.assertRaises(TypeError):
            APIList.create(date=timezone.now().date())

    def test_create_missing_date(self):
        """Calling APIList.create without date raises error"""
        with self.assertRaises(TypeError):
            APIList.create(is_licitacion=True)

    def test_create_licitacion(self):
        """APIList.create happy path for licitacion""" 
        date = timezone.now().date()
        apiresp, n = APIList.create(is_licitacion=True,
                                    date=date,
                                    request_class_or_module=FakeRequestList)
        self.assertTrue(
            FakeRequestList.called_url.startswith( 
                ("http://api.mercadopublico.cl/servicios/v1/publico/licita"
                 "ciones.json?fecha={:%d%m%Y}".format(date))))
        self.assertEquals(apiresp.response, FakeResponseList().json())
        self.assertEquals(apiresp.date, date)
        self.assertIs(apiresp.is_licitacion, True)

    def test_create_licitacion_twice(self):
        """APIList.create returns old object if response is the same""" 
        date = timezone.now().date()
        apiresp, new = APIList.create(is_licitacion=True,
                                      date=date,
                                      request_class_or_module=FakeRequestList)
        self.assertIs(new, True)
        apiresp2, new = APIList.create(is_licitacion=True,
                                       date=date,
                                       request_class_or_module=FakeRequestList)
        self.assertIs(new, False)
        self.assertEquals(apiresp, apiresp2)
        self.assertEquals(APIList.objects.count(), 1)

    def test_create_licitacion_different(self):
        """APIList.create returns new object if response is different""" 
        date = timezone.now().date()
        apiresp, new = APIList.create(is_licitacion=True,
                                      date=date,
                                      request_class_or_module=FakeRequestList)
        self.assertIs(new, True)
        with FakeRequestList.change_response():
            apiresp2, new = APIList.create(
                request_class_or_module=FakeRequestList,
                is_licitacion=True,
                date=date)
            self.assertIs(new, True)
            self.assertEquals(APIList.objects.count(), 2)

    def test_create_orden_compra(self):
        """APIList.create happy path for orden_compra""" 
        date = timezone.now().date()
        apiresp, new = APIList.create(is_licitacion=False,
                                      date=date,
                                      request_class_or_module=FakeRequestList)
        self.assertTrue(
            FakeRequestList.called_url.startswith( 
                ("http://api.mercadopublico.cl/servicios/v1/publico/ordene"
                 "sdecompra.json?fecha={:%d%m%Y}".format(date))))
        self.assertEquals(apiresp.date, date)
        self.assertEquals(apiresp.response, FakeResponseList().json())
        self.assertIs(apiresp.is_licitacion, False)

    def test_create_orden_compra_equal(self):
        """APIList.create returns old object if response is the same""" 
        date = timezone.now().date()
        apiresp, new = APIList.create(is_licitacion=False,
                                      date=date,
                                      request_class_or_module=FakeRequestList)
        self.assertIs(new, True)
        apiresp2, new = APIList.create(is_licitacion=False,
                                       date=date,
                                       request_class_or_module=FakeRequestList)
        self.assertIs(new, False)
        self.assertEquals(apiresp, apiresp2)
        self.assertEquals(APIList.objects.count(), 1)

    def test_create_orden_compra_different(self):
        """APIList.create returns new object if response is different""" 
        date = timezone.now()
        apiresp, new = APIList.create(is_licitacion=False,
                                      date=date,
                                      request_class_or_module=FakeRequestList)
        self.assertIs(new, True)
        with FakeRequestList.change_response():
            apiresp2, new = APIList.create(
                request_class_or_module=FakeRequestList,
                is_licitacion=False,
                date=date)
            self.assertIs(new, True)
            self.assertEquals(APIList.objects.count(), 2)

class APIItemModelTests(TestCase):
    """APIItem Model unit tests"""
    def test_create_no_arguments(self):
        """Trying to create APIItem with no arguments raises error"""
        with self.assertRaises(TypeError):
            APIItem.create()

    def test_create_missing_is_licitacion(self):
        """Calling APIItem.create without is_licitacion raises error"""
        with self.assertRaises(TypeError):
            APIItem.create(code='CODE')

    def test_create_missing_code(self):
        """Calling APIItem.create without code raises error"""
        with self.assertRaises(TypeError):
            APIItem.create(is_licitacion=True)

    def test_create_licitacion(self):
        """APIItem.create happy path for licitacion""" 
        code = 'CODE'
        apiresp, n = APIItem.create(is_licitacion=True,
                                    code=code,
                                    request_class_or_module=FakeRequest)
        self.assertTrue(
            FakeRequest.called_url.startswith( 
                ("http://api.mercadopublico.cl/servicios/v1/publico/licita"
                 "ciones.json?codigo=CODE")))
        self.assertEquals(apiresp.response, FakeResponse().json())
        self.assertEquals(apiresp.code, code)
        self.assertIs(apiresp.is_licitacion, True)

    def test_create_licitacion_twice(self):
        """APIItem.create returns old object if response is the same""" 
        code = 'CODE'
        apiresp, new = APIItem.create(is_licitacion=True,
                                      code=code,
                                      request_class_or_module=FakeRequest)
        self.assertIs(new, True)
        apiresp2, new = APIItem.create(is_licitacion=True,
                                       code=code,
                                       request_class_or_module=FakeRequest)
        self.assertIs(new, False)
        self.assertEquals(apiresp, apiresp2)
        self.assertEquals(APIItem.objects.count(), 1)

    def test_create_licitacion_different(self):
        """APIItem.create returns new object if response is different""" 
        code = 'CODE'
        apiresp, new = APIItem.create(is_licitacion=True,
                                      code=code,
                                      request_class_or_module=FakeRequest)
        self.assertIs(new, True)
        with FakeRequest.change_response():
            apiresp2, new = APIItem.create(
                request_class_or_module=FakeRequest,
                is_licitacion=True,
                code=code)
            self.assertIs(new, True)
            self.assertEquals(APIItem.objects.count(), 2)

    def test_create_orden_compra(self):
        """APIItem.create happy path for orden_compra""" 
        code = 'CODE'
        apiresp, new = APIItem.create(is_licitacion=False,
                                      code=code,
                                      request_class_or_module=FakeRequest)
        self.assertTrue(
            FakeRequest.called_url.startswith( 
                ("http://api.mercadopublico.cl/servicios/v1/publico/ordene"
                 "sdecompra.json?codigo=CODE")))
        self.assertEquals(apiresp.code, code)
        self.assertEquals(apiresp.response, FakeResponse().json())
        self.assertIs(apiresp.is_licitacion, False)

    def test_create_orden_compra_equal(self):
        """APIItem.create returns old object if response is the same""" 
        code = 'CODE'
        apiresp, new = APIItem.create(is_licitacion=False,
                                      code=code,
                                      request_class_or_module=FakeRequest)
        self.assertIs(new, True)
        apiresp2, new = APIItem.create(is_licitacion=False,
                                       code=code,
                                       request_class_or_module=FakeRequest)
        self.assertIs(new, False)
        self.assertEquals(apiresp, apiresp2)
        self.assertEquals(APIItem.objects.count(), 1)

    def test_create_orden_compra_different(self):
        """APIItem.create returns new object if response is different""" 
        code = 'CODE'
        apiresp, new = APIItem.create(is_licitacion=False,
                                      code=code,
                                      request_class_or_module=FakeRequest)
        self.assertIs(new, True)
        with FakeRequest.change_response():
            apiresp2, new = APIItem.create(
                request_class_or_module=FakeRequest,
                is_licitacion=False,
                code=code)
            self.assertIs(new, True)
            self.assertEquals(APIItem.objects.count(), 2)


class CompraPublicaModelTests(TestCase):

    def setUp(self):
        self.cp = CompraPublica.create('fakecode', FakeRequest)

    def test_exists(self):
        """Model CompraPublica exists, is installed and migrated."""
        pass

    def test_empty_comprapublica(self):
        """CompraPublica object created with no arguments is empty"""
        self.assertIs(CompraPublica().name, "")

    def test_atribute_code(self):
        """Test atribute code for CompraPublica api"""
        self.assertEqual(self.cp.code, "2097-241-SE14")

    def test_atribute_name(self):
        """Test atribute name for CompraPublica api"""
        self.assertEqual(self.cp.name, "Insumos dentales especialidades")

    def test_atribute_state_code(self):
        """Test atribute state_code for CompraPublica api"""
        self.assertEqual(self.cp.state_code, 6)

    def test_atribute_state_name(self):
        """Test atribute state_name for CompraPublica api"""
        self.assertEqual(self.cp.state_name, "Aceptada")

    def test_atribute_tender_code(self):
        """Test atribute tender_code for CompraPublica api"""
        self.assertEqual(self.cp.tender_code, "2097-165-L113")

    def test_atribute_description(self):
        """Test atribute description for CompraPublica api"""
        self.assertEqual(self.cp.description,
                         ("Insumos dentales especialidades DESDE 2097-165-"
                          "L113\r\nDENTAL ESPECIALIDADES"))

    def test_atribute_type_code(self):
        """Test atribute type_code for CompraPublica api"""
        self.assertEqual(self.cp.type_code, "8")

    def test_atribute_type_name(self):
        """Test atribute type_name for CompraPublica api"""
        self.assertEqual(self.cp.type_name, "SE")

    def test_atribute_currency(self):
        """Test atribute currency for CompraPublica api"""
        self.assertEqual(self.cp.currency, "CLP")

    def test_atribute_supplier_state_code(self):
        """Test atribute supplier_state_code for CompraPublica api"""
        self.assertEqual(self.cp.supplier_state_code, 4)

    def test_atribute_supplier_state(self):
        """Test atribute supplier_state for CompraPublica api"""
        self.assertEqual(self.cp.supplier_state, "Aceptada")

    def test_atribute_has_items(self):
        """Test atribute has_items for CompraPublica api"""
        self.assertEqual(self.cp.has_items, "1")

    def test_atribute_classification_mean(self):
        """Test atribute classification_mean for CompraPublica api"""
        self.assertEqual(self.cp.classification_mean, 3.9333333333333331)

    def test_atribute_classification(self):
        """Test atribute classification for CompraPublica api"""
        self.assertEqual(self.cp.classification_n, 6)

    def test_atribute_discounts(self):
        """Test atribute discounts for CompraPublica api"""
        self.assertEqual(self.cp.discounts, 0.0)

    def test_atribute_charges(self):
        """Test atribute charges for CompraPublica api"""
        self.assertEqual(self.cp.charges, 0.0)

    def test_atribute_total_net(self):
        """Test atribute total_net for CompraPublica api"""
        self.assertEqual(self.cp.total_net, 35000.0)

    def test_atribute_iva(self):
        """Test atribute iva for CompraPublica api"""
        self.assertEqual(self.cp.iva, 19.0)

    def test_atribute_taxes(self):
        """Test atribute taxes for CompraPublica api"""
        self.assertEqual(self.cp.taxes, 6650.0)

    def test_atribute_total(self):
        """Test atribute total for CompraPublica api"""
        self.assertEqual(self.cp.total, 41650.0)

    def test_atribute_financing(self):
        """Test atribute financing for CompraPublica api"""
        self.assertEqual(self.cp.financing, "")

    def test_atribute_country(self):
        """Test atribute country for CompraPublica api"""
        self.assertEqual(self.cp.country, "CL")

    def test_atribute_delivery_type(self):
        """Test atribute delivery_type for CompraPublica api"""
        self.assertEqual(self.cp.delivery_type, "7")

    def test_atribute_payment_type(self):
        """Test atribute payment_type for CompraPublica api"""
        self.assertEqual(self.cp.payment_type, "2")

    def test_last_five(self):
        """Last_five method parses CompraPublica api reponse correctly"""
        CompraPublica(
            supplier_state='Nueva orden de compra',
            charges=0.0,
            payment_type='2',
            delivery_type='7',
            name='CARNES',
            taxes=68360.0,
            type_code='9',
            id=19,
            country='CL',
            classification_mean=4.8,
            supplier_state_code='1',
            type_name='CM',
            discounts=0.0,
            iva=19.0,
            code='1816-1026-CM17',
            total_net=359790.0,
            description=('Cubre el 27 y 28 de Diciembre\r\nPosta cubito 13'
                         'kilos\r\nPosta Juliana 12 kilos\r\nSobrecostilla'
                         '170 trozos de 200 grs.\r\nTrutro corto 170 unida'
                         'des de 220 grs.\r\nCDP 01'),
            total=428150.0,
            financing='',
            state_code=4,
            has_items='1',
            state_name='Enviada a proveedor',
            tender_code=None,
            classification_n=5,
            currency='CLP').save()
        CompraPublica(
            supplier_state='Nueva orden de compra',
            charges=0.0,
            payment_type='2',
            delivery_type='7',
            name='CARNES',
            taxes=49466.0,
            type_code='9',
            id=20,
            country='CL',
            classification_mean=2.0,
            supplier_state_code=1,
            type_name='CM',
            discounts=8052.0,
            iva=19.0,
            code='1816-1028-CM17',
            total_net=268400.0,
            description='Cubre del 29 de Diciembre al 02 de Enero\r\nCDP 01',
            total=309814.0,
            state_code=4,
            financing='',
            has_items='1',
            state_name='Enviada a proveedor',
            tender_code=None,
            classification_n=1,
            currency='CLP').save()

        CompraPublica(
            supplier_state='Cancelada',
            charges=0.0,
            payment_type='2',
            delivery_type='7',
            name='Adquisición de Cajas - Dirección de Transito',
            taxes=5282.0,
            type_code='8',
            id=21,
            country='CL',
            classification_mean=3.442857142857143,
            supplier_state_code=5,
            type_name='SE',
            discounts=0.0,
            iva=19.0,
            code='3265-837-SE17',
            total_net=27800.0,
            description=('Compra de Materiales de Oficina 2017  DESDE 32'
                         '65-5-LE17. \r\nAdquisición de Cajas para Archi'
                         'vos que serán Utilizados para el Almacenamient'
                         'o de los Permisos de Circulación de Años Anter'
                         'iores  en Bodega.\r\nSegún Formulario Solicitu'
                         'd de Compra N°0841 Dirección de Transito'),
            total=33082.0,
            state_code=9,
            financing='',
            has_items='1',
            state_name='Cancelada',
            tender_code='3265-5-LE17',
            classification_n=14,
            currency='CLP').save()

        CompraPublica(
            supplier_state='En proceso',
            charges=0.0,
            payment_type='2',
            delivery_type='7',
            name='DESRATIZACION Y DESINFECCION',
            taxes=119121.0,
            type_code='8',
            id=22,
            country='CL',
            classification_mean=0.0,
            supplier_state_code=2,
            type_name='SE',
            discounts=0.0,
            iva=19.0,
            code='4686-1709-SE17',
            total_net=626951.0,
            description=('DESRATIZACION Y DESINFECCION DEL EDIFICIO CONG'
                         'RESO NACIONAL SEDE SANTIAGO Y CAMARA DE DIPUTA'
                         'DOS EN VALPARAISO, SOLICITADO POR DIRECCION DE'
                         'ADMINISTRACION, SEGUN RESOLUCION N° 672-2017'),
            total=746072.0,
            state_code=5,
            financing='',
            has_items='1',
            state_name='En proceso',
            tender_code=None,
            classification_n=0,
            currency='CLP').save()

        CompraPublica(
            supplier_state='Nueva orden de compra',
            charges=0.0,
            payment_type='2',
            delivery_type='12',
            name='Servicio de impresión recetarios Adultos mayores',
            taxes=47880.0,
            type_code='8',
            id=23,
            country='CL',
            classification_mean=5.0,
            supplier_state_code=1,
            type_name='SE',
            discounts=0.0,
            iva=19.0,
            code='5857-43-SE17',
            total_net=252000.0,
            description=('Servicio de impresión recetarios Adultos mayores'
                         '\r\nd.a. 981 donde aprueba convenio promocion de'
                         ' salud \r\nd.a. compra 1602 de fecha 18.02.2017'),
            total=299880.0,
            state_code=4,
            financing='',
            has_items='1',
            state_name='Enviada a proveedor',
            tender_code=None,
            classification_n=2,
            currency='CLP').save()
        last_five = CompraPublica.get_last_five(FakeRequestList)
        self.assertEqual(last_five[0].code, '1816-1026-CM17')
        self.assertEqual(last_five[1].code, '1816-1028-CM17')
        self.assertEqual(last_five[2].code, '3265-837-SE17')
        self.assertEqual(last_five[3].code, '4686-1709-SE17')
        self.assertEqual(last_five[4].code, '5857-43-SE17')

    def test_null_tender_code(self):
        """Model accepts None value for tender_code"""
        CompraPublica(
            supplier_state='Nueva orden de compra',
            charges=0.0,
            payment_type='2',
            delivery_type='7',
            name='ADQUISICION DE EQUIPAMIENTO DE OFICINA',
            taxes=87843.0,
            type_code='9',
            id=4,
            country='CL',
            classification_mean=3.9301204819277107,
            supplier_state_code='1',
            type_name='CM',
            discounts=9435.0,
            iva=19.0,
            code='1001546-31-CM17',
            total_net=471768.0,
            description=('Ítem 29.05.001\r\nFacturar a nombre: Primer Trib'
                         'unal Ambiental con asiento en Antofagasta. Rut N'
                         '°61.999.230-K \r\nDirección: Avda. Jose Miguel C'
                         'arrera N°1579, Antofagasta. \r\nHorario de entre'
                         'ga: Lunes a Jueves 08:30-18:00 hrs. y Viernes 08'
                         ':30-14:30 hrs.\r\n'),
            total=550176.0,
            state_code=4,
            financing='',
            has_items='1',
            state_name='Enviada a proveedor',
            tender_code=None,
            classification_n=83,
            currency='CLP').save()
        self.assertIs(CompraPublica.create('1001546-31-CM17').tender_code,
                      None)
