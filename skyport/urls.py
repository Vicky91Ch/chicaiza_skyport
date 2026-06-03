from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import AerolineaViewSet, VueloViewSet

router = DefaultRouter()
router.register(r"aerolineas", AerolineaViewSet, basename="aerolineas")
router.register(r"vuelos", VueloViewSet, basename="vuelos")

urlpatterns = []
urlpatterns += router.urls