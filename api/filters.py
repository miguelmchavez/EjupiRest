import django_filters
from api.models import Detalleparada, Detallerecorrido

class DetalleparadaFilter(django_filters.FilterSet):
	
	parada = django_filters.NumberFilter(name='id_parada')
	recorrido = django_filters.NumberFilter(name='id_recorrido')
	
	class Meta:
		model = Detalleparada
		fields = ('id_parada', 'id_recorrido' ,'tiempo_marcha')

class DetallerecorridoFilter(django_filters.FilterSet):
	
	recorrido = django_filters.NumberFilter(name='id_recorrido')
	
	class Meta:
		model = Detallerecorrido
		fields = ('id_detallerecorrido', 'id_recorrido', 'lat_detallerecorrido', 'lng_detallerecorrido', 'orden_detallerecorrido')


