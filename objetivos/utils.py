from .models import Indicador, Tipofuncion, Data, Parametro, Objetivo, Actividad

import numexpr


# localhost/objetivos/tablero/1/30-04-2021
def calcular(indic, date_Until):
    # Calcula el valor del indicador a la ultima fecha disponible anterior a date_Until

    if 1 == 1:
        # try:
        indicador = Indicador.objects.get(id=indic)
        tipofuncion = Tipofuncion.objects.get(id=indicador.tipofuncion_id)
        parametro = Parametro.objects.filter(vigencia__lte=date_Until, indicador_id=indicador.id).last()
        # parametro = Parametro.objects.filter(indicador_id=indicador.id).last()
        data = Data.objects.filter(datetime__lte=date_Until, indicador_id=indicador.id).last()
        # data = Data.objects.filter(indicador_id=indicador.id).last()
        if data and parametro:
            x = data.value
            a = parametro.parama
            b = parametro.paramb
            c = parametro.paramc
            mifuncion = tipofuncion.func
            # salida = eval(mifuncion)
            salida = numexpr.evaluate(mifuncion).item()
            salida = max(0, min(1, salida))
            print(indicador.name, mifuncion, " a: ", parametro.parama, " b: ", parametro.paramb, " dato: ", x, " = ",
                  salida)
        else:
            salida = None
            print(indicador.name, " no tiene datos o parametros")
        return salida
    # except:
    #    return None


def calcular_objetivo(id_obj, peso_relativo, date_Until, matrix):
    matrix_objetivos = matrix

    # Primero verificar si tiene indicador asociado
    objetivo = Objetivo.objects.get(pk=id_obj)
    if objetivo.id_indicador:
        # print(objetivo.id_indicador)
        co = calcular(objetivo.id_indicador.id, date_Until)
        # print(co)
        if co == None:
            color = "#D4D4D4"
        else:
            if co >= 0.75:
                color = "#00FF00"
            else:
                if co >= 0.5:
                    color = "#FFFF00"
                else:
                    if co >= 0.25:
                        color = "#FF8800"
                    else:
                        color = "#FF0000"
        elem = [objetivo.codigo, objetivo.parent.codigo, peso_relativo, color, co]
    else:
        # Averiguar los hijos de objetivo
        hijos = objetivo.get_children()
        # print("%s tiene %s hijos" %(objetivo.codigo, len(hijos)))
        if hijos:

            # Calcular el total de pesos de los hijos
            suma_pesos = 0
            for hijo in hijos:
                suma_pesos = suma_pesos + hijo.prefer

            # prefer_acum = 0
            valor_acum = 0
            pesos_nulos = 0
            for hijo in hijos:
                peso_hijo = peso_relativo * hijo.prefer / suma_pesos
                Item = calcular_objetivo(hijo.id, peso_hijo, date_Until, matrix_objetivos)
                if Item[-1][4] != None:
                    # prefer_acum = prefer_acum + hijo.prefer
                    valor_acum = valor_acum + Item[-1][4] * hijo.prefer / suma_pesos
                else:
                    pesos_nulos = pesos_nulos + hijo.prefer

            try:
                if pesos_nulos > 0:
                    valor = valor_acum * suma_pesos / (suma_pesos - pesos_nulos)
                else:
                    valor = valor_acum  # / prefer_acum
                    # print(objetivo.codigo, valor)
            except:
                valor = None

            if valor == None:
                color = "#D4D4D4"
            else:
                if valor >= 0.75:
                    color = "#00FF00"
                else:
                    if valor >= 0.5:
                        color = "#FFFF00"
                    else:
                        if valor >= 0.25:
                            color = "#FF8800"
                        else:
                            color = "#FF0000"

            # Si no tiene padre (en el caso de raiz) dejar una cadena vacia
            if objetivo.parent:
                padre = objetivo.parent.codigo
                # elem = [objetivo.codigo, padre, objetivo.prefer, color, valor]
                # matrix_objetivos.append(elem)
            else:
                padre = "Raiz"
                # elem = [objetivo.codigo, padre, objetivo.prefer, color, valor]
                # matrix_objetivos.append(elem)

            elem = [objetivo.codigo, padre, 0, color, valor]


        else:
            # El objetivo no tiene ni indicador ni hijos .. Dejar en gris
            elem = [objetivo.codigo, objetivo.parent.codigo, peso_relativo, "#D4D4D4", None]

    matrix_objetivos.append(elem)

    return matrix_objetivos


def ajustar_cadena(texto):
    # Definir la cantidad de renglones a partir de la longitud de la cadena. Probando con 30 - 72 - 126 - 200
    if len(texto) <= 25:
        texto_ajustado = texto
    elif len(texto) <= 62:

        primer_corte = int(len(texto) / 2)
        texto_ajustado = cortar_texto(texto, primer_corte, int(primer_corte * 1.5))

        ##Si el texto es mayor a 30 pero menos a 72, buscar un espacio próximo al centro y reemplazar por <br>
        # inicio = int(len(texto)/3)
        # medio = int(len(texto)/2)
        # if " " in texto[inicio: inicio * 2]:
        #    texto_ajustado = texto[0: inicio] + texto[inicio: inicio * 2].replace(" ", "<br>", 1) + texto[inicio * 2:]
        # else:
        #    texto_ajustado = texto[0:medio] + "<br>" + texto[medio:]

    elif len(texto) <= 117:
        primer_corte = int(len(texto) / 3)
        texto_ajustado = cortar_texto(texto, primer_corte, primer_corte)
        segundo_corte = primer_corte * 2
        texto_ajustado = cortar_texto(texto_ajustado, segundo_corte, primer_corte)

    else:
        texto_ajustado = texto
    return texto_ajustado


def cortar_texto(texto, ubicacion, rango):
    # Primero buscar un espacio próximo al punto central del corte.
    # print(texto[ubicacion - int(rango/2):ubicacion + int(rango/2)])

    if " " in texto[ubicacion - int(rango / 6):ubicacion + int(rango / 6)]:
        texto_cortado = texto[0: ubicacion - int(rango / 6)] + texto[ubicacion - int(rango / 6): ubicacion + int(
            rango / 6)].replace(" ", "<br>", 1) + texto[ubicacion + int(rango / 6):]
    elif " " in texto[ubicacion - int(rango / 4):ubicacion + int(rango / 4)]:
        texto_cortado = texto[0: ubicacion - int(rango / 4)] + texto[ubicacion - int(rango / 4): ubicacion + int(
            rango / 4)].replace(" ", "<br>", 1) + texto[ubicacion + int(rango / 4):]
    elif " " in texto[ubicacion - int(rango / 2):ubicacion + int(rango / 2)]:
        texto_cortado = texto[0: ubicacion - int(rango / 2)] + texto[ubicacion - int(rango / 2): ubicacion + int(
            rango / 2)].replace(" ", "<br>", 1) + texto[ubicacion + int(rango / 2):]
    else:
        texto_cortado = texto[0:ubicacion] + "<br>" + texto[ubicacion:]

    return texto_cortado


def calc(indic, value):
    indicador = Indicador.objects.get(pk=indic)
    tipofuncion = Tipofuncion.objects.get(pk=indicador.tipofuncion_id)
    parametro = Parametro.objects.filter(indicador_id=indicador.id).last()
    x = value
    a = parametro.parama
    b = parametro.paramb
    c = parametro.paramc
    mifuncion = tipofuncion.func
    # salida = eval(mifuncion)
    salida = numexpr.evaluate(mifuncion).item()
    return salida


def calcular_oai(id_obj, peso_relativo, date_Until, matrix):
    matrix_objetivos = matrix

    # Primero verificar si tiene actividad asociada
    objetivo = Objetivo.objects.get(pk=id_obj)
    if objetivo.id_actividad:
        # El objetivo tiene una actividad asociada. Hay que buscar los indicadores de dicha actividad
        indicadores = Indicador.objects.filter(id_actividad=objetivo.id_actividad)

        if (len(indicadores) > 0):
            # Para cada indicador crear un registro
            co_activ = None
            peso_acum = 0
            for indicador in indicadores:
                peso_acum = peso_acum + indicador.peso

            for indicador in indicadores:
                # El objetivo tiene una actividad asociada
                co = calcular(indicador.id, date_Until)
                # print(co)
                if co == None:
                    color = "#D4D4D4"
                else:
                    if co >= 0.75:
                        color = "#00FF00"
                    else:
                        if co >= 0.5:
                            color = "#FFFF00"
                        else:
                            if co >= 0.25:
                                color = "#FF8800"
                            else:
                                color = "#FF0000"
                elem = [indicador.name, objetivo.codigo, peso_relativo * indicador.peso / peso_acum, color, co]
                matrix_objetivos.append(elem)

                # Calcular indicador promedio para la actividad
                if co != None:
                    if co_activ == None:
                        co_activ = co * indicador.peso / peso_acum
                    else:
                        co_activ = co_activ + co * indicador.peso / peso_acum

            if co_activ == None:
                color = "#D4D4D4"
            else:
                if co_activ >= 0.75:
                    color = "#00FF00"
                else:
                    if co_activ >= 0.5:
                        color = "#FFFF00"
                    else:
                        if co_activ >= 0.25:
                            color = "#FF8800"
                        else:
                            color = "#FF0000"
                            # Agregar el registro de la actividad. El peso relativo es cero porque suma el peso de sus hijos
            elem = [objetivo.codigo, objetivo.parent.codigo, 0, color, co_activ]
    else:
        # Averiguar los hijos de objetivo
        hijos = objetivo.get_children()
        # print("%s tiene %s hijos" %(objetivo.codigo, len(hijos)))
        if hijos:

            # Calcular el total de pesos de los hijos
            suma_pesos = 0
            for hijo in hijos:
                suma_pesos = suma_pesos + hijo.prefer

            # prefer_acum = 0
            valor_acum = 0
            pesos_nulos = 0
            for hijo in hijos:
                peso_hijo = peso_relativo * hijo.prefer / suma_pesos
                Item = calcular_oai(hijo.id, peso_hijo, date_Until, matrix_objetivos)
                if Item[-1][4] != None:
                    # prefer_acum = prefer_acum + hijo.prefer
                    valor_acum = valor_acum + Item[-1][4] * hijo.prefer / suma_pesos
                else:
                    pesos_nulos = pesos_nulos + hijo.prefer

            try:
                if pesos_nulos > 0:
                    valor = valor_acum * suma_pesos / (suma_pesos - pesos_nulos)
                else:
                    valor = valor_acum  # / prefer_acum
                    # print(objetivo.codigo, valor)
            except:
                valor = None

            if valor == None:
                color = "#D4D4D4"
            else:
                if valor >= 0.75:
                    color = "#00FF00"
                else:
                    if valor >= 0.5:
                        color = "#FFFF00"
                    else:
                        if valor >= 0.25:
                            color = "#FF8800"
                        else:
                            color = "#FF0000"

            # Si no tiene padre (en el caso de raiz) dejar una cadena vacia
            if objetivo.parent:
                padre = objetivo.parent.codigo
                # elem = [objetivo.codigo, padre, objetivo.prefer, color, valor]
                # matrix_objetivos.append(elem)
            else:
                padre = "Raiz"
                # elem = [objetivo.codigo, padre, objetivo.prefer, color, valor]
                # matrix_objetivos.append(elem)

            elem = [objetivo.codigo, padre, 0, color, valor]


        else:
            # El objetivo no tiene ni indicador ni hijos .. Dejar en gris
            elem = [objetivo.codigo, objetivo.parent.codigo, peso_relativo, "#D4D4D4", None]

    matrix_objetivos.append(elem)

    return matrix_objetivos


