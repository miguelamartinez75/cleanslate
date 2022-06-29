from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Estructura, Objetivo, Actividad, ods, eje, finalidad_y_funcion, politica_publica, Tipo_Actividad, Beneficiario, Indicador, Parametro, Tipofuncion, Tipo_Indicador


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


class OdsSerializer(ModelSerializer):
    class Meta:
        model = ods
        fields = ['id', 'name']


class EjeSerializer(ModelSerializer):
    class Meta:
        model = eje
        fields = ['id', 'name']


class FinalidadyFuncionSerializer(ModelSerializer):
    class Meta:
        model = finalidad_y_funcion
        fields = ['id', 'name']


class PoliticaPublicaSerializer(ModelSerializer):
    class Meta:
        model = politica_publica
        fields = ['id', 'name']


class TipoActividadSerializer(ModelSerializer):
    class Meta:
        model = Tipo_Actividad
        fields = ['id', 'descripcion']


class BeneficiarioSerializer(ModelSerializer):
    class Meta:
        model = Beneficiario
        fields = ['id', 'name']
        # many = True

    # def create(self, validated_data):
    #     beneficiarios = validated_data.pop('beneficiario', [])
    #     instance = super().create(validated_data)
    #     for l in beneficiarios:
    #         instance.links.create(beneficiario=l)


class IndicadorSerializer(ModelSerializer):
    class Meta:
        model = Indicador
        fields = '__all__'


class ParametroSerializer(ModelSerializer):
    class Meta:
        model = Parametro
        fields = '__all__'


class TipofuncionSerializaer(ModelSerializer):
    class Meta:
        model = Tipofuncion
        fields = '__all__'


class TipoIndicadorSerializer(ModelSerializer):
    class Meta:
        model = Tipo_Indicador
        fields = '__all__'
