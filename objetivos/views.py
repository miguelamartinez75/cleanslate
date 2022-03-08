from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Estructura, Objetivo
from .serializers import EstructuraSerializer, ObjetivoSerializer


@api_view(["GET"])
def getEstructura(request, id=None):
    if id:
        item = Estructura.objects.get(id=id)
        serializer = EstructuraSerializer(item)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    miembros = Estructura.objects.all()
    serializer = EstructuraSerializer(miembros, many=True)
    return Response(serializer.data)


@api_view(['PUT'])
def setEstructura(request):
    serializer = EstructuraSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
    else:
        return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PATCH'])
def patchEstructura(request, id=None):
    item = Estructura.objects.get(id=id)
    serializer = EstructuraSerializer(item, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({"status": "success", "data": serializer.data})
    else:
        return Response({"status": "error", "data": serializer.errors})

@api_view(['DELETE'])
def delEstructura(request, id=None):
    item = get_object_or_404(Estructura, id=id)
    item.delete()
    return Response({"status": "success", "data": "Item Deleted"})


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