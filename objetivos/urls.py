from django.urls import path
from . import views

urlpatterns = [
    path('est/', views.getEstructura),
    path('est/<int:id>', views.getEstructura),
    path('setest/', views.setEstructura),
    path('setest/<int:id>', views.patchEstructura),
    path('delest/<int:id>', views.delEstructura),
    path('subest/', views.getHijosDe, name='desendientes'),
    path('objs/', views.getObjetivo),
]
