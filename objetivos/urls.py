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
    path('estitemname/<int:id>', views.getEstructuraItemName),

    # Objetivos
    path('objetivo/', views.getObjetivo),
    path('objetivo/<int:id>', views.getObjetivo),
    path('setobjetivo/', views.setObjetivo),
    path('setobjetivo/<int:id>', views.patchObjetivo),
    path('delobjetivo/<int:id>', views.delObjetivo),

    # Actividades
    path('actividad/', views.getActividad),
    path('actividad/<int:id>', views.getActividad),

    path('tablero/<int:id_obj>/<date_Until_text>', views.armar_tablero),

    # Resumen
    path('resumen/<int:id_estruc>', views.mostrar_resumen_por_puesto, name='resumen_por_puesto'),
    path('tablero_oai/<int:id_obj>/<date_until_text>/<int:delta_fechas>', views.armar_tablero_oai, name='tablero_oai'),
    ]