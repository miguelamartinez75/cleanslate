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
    path('actividadpp/<int:id>', views.getActividadPorPuesto),
    path('setactividad/', views.setActividad),
    path('setactividad/<int:id>', views.patchActividad),

    # Resumen por puesto
    path('resporpuesto/<int:id_estruc>', views.mostrar_resumen_por_puesto),

    # Tablero sunburst
    path('tablero/<int:id_obj>/<date_Until_text>', views.armar_tablero),

    # ODS
    path('ods/', views.getOds),
    path('ods/<int:id>', views.getOds),

    # EJE
    path('eje/', views.getEje),
    path('eje/<int:id>', views.getEje),

    # Finalidad y Función
    path('fyf/', views.getFinalidadyFuncion),
    path('fyf/<int:id>', views.getFinalidadyFuncion),

    # Política Pública
    path('pp/', views.getPoliticaPublica),
    path('pp/<int:id>', views.getPoliticaPublica),

    # Tipo Actividad
    path('tact/', views.getTipoActividad),
    path('tact/<int:id>', views.getTipoActividad),

    # Beneficiarios (tabla Actibidades)
    path('benef/', views.getBenef),
    path('benef/<int:id>', views.getBenef),
    path('setbenef/', views.setBenef),

    # Indicador
    path('indicador/', views.getIndicador),
    path('indicador/<int:id>', views.getIndicador),

    # Parametro
    path('parametro/', views.getParametro),
    path('parametro/<int:id>', views.getParametro),

    # Tipo Función
    path('tipofuncion/', views.getTipoFuncion),
    path('tipofuncion/<int:id>', views.getTipoFuncion),

    # Tipo Indicador
    path('tipoindicador/', views.getTipoIndicador),
    path('tipoindicador/<int:id>', views.getTipoIndicador),
]
