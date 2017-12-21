from django.test import TestCase

from .models import CompraPublica

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
        self.cp = CompraPublica('fakecode',fake_request)

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
        self.assertEqual(CompraPublica.get_last_five(fake_request_all)[0],
                         {'CodigoEstado': 4,
                         'Codigo': '1816-1026-CM17',
                         'Nombre': 'CARNES'}) 
        self.assertEqual(CompraPublica.get_last_five(fake_request_all)[1],
                        {'CodigoEstado': 4,
                         'Codigo': '1816-1028-CM17',
                         'Nombre': 'CARNES'})
        self.assertEqual(CompraPublica.get_last_five(fake_request_all)[2],
                        {'CodigoEstado': 9,
                         'Codigo': '3265-837-SE17',
                         'Nombre': 'Adquisición de Cajas - Dirección de Transito'})
        self.assertEqual(CompraPublica.get_last_five(fake_request_all)[3],
                        {'CodigoEstado': 5,
                         'Codigo': '4686-1709-SE17',
                         'Nombre': 'DESRATIZACION Y DESINFECCION'})
        self.assertEqual(CompraPublica.get_last_five(fake_request_all)[4],
                        {'CodigoEstado': 4,
                         'Codigo': '5857-43-SE17',
                         'Nombre': 'Servicio de impresión recetarios Adultos mayores'})

#    def test_was_published_recently_with_future_questions(self):
#        """
#        was_published_recently() returns False for questions whose pub_date
#        is in the future.
#        """
#        time = timezone.now() + datetime.timedelta(days=30)
#        future_question = Question(pub_date=time)
#        self.assertIs(future_question.was_published_recently(), False)

