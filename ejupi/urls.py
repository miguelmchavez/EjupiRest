from django.conf.urls import url, include
from rest_framework import routers
from api import views
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.contrib import admin

router = routers.DefaultRouter()
router.register(r'colectivo', views.ColectivoViewSet)
router.register(r'detalleparada', views.DetalleparadaViewSet)
router.register(r'detallerecorrido', views.DetallerecorridoViewSet)
router.register(r'empresa', views.EmpresaViewSet)
router.register(r'frecuencia', views.FrecuenciaViewSet)
router.register(r'linea', views.LineaViewSet)
router.register(r'orden', views.OrdenViewSet)
router.register(r'parada', views.ParadaViewSet)
router.register(r'recorrido', views.RecorridoViewSet)
router.register(r'ubicacion', views.UbicacionViewSet)

urlpatterns = [
    url(r'^api/v1/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/v1/detalleparada/ruta/(?P<olat>([-+]?([1-8]?\d(\.\d+)?)))/(?P<olng>([-+]?([1-8]?\d(\.\d+)?)))/(?P<dlat>([-+]?([1-8]?\d(\.\d+)?)))/(?P<dlng>([-+]?([1-8]?\d(\.\d+)?)))/$', views.DetalleparadaViewSet.ruta),
]
