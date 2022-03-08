from django.urls import path
from . import views

urlpatterns = [
    path('est/', views.getEstructura, name='estructura'),
    path('setest/', views.setEstructura, name='set-estructura'),
    path('subest/', views.getHijosDe, name='desendientes'),
    path('objs/', views.getObjetivo, name='objetivo'),
]
