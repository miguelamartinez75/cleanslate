from django.urls import path
from . import views

urlpatterns = [
    path('est/', views.getEstructura, name='estructura'),
    path('subest/', views.getHijosDe, name='desendientes'),
]
