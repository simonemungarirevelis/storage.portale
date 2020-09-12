# Generated by Django 3.0.8 on 2020-09-12 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ricerca_app', '0002_auto_20200912_1624'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='personale',
            options={'verbose_name_plural': 'Personale'},
        ),
        migrations.AlterField(
            model_name='ricercadocentegruppo',
            name='dt_fine',
            field=models.DateField(blank=True, db_column='DT_FINE', null=True),
        ),
        migrations.AlterField(
            model_name='ricercadocentegruppo',
            name='dt_inizio',
            field=models.DateField(blank=True, db_column='DT_INIZIO', null=True),
        ),
        migrations.AlterField(
            model_name='ricercadocentelineaapplicata',
            name='dt_fine',
            field=models.DateField(blank=True, db_column='DT_FINE', null=True),
        ),
        migrations.AlterField(
            model_name='ricercadocentelineaapplicata',
            name='dt_inizio',
            field=models.DateField(blank=True, db_column='DT_INIZIO', null=True),
        ),
        migrations.AlterField(
            model_name='ricercadocentelineabase',
            name='dt_fine',
            field=models.DateField(blank=True, db_column='DT_FINE', null=True),
        ),
        migrations.AlterField(
            model_name='ricercadocentelineabase',
            name='dt_inizio',
            field=models.DateField(blank=True, db_column='DT_INIZIO', null=True),
        ),
    ]
