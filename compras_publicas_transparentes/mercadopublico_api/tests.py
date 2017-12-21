from django.test import TestCase

from .models import CompraPublica

#TODO: FIX: test_last_five still relies on api connection

#{'Codigo': 10500,
 #'Mensaje': 'Lo sentimos. Hemos detectado que existen peticiones simultáneas.'}

class fake_request():
    def get(url):
        return fake_response()

class fake_response():
    def json(self):
        return {"Cantidad":1,
            "FechaCreacion":"2017-12-20T13:22:22.64",
            "Version":"v1",
            "Listado":[{"Codigo":"2097-241-SE14",
                "Nombre":"Insumos dentales especialidades",
                "CodigoEstado":6,
                "Estado":"Aceptada",
                "CodigoLicitacion":"2097-165-L113",
                "Descripcion": ("Insumos dentales especialidades DESDE 209"
                                "7-165-L113\r\nDENTAL ESPECIALIDADES"),
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
                "Comprador":{"CodigoOrganismo":"7398",
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
                "Proveedor":{"Codigo":"1316979",
                    "Nombre":"COMERCIALIZADORA ILHABELLA EIRL",
                    "Actividad":("VENTA AL POR MAYOR DE OTROS PRODUCTOS N."
                                 "C.P.| VENT"),
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
                "Items":{"Cantidad":1,
                    "Listado":[{"Correlativo":1,
                        "CodigoCategoria":30201900,
                        "Categoria":"Artículos para estructuras,obras y construcciones / Estructuras prefabricadas / Construcciones médicas prefabricadas",
                        "CodigoProducto":30201903,
                        "Producto":"Unidades dentales",
                        "EspecificacionComprador":"Ultracal",
                        "EspecificacionProveedor":" Ultracal.ULTRADENT. PRODUCTO AMERICANO. JERINGA 3 GRS. KIT X 4 UNIDADES.  FECHA DE VENCIMIENTO 2018. SE ADJUNTA CATALOGO DE PRODUCTO. INCLUY FLETE. DESPACHO 24 HRS. PUESTO EN BODEGAS DE HOSPITAL DE ARAUCO.",
                        "Cantidad":1.0,
                        "Unidad":None,
                        "Moneda":"CLP",
                        "PrecioNeto":35000.0,
                        "TotalCargos":0.0,
                        "TotalDescuentos":0.0,
                        "TotalImpuestos":0.0,
                        "Total":35000.0}]}}]}

class fake_request_all():
    def get(url):
        return fake_response_all()

class fake_response_all():
    def json(self):
        return {'Cantidad': 6,
                'Version': 'v1',
                'FechaCreacion': '2017-12-21T00:37:06.397',
                'Listado': [
                    {'CodigoEstado': 4,
                    'Codigo': '1816-1026-CM17',
                    'Nombre': 'CARNES'},
                    {'CodigoEstado': 4,
                    'Codigo': '1816-1028-CM17',
                    'Nombre': 'CARNES'},
                    {'CodigoEstado': 9,
                    'Codigo': '3265-837-SE17',
                    'Nombre': ('Adquisición de Cajas - Dirección de Transi'
                               'to')},
                    {'CodigoEstado': 5,
                    'Codigo': '4686-1709-SE17',
                    'Nombre': 'DESRATIZACION Y DESINFECCION'},
                    {'CodigoEstado': 4,
                    'Codigo': '5857-43-SE17',
                    'Nombre': ('Servicio de impresión recetarios Adultos ma'
                               'yores')},
                    {'CodigoEstado': 6,
                    'Codigo': '617807-7419-SE17',
                    'Nombre': 'HOSLA COMPRA DE SERVICIOS PROFESIONALES'}]}


class CompraPublicaModelTests(TestCase):

    def setUp(self):
        self.cp = CompraPublica.create('fakecode',fake_request)

    def test_exists(self):
        """Model CompraPublica exists, is installed and migrated."""
        pass

    def test_empty_comprapublica(self):
        """CompraPublica object created with no arguments is empty"""
        self.assertIs(CompraPublica().name,"")

    def test_atribute_code(self):
        """Test atribute code for CompraPublica api"""
        self.assertEqual(self.cp.code,"2097-241-SE14")

    def test_atribute_name(self):
        """Test atribute name for CompraPublica api"""
        self.assertEqual(self.cp.name,"Insumos dentales especialidades")

    def test_atribute_state_code(self):
        """Test atribute state_code for CompraPublica api"""
        self.assertEqual(self.cp.state_code,6)

    def test_atribute_state_name(self):
        """Test atribute state_name for CompraPublica api"""
        self.assertEqual(self.cp.state_name,"Aceptada")

    def test_atribute_tender_code(self):
        """Test atribute tender_code for CompraPublica api"""
        self.assertEqual(self.cp.tender_code,"2097-165-L113")

    def test_atribute_description(self):
        """Test atribute description for CompraPublica api"""
        self.assertEqual(self.cp.description,"Insumos dentales especialidades DESDE 2097-165-L113\r\nDENTAL ESPECIALIDADES")

    def test_atribute_type_code(self):
        """Test atribute type_code for CompraPublica api"""
        self.assertEqual(self.cp.type_code,"8")

    def test_atribute_type_name(self):
        """Test atribute type_name for CompraPublica api"""
        self.assertEqual(self.cp.type_name,"SE")

    def test_atribute_currency(self):
        """Test atribute currency for CompraPublica api"""
        self.assertEqual(self.cp.currency,"CLP")

    def test_atribute_supplier_state_code(self):
        """Test atribute supplier_state_code for CompraPublica api"""
        self.assertEqual(self.cp.supplier_state_code,4)

    def test_atribute_supplier_state(self):
        """Test atribute supplier_state for CompraPublica api"""
        self.assertEqual(self.cp.supplier_state,"Aceptada")

    def test_atribute_has_items(self):
        """Test atribute has_items for CompraPublica api"""
        self.assertEqual(self.cp.has_items,"1")

    def test_atribute_classification_mean(self):
        """Test atribute classification_mean for CompraPublica api"""
        self.assertEqual(self.cp.classification_mean,3.9333333333333331)

    def test_atribute_classification(self):
        """Test atribute classification for CompraPublica api"""
        self.assertEqual(self.cp.classification_n,6)

    def test_atribute_discounts(self):
        """Test atribute discounts for CompraPublica api"""
        self.assertEqual(self.cp.discounts,0.0)

    def test_atribute_charges(self):
        """Test atribute charges for CompraPublica api"""
        self.assertEqual(self.cp.charges,0.0)

    def test_atribute_total_net(self):
        """Test atribute total_net for CompraPublica api"""
        self.assertEqual(self.cp.total_net,35000.0)

    def test_atribute_iva(self):
        """Test atribute iva for CompraPublica api"""
        self.assertEqual(self.cp.iva,19.0)

    def test_atribute_taxes(self):
        """Test atribute taxes for CompraPublica api"""
        self.assertEqual(self.cp.taxes,6650.0)

    def test_atribute_total(self):
        """Test atribute total for CompraPublica api"""
        self.assertEqual(self.cp.total,41650.0)

    def test_atribute_financing(self):
        """Test atribute financing for CompraPublica api"""
        self.assertEqual(self.cp.financing,"")

    def test_atribute_country(self):
        """Test atribute country for CompraPublica api"""
        self.assertEqual(self.cp.country,"CL")

    def test_atribute_delivery_type(self):
        """Test atribute delivery_type for CompraPublica api"""
        self.assertEqual(self.cp.delivery_type,"7")

    def test_atribute_payment_type(self):
        """Test atribute payment_type for CompraPublica api"""
        self.assertEqual(self.cp.payment_type,"2")

    def test_last_five(self):
        """Last_five method parses CompraPublica api reponse correctly"""
        CompraPublica(supplier_state='Nueva orden de compra',
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
              description=('Cubre el 27 y 28 de Diciembre\r\nPosta cubito '
                           '13 kilos\r\nPosta Juliana 12 kilos\r\nSobrecos'
                           'tilla 170 trozos de 200 grs.\r\nTrutro corto 1'
                           '70 unidades de 220 grs.\r\nCDP 01'),
              total=428150.0,
              financing='',
              state_code=4,
              has_items='1',
              state_name='Enviada a proveedor',
              tender_code=None,
              classification_n=5,
              currency='CLP').save()
        
        CompraPublica(supplier_state='Nueva orden de compra',
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

        CompraPublica(supplier_state='Cancelada',
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

        CompraPublica(supplier_state='En proceso',
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

        CompraPublica(supplier_state='Nueva orden de compra',
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
              description=('Servicio de impresión recetarios Adultos mayor'
                           'es\r\nd.a. 981 donde aprueba convenio promocio'
                           'n de salud \r\nd.a. compra 1602 de fecha 18.02'
                           '.2017'),
              total=299880.0,
              state_code=4,
              financing='',
              has_items='1',
              state_name='Enviada a proveedor',
              tender_code=None,
              classification_n=2,
              currency='CLP').save()
        last_five = CompraPublica.get_last_five(fake_request_all)
        self.assertEqual(last_five[0].code,'1816-1026-CM17')
        self.assertEqual(last_five[1].code,'1816-1028-CM17')
        self.assertEqual(last_five[2].code,'3265-837-SE17')
        self.assertEqual(last_five[3].code,'4686-1709-SE17')
        self.assertEqual(last_five[4].code,'5857-43-SE17')

    def test_null_tender_code(self):
        """Model accepts None value for tender_code"""
        CompraPublica(supplier_state='Nueva orden de compra',
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
        self.assertIs(CompraPublica.create('1001546-31-CM17').tender_code,None)
