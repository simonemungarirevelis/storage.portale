# Generated by Django 3.0.8 on 2020-09-12 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ricerca_app', '0003_auto_20200912_1745'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ricercaaster1',
            options={'ordering': ('descrizione',), 'verbose_name_plural': 'Aster 1'},
        ),
        migrations.AlterModelOptions(
            name='ricercaaster2',
            options={'ordering': ('ricerca_aster1',), 'verbose_name_plural': 'Aster 2'},
        ),
        migrations.AlterModelOptions(
            name='ricercadocentegruppo',
            options={'ordering': ('-dt_fine',), 'verbose_name_plural': 'Docente Gruppi di Ricerca'},
        ),
        migrations.AlterModelOptions(
            name='ricercagruppo',
            options={'ordering': ('nome',), 'verbose_name_plural': 'Gruppo di Ricerca'},
        ),
        migrations.AlterModelOptions(
            name='ricercalineaapplicata',
            options={'ordering': ('ricerca_aster2',), 'verbose_name_plural': 'Linea Applicata'},
        ),
        migrations.AlterModelOptions(
            name='ricercalineabase',
            options={'ordering': ('ricerca_erc2',), 'verbose_name_plural': 'Linea di Base'},
        ),
        migrations.AlterField(
            model_name='ricercaaster1',
            name='descrizione',
            field=models.TextField(db_column='DESCRIZIONE', max_length=200),
        ),
        migrations.AlterField(
            model_name='ricercaaster2',
            name='descrizione',
            field=models.TextField(db_column='DESCRIZIONE', max_length=200),
        ),
        migrations.AlterField(
            model_name='ricercaerc1',
            name='descrizione',
            field=models.TextField(db_column='DESCRIZIONE', max_length=200),
        ),
        migrations.AlterField(
            model_name='ricercaerc2',
            name='descrizione',
            field=models.TextField(db_column='DESCRIZIONE', max_length=200),
        ),
        migrations.AlterField(
            model_name='ricercagruppo',
            name='descrizione',
            field=models.TextField(db_column='DESCRIZIONE', max_length=2000),
        ),
        migrations.AlterField(
            model_name='ricercalineaapplicata',
            name='descr_pubblicaz_prog_brevetto',
            field=models.TextField(blank=True, db_column='DESCR_PUBBLICAZ_PROG_BREVETTO', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='ricercalineaapplicata',
            name='descrizione',
            field=models.TextField(db_column='DESCRIZIONE', max_length=400),
        ),
        migrations.AlterField(
            model_name='ricercalineabase',
            name='descrizione',
            field=models.TextField(db_column='DESCRIZIONE', max_length=400),
        ),
    ]