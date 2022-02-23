from rest_framework.serializers import ModelSerializer
from .models import Estructura


class EstructuraSerializer(ModelSerializer):
    class Meta:
        model = Estructura
        fields = ['id', 'name', 'letra', 'mission', 'function', 'decreto', 'marco_legal', 'diagnostico', 'procesos_participativos', 'parent']
