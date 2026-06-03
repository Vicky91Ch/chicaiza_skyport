from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Aerolinea, Vuelo
from .serializers import AerolineaSerializer, VueloSerializer
from .permissions import IsAdminOrReadOnly

class AerolineaViewSet(viewsets.ModelViewSet):
    queryset = Aerolinea.objects.all().order_by("id")
    serializer_class = AerolineaSerializer
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ["nombre"]
    ordering_fields = ["codigo", "nombre"]

class VueloViewSet(viewsets.ModelViewSet):
    queryset = Vuelo.objects.select_related("Aerolinea").all().order_by("-id")
    serializer_class = VueloSerializer
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["Aerolinea","activo"]
    search_fields = ["codigo", "destino"]
    ordering_fields = ["precio_base"]

    def get_queryset(self):
        qs = super().get_queryset()
        anio_min = self.request.query_params.get("anio_min")
        anio_max = self.request.query_params.get("anio_max")
        if anio_min:
            qs = qs.filter(anio__gte=int(anio_min))
        if anio_max:
            qs = qs.filter(anio__lte=int(anio_max))
        return qs

    def get_permissions(self):
        # Público: SOLO listar vehículos
        if self.action == "list":
            return [AllowAny()]
        return super().get_permissions()