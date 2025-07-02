from rest_framework import viewsets, permissions
from django_filters.rest_framework import DjangoFilterBackend
from .models import Tarea
from .serializers import TareaSerializer

class TareaViewSet(viewsets.ModelViewSet):
    serializer_class = TareaSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['completada', 'titulo']  # ← aquí defines los campos filtrables

    def get_queryset(self):
        return Tarea.objects.filter(usuario=self.request.user)

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)
