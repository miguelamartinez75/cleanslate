from django.urls import path
from . import views

urlpatterns = [
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

    # Resumen por puesto
    path('resporpuesto/<int:id_estruc>', views.mostrar_resumen_por_puesto),

    # Tablero sunburst
    path('tablero/<int:id_obj>/<date_Until_text>', views.armar_tablero),
]
