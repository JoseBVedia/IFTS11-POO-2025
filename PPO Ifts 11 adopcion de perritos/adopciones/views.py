from django.shortcuts import render, get_object_or_404
from .models import PersonasAdoptantes, Perro

def Macheador(request, persona_id):
    persona = get_object_or_404(PersonasAdoptantes, id=persona_id)

    filtros = {'estado': 'disponible'}

    if persona.preferencias_raza != 'Sin_Preferencia':
        filtros['raza'] = persona.preferencias_raza

    if persona.preferencias_edad != 'Sin Preferencia':
        filtros['edad'] = persona.preferencias_edad

    if persona.preferencias_tamaño != 'Sin Preferencia':
        filtros['tamaño'] = persona.preferencias_tamaño

    perros = Perro.objects.filter(**filtros)

    return render(request, 'adopciones/perros_filtrados.html', {
        'persona': persona,
        'perros': perros
    })