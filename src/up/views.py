from django.conf import settings
from django.db import connection
from django.http import HttpResponse
from redis import Redis
from .clases import Persona, Curso  

redis = Redis.from_url(settings.REDIS_URL)

def index(request):
    # Creamos instancias de las clases
    persona = Persona("Benjamin", 28)
    curso = Curso("Fundamentos de Django", "4 semanas")

    # Creamos un mensaje usando atributos de los objetos
    mensaje = f"{persona.nombre} está inscrito en el curso: {curso.titulo} que dura {curso.duracion}"
    return HttpResponse(mensaje)

def databases(request):
    # Verificamos conexiones con Redis y PostgreSQL
    redis.ping()
    connection.ensure_connection()

    return HttpResponse("Conexión a Redis y Base de Datos exitosa.")
