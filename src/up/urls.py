from django.urls import path
from up import views

urlpatterns = [
    path('', views.index, name='index'),           # Página principal que muestra las clases
    path('databases/', views.databases, name='databases'),  # Conexión a Redis y PostgreSQL
    path('practica/', views.index, name='practica'),        # Ruta opcional para la actividad
]
