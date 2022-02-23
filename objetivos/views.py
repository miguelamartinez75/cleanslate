from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Estructura
from .serializers import EstructuraSerializer


@api_view(["GET"])
def getEstructura(request):
    miembros = Estructura.objects.all()
    serializer = EstructuraSerializer(miembros, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getHijosDe(request):
    hijos = Estructura.get_descendants_for(True, 5, True)
    serializer = EstructuraSerializer(hijos, many=True)
    return Response(serializer.data)