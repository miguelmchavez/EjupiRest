# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Colectivo(models.Model):
    id_colectivo = models.AutoField(primary_key=True)
    id_recorrido = models.ForeignKey('Recorrido', models.DO_NOTHING, db_column='id_recorrido', blank=True, null=True)
    desc_colectivo = models.CharField(max_length=128, blank=True, null=True)
    id_device = models.BigIntegerField(blank=True, null=True)
    id_unico = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'colectivo'


class Detalleparada(models.Model):
    id_detalleparada = models.AutoField(primary_key=True)
    id_parada = models.ForeignKey('Parada', models.DO_NOTHING, db_column='id_parada', blank=True, null=True)
    id_recorrido = models.ForeignKey('Recorrido', models.DO_NOTHING, db_column='id_recorrido', blank=True, null=True)
    #id_recorrido = models.ForeignKey('Recorrido', related_name='linea', db_column='id_recorrido', on_delete=models.CASCADE)
    id_orden = models.ForeignKey('Orden', models.DO_NOTHING, db_column='id_orden', blank=True, null=True)
    tiempo_marcha = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'detalleparada'


class Detallerecorrido(models.Model):
    id_detallerecorrido = models.AutoField(primary_key=True)
    #id_recorrido = models.ForeignKey('Recorrido', related_name='detalles', db_column='id_recorrido', on_delete=models.CASCADE)
    id_recorrido = models.ForeignKey('Recorrido', models.DO_NOTHING, db_column='id_recorrido', blank=True, null=True)
    lat_detallerecorrido = models.FloatField(blank=True, null=True)
    lng_detallerecorrido = models.FloatField(blank=True, null=True)
    orden_detallerecorrido = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'detallerecorrido'
        ordering = ['id_detallerecorrido']


class Empresa(models.Model):
    id_empresa = models.AutoField(primary_key=True)
    desc_empresa = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'empresa'


class Frecuencia(models.Model):
    id_frecuencia = models.AutoField(primary_key=True)
    id_recorrido = models.ForeignKey('Recorrido', models.DO_NOTHING, db_column='id_recorrido', blank=True, null=True)
    inicio = models.TimeField(blank=True, null=True)
    fin = models.TimeField(blank=True, null=True)
    frecuencia = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'frecuencia'


class Linea(models.Model):
    id_linea = models.AutoField(primary_key=True)
    id_empresa = models.ForeignKey(Empresa, models.DO_NOTHING, db_column='id_empresa', blank=True, null=True)
    desc_linea = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'linea'


class Orden(models.Model):
    id_orden = models.AutoField(primary_key=True)
    desc_orden = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orden'


class Parada(models.Model):
    id_parada = models.AutoField(primary_key=True)
    desc_parada = models.CharField(max_length=128, blank=True, null=True)
    lat_parada = models.FloatField(blank=True, null=True)
    lng_parada = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'parada'
        ordering = ['id_parada']


class Recorrido(models.Model):
    id_recorrido = models.AutoField(primary_key=True)
    id_linea = models.ForeignKey(Linea, models.DO_NOTHING, db_column='id_linea', blank=True, null=True)
    desc_recorrido = models.CharField(max_length=128, blank=True, null=True)
    sub_recorrido = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'recorrido'
        ordering = ['id_recorrido']


class Ubicacion(models.Model):
    id_ubicacion = models.AutoField(primary_key=True)
    id_colectivo = models.ForeignKey(Colectivo, models.DO_NOTHING, db_column='id_colectivo', blank=True, null=True)
    desc_ubicacion = models.CharField(max_length=128, blank=True, null=True)
    lat_ubicacion = models.FloatField(blank=True, null=True)
    lng_ubicacion = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ubicacion'
