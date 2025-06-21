from django.urls import path
from . import views

urlpatterns = [
    path('buscar_perros/<int:persona_id>/', views.Macheador, name='buscar_perros'),
]