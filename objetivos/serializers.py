from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Estructura, Objetivo, Actividad


class EstructuraSerializer(ModelSerializer):
    name = serializers.CharField(max_length=200)
    letra = serializers.CharField(max_length=20, required=False, allow_blank=True)
    mission = serializers.CharField(required=False, allow_blank=True)
    function = serializers.CharField(required=False, allow_blank=True)
    decreto = serializers.CharField(max_length=50, required=False, allow_blank=True)
    marco_legal = serializers.CharField(required=False, allow_blank=True)
    diagnostico = serializers.CharField(required=False, allow_blank=True)
    procesos_participativos = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        model = Estructura
        fields = ('__all__')
        #fields = ['id', 'name', 'letra', 'mission', 'function', 'decreto', 'marco_legal', 'diagnostico', 'procesos_participativos', 'parent']


class EstructuraItemSerializer(ModelSerializer):
    class Meta:
        model = Estructura
        fields = ('__all__')


class EstructuraItemNameSerializer(ModelSerializer):
    class Meta:
        model = Estructura
        fields = ['name']


class ObjetivoSerializer(ModelSerializer):
    class Meta:
        model = Objetivo
        fields = ('__all__')


class ActividadSerializer(ModelSerializer):
    class Meta:
        model = Actividad
        fields = ('__all__')

