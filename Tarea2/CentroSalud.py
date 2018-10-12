# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import pandas as pd
import time,collections,random,webbrowser#librerias que se utlizaron

class CentroSalud:
    def __init__(self,nombre_archivo):#inicializar variables iniciales
        self.nombre_archivo = nombre_archivo
        self.datos = pd.read_csv(self.nombre_archivo,sep=';')#datos obtenidos del archivo csv
        
    def especialidades_centro(self):# metodo que entrega todas las especialidades del centro sin repeticiones
        data = np.asarray(self.datos)
        esp_data = []
        for i in range(len(data)):
            esp_data.append(data[i][1])#obtener todas las especialidades
        return (collections.Counter(esp_data)).keys()#funcion collection para eliminar elementos repetidos
        
    def nombre_centro(self):# metodo que devuelve el nombre del centro
        return str(self.nombre_archivo.rstrip('.csv'))

    def estadisticas_especialidad (self,especialidad,parametro):# metodo que retorna una tupla con el valor promedio y la desviacion estandar
        p = np.asarray(self.datos.set_index('especialidad').loc[especialidad,parametro])
        desviacion = int(p.std())# funcion std para calcular la desviacion estandar 
        promedio = round(float(p.mean()),2)#funcion mean para calcular el promedio
        return str(promedio)+'+-'+str(desviacion)       
        
    def especialidad_imc (self,especialidad):
        m = np.asarray(self.datos.set_index('especialidad').loc[especialidad,"masa"])
        a = np.asarray(self.datos.set_index('especialidad').loc[especialidad,"altura"])
        IMC,obeso = [],0
        for i in range(len(m)):
           IMC.append((float(m[i])/((float(a[i])/100.0)**2)))#formula para calcular el IMC
           if(IMC[i]>=30):
               obeso+=1 #cantidad de pacientes que tienen obecidad
        imc_a = np.array(IMC)
        promedio = round(float(imc_a.mean()),2)#funcion mean para calcular el promedio
        desviacion = int(imc_a.std())# funcion std para calcular la desviacion estandar
        print "Promedio IMC: "+str(promedio)+'+-'+str(desviacion)+" Pacientes con obesidad: "+str(obeso)        
        
    def especialidad_pam (self,especialidad):
        pas = np.asarray(self.datos.set_index('especialidad').loc[especialidad,"pas"])
        pad = np.asarray(self.datos.set_index('especialidad').loc[especialidad,"pad"])
        PAM,normal = [],0
        for i in range(len(pas)):
           PAM.append(((float(2*pad[i]))+float(pas[i]))/3)#formula para calcular el PAM
           if(PAM[i]>=70 and PAM[i]<=105):
               normal+=1 #cantidad de pacientes en rango normal
        pam_a = np.array(PAM)
        promedio = round(float(pam_a.mean()),2)#funcion mean para calcular el promedio
        desviacion = int(pam_a.std())# funcion std para calcular la desviacion estandar
        print "Promedio PAM: "+str(promedio)+'+-'+str(desviacion)+" Pacientes con un rango normal: "+str(normal)
    
    def nuevo_paciente(self):
        id = int(random.randrange(min(self.datos['ID']),max(self.datos['ID'])))       
        new = pd.DataFrame(columns=['ID','especialidad','masa','altura','pas','pad'])#creacion de dataframe vacio, solo con las columnas , para poder guardar los datos obtenidos por consola
        esp = raw_input("Especialidad: ")#parametro recibido por consola 
        masa = int(input("Masa: "))#parametro recibido por consola
        altura = int(input("Altura: "))#parametro recibido por consola
        pas = int(input("PAS: "))#parametro recibido por consola
        pad = int(input("PAD: "))#parametro recibido por consola
        new = new.append([{'ID':id,'especialidad':esp,'masa':masa,'altura':altura,'pas':pas,'pad':pad}])#agregar datos obtenidos por consola al dataframe
        self.datos = pd.concat([self.datos,new],ignore_index=True)# funcion para concatenar 2 dataframe
        print 'Paciente Agregado'
        
    def guardar_datos(self,nombre_archivo_csv):# metodo para guardar el dataframe datos en un archivo csv
        self.datos.set_index('ID').to_csv(nombre_archivo_csv,sep=str(';'))        
        print 'Archivo Guardado'
        
    def reporte(self):#metodo para generar reporte
        file = open(str(self.nombre_centro())+"_"+str(time.strftime("%d_%m_%y"))+".txt", "w")#fincion para crear una archivo txt vacio que contiene la fecha actual de la libreria time mediante la funcion strftime      
        file.write("Reporte\nCentro de Salud: "+str(self.nombre_centro())+"\nEstadisticas por especialidad:\n\n")
        esp = self.especialidades_centro()#especialidad del centro
        for i in range(len(esp)):
            file.write(str(esp[i]+":\n"))#datos a guardar en archivo txt
            file.write("Masa: "+self.estadisticas_especialidad(esp[i],"masa")+" kg\n")#datos a guardar en archivo txt
            file.write("Altura: "+self.estadisticas_especialidad(esp[i],"altura")+" cm\n")#datos a guardar en archivo txt
            file.write("Pas: "+self.estadisticas_especialidad(esp[i],"pas")+" mmHg\n")#datos a guardar en archivo txt
            file.write("Pad: "+self.estadisticas_especialidad(esp[i],"pad")+" mmHg\n\n") #datos a guardar en archivo txt
        file.close()        
        ar = webbrowser.open(str(self.nombre_centro())+"_"+str(time.strftime("%d_%m_%y"))+".txt")#funcion para desplegar el archivo txt
        if ar is True:#comprobar que se desplego el archivo
            print 'Reporte Desplegado de '+self.nombre_centro()
        else:
            print 'Error al abrir reporte de '+self.nombre_centro()
            
    def __add__(self,otro):#metodo para sumar centros
        centro = CentroSalud(str(self.nombre_archivo))#crea un objeto centro
        centro.datos = pd.concat([self.datos,otro.datos])#se concatena los datos de los centros a sumar
        centro.nombre_archivo = str(self.nombre_centro())+"_"+str(otro.nombre_centro())#concatena nombre de los archivos 
        return centro #centro nuevo compuesto 