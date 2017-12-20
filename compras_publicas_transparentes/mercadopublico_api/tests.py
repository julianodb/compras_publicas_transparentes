from django.test import TestCase

from .models import CompraPublica

class fake_request():
    def get(code):
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
                "Descripcion":"Insumos dentales especialidades DESDE 2097-165-L113\r\nDENTAL ESPECIALIDADES",
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
                    "Actividad":"VENTA AL POR MAYOR DE OTROS PRODUCTOS N.C.P.| VENT",
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

class CompraPublicaModelTests(TestCase):

    def test_exists(self):
        """Model CompraPublica exists, is installed and migrated."""
        pass

    def test_empty_comprapublica(self):
        """CompraPublica object created with no arguments is empty"""
        self.assertIs(CompraPublica().name,"")

    def test_correct_atribute_names(self):
        """Test expected atributes names for CompraPublica api"""
        cp = CompraPublica('fakecode',fake_request)
        self.assertEqual(cp.code,"2097-241-SE14")
        self.assertEqual(cp.name,"Insumos dentales especialidades")
        self.assertEqual(cp.state_code,6)
        self.assertEqual(cp.state,"Aceptada")
        self.assertEqual(cp.tender_code,"2097-165-L113")
        self.assertEqual(cp.description,"Insumos dentales especialidades DESDE 2097-165-L113\r\nDENTAL ESPECIALIDADES")
        self.assertEqual(cp.type_code,"8")
        self.assertEqual(cp.type,"SE")
        self.assertEqual(cp.currency,"CLP")
        self.assertEqual(cp.supplier_state_code,"4")
        self.assertEqual(cp.supplier_state,"Aceptada")
        self.assertEqual(cp.has_items,"1")
        self.assertEqual(cp.classification_mean,3.9333333333333331)
        self.assertEqual(cp.classification_n,6)
        self.assertEqual(cp.discounts,0.0)
        self.assertEqual(cp.charges,0.0)
        self.assertEqual(cp.total_net,35000.0)
        self.assertEqual(cp.iva,19.0)
        self.assertEqual(cp.taxes,6650.0)
        self.assertEqual(cp.total,41650.0)
        self.assertEqual(cp.financing,"")
        self.assertEqual(cp.country,"CL")
        self.assertEqual(cp.delivery_type,"7")
        self.assertEqual(cp.payment_type,"2")

#    def test_was_published_recently_with_future_questions(self):
#        """
#        was_published_recently() returns False for questions whose pub_date
#        is in the future.
#        """
#        time = timezone.now() + datetime.timedelta(days=30)
#        future_question = Question(pub_date=time)
#        self.assertIs(future_question.was_published_recently(), False)

