# -*- coding: utf-8 -*-
#from __future__ import unicode_literals

import collections

# funcion para leer archivo
def leer_archivo(nombre = "guion.txt"):
    with open(nombre, "r") as a:
        return a.read()
#variable en donde se almacena el archivo
#guion = leer_archivo()

#funcion para eliminar cualquier caracter que no sea letra ni numero
def filtrar_texto(s):
    str1 = ''
    for i in range(len(s)):
        j = ord(s[i])
        if j==32 or (48<=j and j<=57) or (65<=j and j<=90) or (97<=j and j<=122):
            str1 += s[i]
    return str1

#funcion que genera una lista con los personajes que aparecen en el guion 
def personajes_principales(guion):
    parrafo = guion.split('\n')
    personajes = []
    per = []
    for i in range(len(parrafo)):
        palabra = parrafo[i].split(':')
        for j in range(len(palabra)):
            for k in range(len(palabra[j])):
                letra = ord(palabra[j][0])
                if letra == 45:
                    per.append(palabra[j])
    cuenta1 = collections.Counter(per) #elimina elemntos repetidos
    personajes = cuenta1.keys()
    return personajes
   
#funcion que crea un diccionario donde cada personaje se le asocian todos sus dialogos
def crea_diccionario(guion, personajes): 
    parrafo = guion.split('\n')
    dic = {}
    for i in personajes:
        dic[i] = []
    for i in range(len(parrafo)):
        for j in range(len(personajes)):
            if (list(personajes)[j] in list(parrafo)[i]):
                pos = len(list(personajes)[j])
                dialogo = parrafo[i][pos:]
                dic[list(personajes)[j]].append(dialogo) #asocia los dialogos con el personaje
    return dic

#funcion que entrega el personaje que tiene el dialogo mas extenso
def mas_extenso(dicc):
    max = 0
    max_ext = []
    for clave, valor in dicc.items():
        for i in range(len(valor)):
            tmp = filtrar_texto(valor[i]).strip().split(' ')#strip elimina el espacio antes de un string
            if max <= len(tmp):
                max = len(tmp)
    for clave,valor in dicc.items():
        for i in range(len(valor)):
            tmp = filtrar_texto(valor[i]).strip().split(' ')
            if max == len(tmp):
                max_ext.append(clave)
    cuenta1 = collections.Counter(max_ext)
    m_e = cuenta1.keys()
    return m_e

#funcion que entrega un personaje que tiene el dialogo mas corto
def menos_extenso(dicc):
    min = 100000
    min_ext = []
    for clave, valor in dicc.items():
        for i in range(len(valor)):
            tmp = filtrar_texto(valor[i]).strip().split(' ')
            if min >= len(tmp):
                min = len(tmp)
    for clave,valor in dicc.items():
        for i in range(len(valor)):
            tmp = filtrar_texto(valor[i]).strip().split(' ')
            if min == len(tmp):
                min_ext.append(clave)
    cuenta1 = collections.Counter(min_ext)
    m_e = cuenta1.keys()
    return m_e
    
# funcion que entrega el personaje que tiene mas dialogos en el guion 
def mas_dialogo(dicc):
    max = 0
    for clave, valor in dicc.items():#iteritems permite iterar con los elementos del diccionario
        tmp = len(valor)
        if max <= tmp:
            max = tmp
            max_per = clave
    return max_per
# funcion que entrega el personaje que tiene menos dialogos en el guion
def menos_dialogo(dicc):
    min = 100000
    for clave, valor in dicc.items():
        tmp = len(valor)
        if min >= tmp:
            min = tmp
            min_per = clave
    return min_per         

#funcion que dado un personaje y el guion entrega con quien interactuo este personaje
def dialogos (personaje, guion):
    pe = personajes_principales(guion)
    per = []    
    for i in range(len(pe)):
        per.append(filtrar_texto(list(pe)[i]))
    intera = []
    parrafo = []
    parrafo = guion.split('\n')
    
    for j in range(len(per)):
        if per[j] != personaje:
            for i in range(2,len(parrafo)-2):
                if personaje in parrafo[i]:
                    if per[j] in parrafo[i-2]:
                        intera.append(per[j])
                    if per[j] in parrafo[i+2]:
                        intera.append(per[j])
    cuenta1 = collections.Counter(intera)
    diag = cuenta1.keys()
    return diag
