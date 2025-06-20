from django.contrib import admin
from .models import Perro, PersonasAdoptantes, Adopcion

@admin.register(Perro)
class PerroAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'raza', 'edad', 'tamaño', 'estado', 'vacunado')
    search_fields = ('nombre', 'raza')
    list_filter = ('estado', 'raza', 'edad', 'tamaño', 'vacunado')

@admin.register(PersonasAdoptantes)
class PersonasAdoptantesAdmin(admin.ModelAdmin):
    list_display = ('user', 'dni', 'telefono', 'preferencias_raza', 'preferencias_edad', 'preferencias_tamaño')
    search_fields = ('user__username', 'dni', 'telefono')
    list_filter = ('preferencias_raza', 'preferencias_edad', 'preferencias_tamaño')

@admin.register(Adopcion)
class AdopcionAdmin(admin.ModelAdmin):
    list_display = ('perro', 'usuario', 'fecha_adopcion', 'completada')
    list_filter = ('completada', 'fecha_adopcion')
    search_fields = ('perro__nombre', 'usuario__user__username')
# Register your models here.
