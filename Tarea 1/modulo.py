# -*- coding: utf-8 -*-

def leer_archivo(nombre = "guion.txt"):
    #entrada: nombre archivo
    #salida: string
    #guion.txt y modulo.py deben estar en el mismo directorio de su script
    with open(nombre, "r") as a:
        return a.read()
        
#Para usar la funcion, puede utilizar la siguiente linea de codigo en su script
#string = leer_archivo()

#def dialogos (personaje, guion):
#    #entrada: personaje (string), guion (string)
#    #salida: otro_personaje (string)
#    '''
#    codigo
#    '''
#    return otro_personaje
