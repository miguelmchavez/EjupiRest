from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import Colectivo, Detalleparada, Detallerecorrido, Empresa, Frecuencia, Linea, Orden, Parada, Recorrido, Ubicacion

class ColectivoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Colectivo
		fields = ('id_colectivo', 'desc_colectivo')

class DetallerecorridoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Detallerecorrido
		fields = ('id_detallerecorrido', 'id_recorrido', 'lat_detallerecorrido', 'lng_detallerecorrido', 'orden_detallerecorrido')

class EmpresaSerializer(serializers.ModelSerializer):
	class Meta:
		model = Empresa
		fields = ('id_empresa', 'desc_empresa')

class FrecuenciaSerializer(serializers.ModelSerializer):
	class Meta:
		model = Frecuencia
		fields = ('id_frecuencia', 'frecuencia')

class LineaSerializer(serializers.ModelSerializer):
	class Meta:
		model = Linea
		fields = ('id_linea', 'desc_linea')

class OrdenSerializer(serializers.ModelSerializer):
	class Meta:
		model = Orden
		fields = ('id_orden', 'desc_orden')

class ParadaSerializer(serializers.ModelSerializer):
	class Meta:
		model = Parada
		fields = ('id_parada', 'desc_parada', 'lat_parada', 'lng_parada')

class RecorridoSerializer(serializers.ModelSerializer):
	#detalles = DetallerecorridoSerializer(many=True)

	class Meta:
		model = Recorrido
		fields = ('id_recorrido', 'desc_recorrido')

class UbicacionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Ubicacion
		fields = ('id_ubicacion', 'desc_ubicacion')

class DetalleparadaSerializer(serializers.ModelSerializer):
	id_recorrido = RecorridoSerializer(many=False)
	id_parada = ParadaSerializer(many=False)

	class Meta:
		model = Detalleparada
		fields = ('id_parada', 'id_recorrido' ,'tiempo_marcha')