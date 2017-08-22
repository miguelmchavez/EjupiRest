from django.http import HttpResponse, HttpResponseRedirect
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from django.template import RequestContext, loader
from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth.models import User, Group
from django.db.models import Count
from django.core import serializers
from collections import defaultdict
from rest_framework import viewsets, filters, generics
from rest_framework.response import Response
from rest_framework.permissions import (IsAuthenticated, IsAuthenticatedOrReadOnly, DjangoModelPermissions, DjangoObjectPermissions, IsAdminUser, AllowAny)
from api.serializers import ColectivoSerializer, DetalleparadaSerializer, DetallerecorridoSerializer, EmpresaSerializer, FrecuenciaSerializer, LineaSerializer, OrdenSerializer, ParadaSerializer, RecorridoSerializer, UbicacionSerializer
from api.models import Colectivo, Detalleparada, Detallerecorrido, Empresa, Frecuencia, Linea, Orden, Parada, Recorrido, Ubicacion
from rest_framework.pagination import PageNumberPagination
from api.filters import DetalleparadaFilter, DetallerecorridoFilter
from api.extras import coordenadas
import math

class StandardResultsSetPagination(PageNumberPagination):
	page_size = 1000
	page_size_query_param = 'page_size'
	max_page_size = 1000

class ColectivoViewSet(viewsets.ModelViewSet):
	"""
	Colectivo.
	"""
	permission_classes = [IsAuthenticatedOrReadOnly]
	queryset = Colectivo.objects.all()
	serializer_class = ColectivoSerializer

class DetalleparadaViewSet(viewsets.ModelViewSet):
	"""
	Detalleparada.
	"""
	permission_classes = [IsAuthenticatedOrReadOnly]
	queryset = Detalleparada.objects.all()
	serializer_class = DetalleparadaSerializer
	filter_class = DetalleparadaFilter

	def ruta(request, olat, olng, dlat, dlng):
		if request.method == 'GET':
			"""olat = (float, request.GET.getlist('olat'))
			olng = (float, request.GET.getlist('olng'))
			dlat = (float, request.GET.getlist('dlat'))
			dlng = (float, request.GET.getlist('dlng'))"""
			validado = coordenadas(olat, olng, dlat, dlng)
			return HttpResponse(validado)

class DetallerecorridoViewSet(viewsets.ModelViewSet):
	"""
	Detallerecorrido.
	"""
	permission_classes = [IsAuthenticatedOrReadOnly]
	queryset = Detallerecorrido.objects.all()
	serializer_class = DetallerecorridoSerializer
	filter_class = DetallerecorridoFilter

class EmpresaViewSet(viewsets.ModelViewSet):
	"""
	Empresa.
	"""
	permission_classes = [IsAuthenticatedOrReadOnly]
	queryset = Empresa.objects.all()
	serializer_class = EmpresaSerializer

class FrecuenciaViewSet(viewsets.ModelViewSet):
	"""
	Frecuencia.
	"""
	permission_classes = [IsAuthenticatedOrReadOnly]
	queryset = Frecuencia.objects.all()
	serializer_class = FrecuenciaSerializer

class LineaViewSet(viewsets.ModelViewSet):
	"""
	Linea.
	"""
	permission_classes = [IsAuthenticatedOrReadOnly]
	queryset = Linea.objects.all()
	serializer_class = LineaSerializer

class OrdenViewSet(viewsets.ModelViewSet):
	"""
	Orden.
	"""
	permission_classes = [IsAuthenticatedOrReadOnly]
	queryset = Orden.objects.all()
	serializer_class = OrdenSerializer

class ParadaViewSet(viewsets.ModelViewSet):
	"""
	Parada.
	"""
	permission_classes = [IsAuthenticatedOrReadOnly]
	queryset = Parada.objects.all()
	serializer_class = ParadaSerializer

class RecorridoViewSet(viewsets.ModelViewSet):
	"""
	Recorrido.
	"""
	permission_classes = [IsAuthenticatedOrReadOnly]
	queryset = Recorrido.objects.all()
	serializer_class = RecorridoSerializer

class UbicacionViewSet(viewsets.ModelViewSet):
	"""
	Ubicacion.
	"""
	permission_classes = [IsAuthenticatedOrReadOnly]
	queryset = Ubicacion.objects.all()
	serializer_class = UbicacionSerializer
