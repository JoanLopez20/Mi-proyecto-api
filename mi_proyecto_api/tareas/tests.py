from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Tarea
from rest_framework_simplejwt.tokens import RefreshToken

class TareaAPITestCase(APITestCase):

    def setUp(self):
        # Crear usuario
        self.usuario = User.objects.create_user(username='cristian', password='test123456')
        self.token = RefreshToken.for_user(self.usuario).access_token
        self.auth_headers = {'HTTP_AUTHORIZATION': f'Bearer {self.token}'}
        self.url = '/api/tareas/'

    def test_usuario_autenticado_puede_crear_tarea(self):
        data = {
            'titulo': 'Tarea de prueba',
            'descripcion': 'Creada en test',
            'completada': False
        }
        response = self.client.post(self.url, data, **self.auth_headers)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Tarea.objects.count(), 1)
        self.assertEqual(Tarea.objects.get().titulo, 'Tarea de prueba')

    def test_usuario_no_autenticado_no_puede_crear_tarea(self):
        data = {
            'titulo': 'Tarea no autorizada',
            'descripcion': 'No debe crearse',
            'completada': True
        }
        response = self.client.post(self.url, data)  # sin token
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
