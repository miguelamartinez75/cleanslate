from rest_framework.response import Response
from rest_framework.decorators import api_view
# from rest_framework.views import APIView
from datetime import date, datetime, timedelta
from rest_framework import status
from django.shortcuts import get_object_or_404
from json import JSONEncoder
import numpy as np
from .models import Estructura, Objetivo, Actividad
from .serializers import EstructuraSerializer, EstructuraItemSerializer, EstructuraItemNameSerializer, ObjetivoSerializer, ActividadSerializer
from .utils import calcular_objetivo, calcular_oai, ajustar_cadena

# Render es necesario solo para la vista por puesto
from django.shortcuts import render
from django.http import HttpResponse
import json

#import plotly.graph_objects as go


class NumpyArrayEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return JSONEncoder.default(self, obj)


# Estructura
@api_view(["GET"])
def getEstructura(request, id=None):
    if id:
        hijos = Estructura.objects.get(pk=id).get_descendants(include_self=True)
        serializer = EstructuraSerializer(hijos, many=True)
        return Response(serializer.data)

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
    item = Estructura.objects.get(pk=id)
    serializer = EstructuraSerializer(item, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({"status": "success", "data": serializer.data})
    else:
        return Response({"status": "error", "data": serializer.errors})


@api_view(['DELETE'])
def delEstructura(request, id=None):
    item = get_object_or_404(Estructura, pk=id)
    item.delete()
    return Response({"status": "success", "data": "Item Deleted"})


@api_view(['GET'])
def getEstructuraItem(request, id):
    item = Estructura.objects.get(pk=id)
    serializer = EstructuraItemSerializer(item)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def getEstructuraItemName(request, id):
    item = Estructura.objects.get(pk=id)
    serializer = EstructuraItemNameSerializer(item)
    return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)


# Objetivos
@api_view(['GET'])
def getObjetivo(request, id=None):
    if id:
        item = Objetivo.objects.get(pk=id)
        serializer = ObjetivoSerializer(item)
        return Response(serializer.data)

    objetivos = Objetivo.objects.all()
    serializer = ObjetivoSerializer(objetivos, many=True)
    return Response(serializer.data)


@api_view(['PUT'])
def setObjetivo(request):
    serializer = ObjetivoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
    else:
        return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PATCH'])
def patchObjetivo(request, id=None):
    item = Objetivo.objects.get(pk=id)
    serializer = ObjetivoSerializer(item, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({"status": "success", "data": serializer.data})
    else:
        return Response({"status": "error", "data": serializer.errors})


@api_view(['DELETE'])
def delObjetivo(request, id=None):
    item = get_object_or_404(Objetivo, pk=id)
    item.delete()
    return Response({"status": "success", "data": "Item Deleted"})


# Actividades
@api_view(['GET'])
def getActividad(request, id=None):
    if id:
        item = Actividad.objects.get(pk=id)
        serializer = ActividadSerializer(item)
        return Response(serializer.data)

    actividades = Actividad.objects.all()
    serializer = ActividadSerializer(actividades, many=True)
    return Response(serializer.data)

# Tablero, datos para el sunburst
@api_view(['GET'])
def armar_tablero(request, id_obj, date_Until_text):
    # Rojo = "#FF0000"
    # Naranja = "#FF8800"
    # Amarillo = "#FFFF00"
    # Verde = "#00FF00"
    # Gris = "#D4D4D4"

    matrix_objetivos = []
    date_Until = datetime.strptime(date_Until_text, '%d-%m-%Y')
    matrix_resultados = calcular_oai(id_obj, 100, date_Until, matrix_objetivos)

    matrix_transversa = np.array(matrix_resultados).T
    marcadores = dict(colors=matrix_transversa[3])

    labels = []  # matrix_transversa[0].copy()
    valores = matrix_transversa[4].copy()

    for i in range(0, len(valores)):
        if valores[i] is None:
            labels.append(f"{matrix_transversa[0][i]} <br> <b>Sin datos</b>")
        else:
            labels.append(f"{matrix_transversa[0][i]} <br> <b>{int(round(float(valores[i]) * 100, 0))}</b>")

    ids = matrix_transversa[0]
    parents = matrix_transversa[1]
    values = matrix_transversa[2]

    return Response({"data": [
        {"ids": ids, "labels": labels, "parents": parents, "values": values, "type": "sunburst", "maxdepth": 3,
         "marker": marcadores}]})


# Esta vista la traje del proyecto viejo solo para poder ver los datos. Hay que serializarlos
def mostrar_resumen_por_puesto(request, id_estruc):
    estructura = Estructura.objects.get(pk=id_estruc)
    objetivos = Objetivo.objects.filter(id_estructura=id_estruc).exclude(parent__id_estructura=id_estruc)
    dependientes = Estructura.objects.filter(parent=id_estruc)
    #temas = Tema_Estrategico.objects.filter(id_estructura=id_estruc)
    objetivos_estrategicos = Objetivo.objects.filter(id_estructura=id_estruc).filter(es_tema_estrategico=True)
    activ = Actividad.objects.filter(id_Estructura=id_estruc)
    # Faltaría buscar los indicadores de esas actividades, para poder mostrarlos en el template
    contexto = {"estructura":estructura, "dep":dependientes, "te":objetivos_estrategicos, "act":activ, "obj":objetivos}
    return render(request, "tablero/plantilla_resumen_por_puesto.html", contexto )

def armar_tablero_oai(request, id_obj, date_until_text, delta_fechas):
    #Rojo = "#FF0000"
    #Naranja = "#FF8800"
    #Amarillo = "#FFFF00"
    #Verde = "#00FF00"
    #Gris = "#D4D4D4"
    print(" ----- Primer diagrama Objetivo - Actividad - Indicador ----- ")

    # Calcular valores a mostrar
    matrix_objetivos=[]
    date_until = datetime.strptime(date_until_text, '%d-%m-%Y')
    matrix_resultados = calcular_oai(id_obj, 100, date_until, matrix_objetivos)
    
    #Transponer array de valores para adecuarlos a la estructura del sunburst
    matrix_transversa = np.array(matrix_resultados).T
    marcadores=dict(colors=matrix_transversa[3])
    
    etiquetas = [] #matrix_transversa[0].copy()
    valores = matrix_transversa[4].copy()
    
    #Ajustar etiquetas para multiples renglones, facilitando lectura
    for i in range(0, len(valores)):
        #print(i)
        if valores[i] == None:
            etiquetas.append(f"{ajustar_cadena(matrix_transversa[0][i])} <br> <b>Sin datos</b>") 
            #print(etiquetas[i])
        else:
            etiquetas.append(f"{ajustar_cadena(matrix_transversa[0][i])} <br> <b>{int(round(float(valores[i])*100, 0))}</b>")
            #print(etiquetas[i])

    #Crear el diagrama 
    ids = matrix_transversa[0],
    labels = etiquetas, # + " " + str(matrix_transversa[4]),
    parents = matrix_transversa[1],
    values = matrix_transversa[2],

       
    #fig = go.Figure(go.Sunburst(

    """ ids = matrix_transversa[0],
        labels = etiquetas, # + " " + str(matrix_transversa[4]),
        parents = matrix_transversa[1],
        values = matrix_transversa[2], """
        #maxdepth = 4,
        #domain=dict(column=0),
        #branchvalues = 'total',
        #branchvalues = "remainder",
        #marker=marcadores,
        #hovertemplate='%{label} <br> %{percentEntry:0%}'
        #), 
        #layout=go.layout(title=go.layout.title(text="Titulo"))
    #)
    
    # El siguiente render requiere Plotly instalado
    # return render(request, "plantilla_diagrama.html", {"imagen":fig.to_html(default_height=700, default_width=700)} )  #default_height=900, default_width=1800

    #return JsonResponse({"ids": ids, "labels": labels, "parents": parents, "values": values, "type": "sunburst", "maxdepth": 3, "marker": marcadores})
    return HttpResponse(json.dumps({"ids": ids, "labels": labels, "parents": parents, "values": values, "type": "sunburst", "maxdepth": 3, "marker": marcadores}), content_type = "application/json")