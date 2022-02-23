from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin

from .models import Tema_Estrategico, Accion, Actividad, Objetivo, Data, Estructura, Preferencia, Tipo_Actividad, \
    Tipo_Indicador, Tipofuncion, Indicador, Parametro, finalidad_y_funcion, ods, politica_publica

# admin.site.register(Preferencia)
admin.site.register(Tipofuncion)
admin.site.register(Indicador)
admin.site.register(Parametro)
admin.site.register(Actividad)
admin.site.register(Accion)
admin.site.register(Tipo_Indicador)
admin.site.register(Tipo_Actividad)
admin.site.register(Tema_Estrategico)


# admin.site.register(IndicadorxActividad)

@admin.register(Data)
class DataAdmin(admin.ModelAdmin):
    list_display = ['indicador', 'creator', 'value', 'datetime']
    date_hierarchy = 'datetime'
    # list_editable = ['value', 'datetime']


admin.site.register(
    Objetivo,
    DraggableMPTTAdmin,
    list_display=(
        'tree_actions',
        'indented_title',

    ),
    list_display_links=(
        'indented_title',
    ),
)

admin.site.register(
    Estructura,
    DraggableMPTTAdmin,
    list_display=(
        'tree_actions',
        'indented_title',
        # ...more fields if you feel like it...
    ),
    list_display_links=(
        'indented_title',
    ),
)

admin.site.register(
    ods,
    DraggableMPTTAdmin,
    list_display=(
        'tree_actions',
        'indented_title',
        # ...more fields if you feel like it...
    ),
    list_display_links=(
        'indented_title',
    ),
)

admin.site.register(
    finalidad_y_funcion,
    DraggableMPTTAdmin,
    list_display=(
        'tree_actions',
        'indented_title',
        # ...more fields if you feel like it...
    ),
    list_display_links=(
        'indented_title',
    ),
)

admin.site.register(
    politica_publica,
    DraggableMPTTAdmin,
    list_display=(
        'tree_actions',
        'indented_title',
        # ...more fields if you feel like it...
    ),
    list_display_links=(
        'indented_title',
    ),
)

