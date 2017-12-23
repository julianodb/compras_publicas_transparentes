# Generated by Django 2.0 on 2017-12-21 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mercadopublico_api', '0003_auto_20171220_2341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comprapublica',
            name='currency',
            field=models.CharField(choices=[('CLP', 'Peso Chileno'), ('CLF', 'Unidad de Fomento'), ('USD', 'Dólar Americano'), ('UTM', 'Unidad Tributaria Mensual'), ('EUR', 'Euro')], max_length=3),
        ),
        migrations.AlterField(
            model_name='comprapublica',
            name='delivery_type',
            field=models.CharField(choices=[('7', 'Despachar a Dirección de envío'), ('9', 'Despachar según programa adjuntado'), ('12', 'Otra Forma de Despacho, Ver Instruc'), ('14', 'Retiramos de su bodega'), ('20', 'Despacho por courier o encomienda aérea'), ('21', 'Despacho por courier o encomienda terrestre'), ('22', 'A convenir')], max_length=2),
        ),
        migrations.AlterField(
            model_name='comprapublica',
            name='payment_type',
            field=models.CharField(choices=[('1', '15 días contra la recepción de la factura'), ('2', '30 días contra la recepción de la factura'), ('39', 'Otra forma de pago'), ('46', '50 días contra la recepción de la factura'), ('47', '60 días contra la recepción de la factura')], max_length=10),
        ),
        migrations.AlterField(
            model_name='comprapublica',
            name='state_code',
            field=models.PositiveSmallIntegerField(choices=[(4, 'Enviada a Proveedor'), (6, 'Aceptada'), (9, 'Cancelada'), (12, 'Recepción Conforme'), (13, 'Pendiente de Recepcionar'), (14, 'Recepcionada Parcialmente'), (15, 'Recepcion Conforme Incompleta')]),
        ),
        migrations.AlterField(
            model_name='comprapublica',
            name='tender_code',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='comprapublica',
            name='type_code',
            field=models.CharField(choices=[('1', 'OC - Automática'), ('2', 'D1 - Trato directo que genera Orden de Compra por proveedor único'), ('3', 'C1 - Trato directo que genera Orden de Compra por emergencia, urgencia e imprevisto'), ('4', 'F3 - Trato directo que genera Orden de Compra por confidencialidad'), ('5', 'G1 - Trato directo que genera Orden de Compra por naturaleza de negociación'), ('6', 'R1 - Orden de compra menor a 3UTM'), ('7', 'CA - Orden de compra sin resolución.'), ('8', 'SE - Sin emisión automática'), ('9', 'CM - Convenio Marco'), ('10', 'FG'), ('11', 'TL')], max_length=2),
        ),
    ]
