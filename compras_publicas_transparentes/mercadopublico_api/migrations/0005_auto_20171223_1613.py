# Generated by Django 2.0 on 2017-12-23 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mercadopublico_api', '0004_auto_20171221_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comprapublica',
            name='state_code',
            field=models.PositiveSmallIntegerField(choices=[(4, 'Enviada a Proveedor'), (5, 'En proceso'), (6, 'Aceptada'), (9, 'Cancelada'), (12, 'Recepción Conforme'), (13, 'Pendiente de Recepcionar'), (14, 'Recepcionada Parcialmente'), (15, 'Recepcion Conforme Incompleta')]),
        ),
    ]
