
# API de Tareas - Django REST Framework

Este proyecto es una API RESTful para la gestión de tareas, implementada con Django y Django REST Framework. Incluye autenticación JWT, CRUD completo, filtros, paginación, y pruebas automatizadas.

**Autor:** Joan López

---

## 🔐 Autenticación JWT

La API utiliza `djangorestframework-simplejwt` para la autenticación basada en tokens.

### Obtener Token:
- **POST** `/api/token/`
```json
{
  "username": "tu_usuario",
  "password": "tu_contraseña"
}
```

### Refresh Token:
- **POST** `/api/token/refresh/`
```json
{
  "refresh": "tu_refresh_token"
}
```

Incluye el token en tus peticiones con el encabezado:

```
Authorization: Bearer tu_access_token
```

---

## 📦 Endpoints CRUD

Todos los endpoints requieren autenticación:

- **GET** `/api/tareas/` → Lista tus tareas
- **POST** `/api/tareas/` → Crea una nueva tarea
- **PUT** `/api/tareas/{id}/` → Actualiza una tarea existente
- **DELETE** `/api/tareas/{id}/` → Elimina una tarea

---

## 🔍 Filtros y paginación

Puedes aplicar filtros directamente en la URL:

- Filtrar por estado:
  ```
  /api/tareas/?completada=true
  ```
- Filtrar por título:
  ```
  /api/tareas/?titulo=Estudiar Django
  ```

La paginación está activa con 5 elementos por página:
```
/api/tareas/?page=2
```

---

## 🧪 Pruebas Automatizadas

Ejecuta:

```
python manage.py test
```

Se incluyen las siguientes pruebas:
- Usuario autenticado puede crear una tarea
- Usuario no autenticado recibe error 401

---

## 🚀 Ejecución del proyecto

1. Clona el repositorio
2. Instala dependencias:  
   `pip install -r requirements.txt`
3. Aplica migraciones:  
   `python manage.py migrate`
4. Crea un superusuario:  
   `python manage.py createsuperuser`
5. Ejecuta el servidor:  
   `python manage.py runserver`

---

## 🛠 Tecnologías

- Django
- Django REST Framework
- SimpleJWT
- django-filter
- Postman (para pruebas)
