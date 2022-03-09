from django.urls import path
from . import views

urlpatterns = [
    # path('est/', EstructuraItemViews.as_view()),
    # path('est/<int:id>', EstructuraItemViews.as_view()),
    # Estructura
    path('est/', views.getEstructura),
    path('est/<int:id>', views.getEstructura),
    path('setest/', views.setEstructura),
    path('setest/<int:id>', views.patchEstructura),
    path('delest/<int:id>', views.delEstructura),
    path('estitem/<int:id>', views.getEstructuraItem),

    # Objetivos
    path('objetivo/', views.getObjetivo),
    path('objetivo/<int:id>', views.getObjetivo),
    path('setobjetivo/', views.setObjetivo),
    path('setobjetivo/<int:id>', views.patchObjetivo),
    path('delobjetivo/<int:id>', views.delObjetivo),

    path('tablero/<int:id_obj>/<date_Until_text>', views.armar_tablero),
]
