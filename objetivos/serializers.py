from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Estructura, Objetivo


class EstructuraSerializer(ModelSerializer):
    name = serializers.CharField(max_length=200)
    letra = serializers.CharField(max_length=20, required=False)
    mission = serializers.CharField(required=False)
    function = serializers.CharField(required=False)
    decreto = serializers.CharField(max_length=50, required=False)
    marco_legal = serializers.CharField(required=False)
    diagnostico = serializers.CharField(required=False)
    procesos_participativos = serializers.CharField(required=False)

    class Meta:
        model = Estructura
        fields = ('__all__')
        #fields = ['id', 'name', 'letra', 'mission', 'function', 'decreto', 'marco_legal', 'diagnostico', 'procesos_participativos', 'parent']


class ObjetivoSerializer(ModelSerializer):
    class Meta:
        model = Objetivo
        fields = ('__all__')

