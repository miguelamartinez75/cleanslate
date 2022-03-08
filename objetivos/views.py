from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Estructura, Objetivo
from .serializers import EstructuraSerializer, ObjetivoSerializer


@api_view(["GET"])
def getEstructura(request):
    miembros = Estructura.objects.all()
    serializer = EstructuraSerializer(miembros, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def setEstructura(request):
    serializer = EstructuraSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
    else:
        return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def getHijosDe(request):
    hijos = Estructura.get_descendants_for(True, 5, True)
    serializer = EstructuraSerializer(hijos, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getObjetivo(request):
    objetivos = Objetivo.objects.all()
    serializer = ObjetivoSerializer(objetivos, many=True)
    return Response(serializer.data)