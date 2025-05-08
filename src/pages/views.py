import os
from django import get_version
from django.conf import settings
from django.shortcuts import render
from up.clases import Persona, Curso  # Importa las clases del archivo up/clases.py

def home(request):
    # Crea instancias de las clases
    persona = Persona("Benjamin", 28)
    curso = Curso("Fundamentos de Django", "4 semanas")

    # Arma el contexto completo
    context = {
        "debug": settings.DEBUG,
        "django_ver": get_version(),
        "python_ver": os.environ.get("PYTHON_VERSION", "no definida"),
        "nombre": persona.nombre,
        "curso": curso.titulo,
        "duracion": curso.duracion,
    }

    return render(request, "pages/home.html", context)
