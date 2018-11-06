# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import CentroSalud as cs

#main para mostrar todas las funcionalidades de la Clase CentroSalud()

c1 = cs.CentroSalud("centro_A.csv")#crea objeto centro 1
c2 = cs.CentroSalud("centro_B.csv")#crea objeto centro 2
c3 = c1 + c2 #Sumar Objetos CentroSalud

esp_a = c1.especialidades_centro()#metodo que obtiene todas las especialidades del centro
esp_b = c2.especialidades_centro()#metodo que obtiene todas las especialidades del centro
esp_ab = esp_a + esp_b #suma las especialidades para el centro c3
para = ['masa','altura','pas','pad'] #parametros

print ('\n-------------'+c1.nombre_centro()+'-------------\n')#imprimir todas las estadisticas del centro
for i in esp_a:
    print ('***'+i+': ')#imprime nombre de la especialidad
    for j in para:
        print (j+'= '+c1.estadisticas_especialidad(i,j))#imprime estadistica por especialidad
    c1.especialidad_imc(i)#imprime IMC por especialidad
    c1.especialidad_pam(i)#imprime PAM por especialidad
    print ('\n')
    
c1.nuevo_paciente()#crea un paciente nuevo
c1.reporte()#crea el reporte
c1.guardar_datos("newDataCentroA.csv")#guarda los datos en un archivo csv
print ('---------------------------------------')

print ('\n-------------'+c2.nombre_centro()+'-------------\n')#imprimir todas las estadisticas del centro
for i in esp_b:
    print ('***'+i+': ')#imprime nombre de la especialidad
    for j in para:
        print (j+'= '+c2.estadisticas_especialidad(i,j))#imprime estadistica por especialidad
    c2.especialidad_imc(i)#imprime IMC por especialidad
    c2.especialidad_pam(i)#imprime PAM por especialidad
    print ('\n')

c2.nuevo_paciente()#crea un paciente nuevo
c2.reporte()#crea el reporte
c2.guardar_datos("newDataCentroB.csv")#guarda los datos en un archivo csv
print ('---------------------------------------')

print ('\n-------------'+c3.nombre_centro()+'-------------\n')#imprimir todas las estadisticas del centro
for i in esp_ab:
    print ('***'+i+': ')#imprime nombre de la especialidad
    for j in para:
        print (j+'= '+c3.estadisticas_especialidad(i,j))#imprime estadistica por especialidad
    c3.especialidad_imc(i)#imprime IMC por especialidad
    c3.especialidad_pam(i)#imprime PAM por especialidad
    print ('\n')

c3.nuevo_paciente()#crea un paciente nuevo
c3.reporte()#crea el reporte
c3.guardar_datos("newDataCentroAB.csv")#guarda los datos en un archivo csv
print ('---------------------------------------')