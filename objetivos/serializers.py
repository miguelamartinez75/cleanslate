from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Estructura, Objetivo


class EstructuraSerializer(ModelSerializer):
    class Meta:
        model = Estructura
        fields = ('__all__')
        #fields = ['id', 'name', 'letra', 'mission', 'function', 'decreto', 'marco_legal', 'diagnostico', 'procesos_participativos', 'parent']


class ObjetivoSerializer(ModelSerializer):
    class Meta:
        model = Objetivo
        fields = ('__all__')

