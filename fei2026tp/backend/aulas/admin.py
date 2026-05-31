from django.contrib import admin

from django.contrib import admin
from .models import Carrera, Profesor, Materia, Aula

admin.site.register(Carrera)
admin.site.register(Profesor)
admin.site.register(Materia)
admin.site.register(Aula)