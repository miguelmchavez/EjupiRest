# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


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
    #reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)
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


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


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
