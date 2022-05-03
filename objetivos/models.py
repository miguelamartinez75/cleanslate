from django.contrib.auth.models import User
from django.db import models
from mptt.models import MPTTModel
from treewidget.fields import TreeForeignKey


class Objetivo(MPTTModel):
    nombre = models.CharField(max_length=50, null=True)
    descripcion = models.CharField(max_length=500)
    descripcion_alternativa = models.CharField(max_length=500, null=True, blank=True)
    id_estructura = models.ForeignKey('Estructura', on_delete=models.CASCADE, null=True, blank=True)
    createdAt = models.DateTimeField()
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    es_tema_estrategico = models.BooleanField(default=False)
    situacion_actual = models.TextField(max_length=2000, null=True, blank=True)
    situacion_deseada = models.TextField(max_length=2000, null=True, blank=True)
    id_actividad = models.ForeignKey('Actividad', on_delete=models.CASCADE, null=True, blank=True)
    prefer = models.FloatField(default=1)

    class MPTTMeta:
        order_insertion_by = ['nombre']

    def __str__(self):
        return self.nombre


class ods(MPTTModel):
    name = models.CharField(max_length=200)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name


class eje(MPTTModel):
    name = models.CharField(max_length=200)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name


class finalidad_y_funcion(MPTTModel):
    name = models.CharField(max_length=200)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name


class politica_publica(MPTTModel):
    name = models.CharField(max_length=200)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name


# class Tema_Estrategico(models.Model):
#     name = models.CharField(max_length=50)
#     situacion_actual = models.TextField(max_length=2000, null=True, blank=True)
#     situacion_deseada = models.TextField(max_length=2000, null=True, blank=True)
#     id_estructura = models.ForeignKey('Estructura', on_delete=models.CASCADE, null=True, blank=True)
#
#     def __str__(self):
#         return self.name


class Tipo_Actividad(models.Model):
    descripcion = models.CharField(max_length=50)

    def __str__(self):
        return self.descripcion


class Actividad(models.Model):
    name = models.CharField(max_length=50, null=True)
    Id_Tipo_Actividad = models.ForeignKey(Tipo_Actividad, on_delete=models.CASCADE, null=True, blank=True)
    id_Estructura = models.ForeignKey('Estructura', on_delete=models.CASCADE, null=True, blank=True)
    id_Objetivo = models.ForeignKey('Objetivo', on_delete=models.CASCADE, null=True, blank=True)
    producto = models.CharField(max_length=500, null=True, blank=True)
    resultado = models.CharField(max_length=500, null=True, blank=True)
    id_ods = models.ForeignKey('ods', on_delete=models.CASCADE, null=True, blank=True)
    id_eje = models.ForeignKey('eje', on_delete=models.CASCADE, null=True, blank=True)
    id_finalidadyfuncion = models.ForeignKey('finalidad_y_funcion', on_delete=models.CASCADE, null=True, blank=True)
    id_politicapublica = models.ForeignKey('politica_publica', on_delete=models.CASCADE, null=True, blank=True)
    beneficiario = models.ManyToManyField('Beneficiario', blank=True)
    # Nuevos campos
    problema = models.CharField(max_length=500, null=True, blank=True)
    productos_secundarios = models.CharField(max_length=500, null=True, blank=True)
    ref_presupuesto = models.CharField(max_length=50, null=True)
    duracion = models.IntegerField()
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Beneficiario(models.Model):
    name = models.CharField(max_length=100)
    createdAt = models.DateTimeField()

    def __str__(self):
        return self.name

# class IndicadorxActividad(models.Model):
#    id_indicador = models.ForeignKey('Indicador', on_delete=models.CASCADE, null=True, blank=True)
#    id_actividad = models.ForeignKey('Actividad', on_delete=models.CASCADE, null=True, blank=True)
#    peso = models.FloatField()
#    def __str__(self):
#        return self.id_actividad.name + " - " + self.id_indicador.name


# class Objetivos_Requeridos(models.Model):
# Objetivo_Precedente = models.ForeignKey('Objetivo', on_delete=models.CASCADE, null=True, blank=True, related_name='Precedente')
# Objetivo_Siguiente = models.ForeignKey('Objetivo', on_delete=models.CASCADE, null=True, blank=True, related_name='Siguiente')


class TipoAccion(models.Model):
    nombre = models.CharField(max_length=50, null=True)
    descripcion = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.nombre


class PrioridadAccion(models.Model):
    nombre = models.CharField(max_length=50, null=True)
    descripcion = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.nombre


class EstadoAccion(models.Model):
    nombre = models.CharField(max_length=50, null=True)
    descripcion = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.nombre


class Accion(models.Model):
    descripcion = models.CharField(max_length=200)
    id_TipoAccion = models.ForeignKey('TipoAccion', on_delete=models.CASCADE, null=True, blank=True)
    id_PrioridadAccion = models.ForeignKey('PrioridadAccion', on_delete=models.CASCADE, null=True, blank=True)
    id_EstadoAccion = models.ForeignKey('EstadoAccion', on_delete=models.CASCADE, null=True, blank=True)
    id_user = models.CharField(max_length=50)  # Debería linquearse al usuario de la aplicación
    fecha_inicio = models.DateField()
    duracion = models.IntegerField()
    avance = models.FloatField()
    observacion = models.CharField(max_length=500)

    def __str__(self):
        return self.descripcion


class Insumo(models.Model):
    nombre = models.CharField(max_length=50, null=True)
    descripcion = models.CharField(max_length=250, blank=True)
    Inciso = models.CharField(max_length=20)
    cantidad = models.FloatField()
    importe = models.DecimalField(decimal_places=2, max_digits=4)


class Estructura(MPTTModel):
    name = models.CharField(max_length=200)
    letra = models.CharField(max_length=20, null=True)
    mission = models.TextField(null=True)
    function = models.TextField(null=True)
    decreto = models.CharField(max_length=50, null=True)
    marco_legal = models.TextField(null=True)
    diagnostico = models.TextField(null=True)
    procesos_participativos = models.TextField(null=True)
    # objetivos = models.ManyToManyField('Objetivo', blank=True)
    # Habría que agregar campos para subir archivos adjuntos
    # documento_myf = models.FileField

    parent = models.ForeignKey('self', on_delete=models.CASCADE,
                               null=True, blank=True, related_name='children')

    def __str__(self):
        if self.letra == "":
            return self.name + " id(" + str(self.id) + ")"
        else:
            return self.letra + " - " + self.name + " id(" + str(self.id) + ")"

    # def get_descendants_for(self, idx, include_self):
    #     return set(self.nodes[idx].get_descendants(include_self=include_self))

    class MPTTMeta:
        order_insertion_by = ['name']


class Preferencia(models.Model):
    name = models.CharField(max_length=100)
    objetivo = models.ForeignKey(Objetivo, on_delete=models.CASCADE)
    parent = models.ForeignKey(Estructura, on_delete=models.CASCADE)
    amount = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Tipofuncion(models.Model):
    name = models.CharField(max_length=50)
    func = models.CharField(max_length=255)

    def __str__(self):
        return self.name + f" ({self.func})"

    class Meta:
        ordering = ['name']


class Tipo_Indicador(models.Model):
    nombre = models.CharField(max_length=50, null=True)
    descripcion = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.nombre


class Indicador(models.Model):
    name = models.CharField(max_length=100)
    id_Tipo_Indicador = models.ForeignKey(Tipo_Indicador, on_delete=models.CASCADE, blank=True, null=True)
    tipofuncion = models.ForeignKey(Tipofuncion, on_delete=models.CASCADE, blank=True, null=True)
    id_actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE, blank=True, null=True)
    peso = models.FloatField(default=1)
    # Nuevos campos
    definicion = models.CharField(max_length=500, blank=True)
    modo_calculo = models.TextField(max_length=1000, blank=True)
    unidades_medida = models.CharField(max_length=50)
    fuente = models.CharField(max_length=500, blank=True)
    periodicidad = models.IntegerField()  # Dias cada cuanto se publica
    desagregaciones = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return "%s %s" % (self.pk, self.name)

    class Meta:
        ordering = ['name']


class Parametro(models.Model):
    indicador = models.ForeignKey(Indicador, on_delete=models.CASCADE, blank=True, null=True)
    parama = models.FloatField(null=True, blank=True)
    paramb = models.FloatField(null=True, blank=True)
    paramc = models.FloatField(null=True, blank=True)
    paramd = models.FloatField(null=True, blank=True)
    vigencia = models.DateTimeField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='param_creator')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']
        # ordering = ('-created',)

    def __str__(self):
        return "%s %s" % (self.indicador.name, self.vigencia)


class Data(models.Model):
    datetime = models.DateTimeField()
    detail = models.CharField(max_length=250, null=True, blank=True)
    value = models.FloatField(null=True, blank=True)
    indicador = models.ForeignKey(Indicador, on_delete=models.CASCADE, blank=True, null=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='data_creator')

    def __str__(self):
        return self.indicador.name + " - " + str(self.datetime)


# Modelos nuevos
class PresupuestoPorActividad(models.Model):
    id_actividad = models.ForeignKey('actividad', on_delete=models.CASCADE, null=True, blank=True)
    presupuesto = models.FloatField()
    avance_estimado = models.FloatField()
    ejecicio = models.CharField(max_length=50, null=True, blank=True)