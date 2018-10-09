# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import pandas as pd
import time
import collections
import os

class CentroSalud:
    def __init__(self,nombre_archivo):
        self.nombre_archivo = nombre_archivo
        self.datos = pd.read_csv(self.nombre_archivo,sep=';')

    def estadisticas_especialidad (self,especialidad,parametro):
        p = np.asarray(self.datos.set_index('especialidad').loc[especialidad,parametro])
        desviacion = p.std()
        promedio = p.mean()
        return str(int(promedio))+"+-"+str(int(desviacion))       
        
    def especialidad_imc (self,especialidad):
        m = np.asarray(self.datos.set_index('especialidad').loc[especialidad,"masa"])
        a = np.asarray(self.datos.set_index('especialidad').loc[especialidad,"altura"])
        IMC = []
        obeso=0
        for i in range(len(m)):
           IMC.append((float(m[i])/((float(a[i])/100.0)**2)))
           if(IMC[i]>=30):
               obeso+=1
        imc_a = np.array(IMC)
        promedio = imc_a.mean()
        desviacion = imc_a.std()
        print "Promedio IMC: "+str(int(promedio))+"+-"+str(int(desviacion))+" Pacientes con obesidad: "+str(obeso)        
        
    def especialidad_pam (self,especialidad):
        pas = np.asarray(self.datos.set_index('especialidad').loc[especialidad,"pas"])
        pad = np.asarray(self.datos.set_index('especialidad').loc[especialidad,"pad"])
        PAM = []
        normal=0
        for i in range(len(pas)):
           PAM.append(((float(2*pad[i]))+float(pas[i]))/3)
           if(PAM[i]>=70 and PAM[i]<=105):
               normal+=1
        pam_a = np.array(PAM)
        promedio = pam_a.mean()
        desviacion = pam_a.std()
        print "Promedio PAM: "+str(int(promedio))+"+-"+str(int(desviacion))+" Pacientes con un rango normal: "+str(normal)
    
    def nuevo_paciente(self):
        return None
        
    def guardar_datos(self,nombre_archivo_csv):
        self.datos.set_index('ID').to_csv(nombre_archivo_csv,sep=str(';'))        
        print 'Archivo Guardado'
        
    def reporte(self):
        file = open(str(self.nombre_archivo.rstrip('.csv'))+"_"+str(time.strftime("%d_%m_%y"))+".txt", "w")        
        file.write("Reporte\nCentro de Salud: "+str(self.nombre_archivo.rstrip('.csv'))+"\nEstadisticas por especialidad:\n\n")
        data = np.asarray(self.datos)
        esp_data = []
        for i in range(len(data)):
            esp_data.append(data[i][1])
        esp = (collections.Counter(esp_data)).keys()
        for i in range(len(esp)):
            file.write(str(esp[i]+":\n"))
            file.write("Masa: "+self.estadisticas_especialidad(esp[i],"masa")+" kg\n")
            file.write("Altura: "+self.estadisticas_especialidad(esp[i],"altura")+" cm\n")
            file.write("Pas: "+self.estadisticas_especialidad(esp[i],"pas")+" mmHg\n")
            file.write("Pad: "+self.estadisticas_especialidad(esp[i],"pad")+" mmHg\n\n") 
        file.close()
        os.system(str(self.nombre_archivo.rstrip('.csv'))+"_"+str(time.strftime("%d_%m_%y"))+".txt")
        return None
    
    def __add__(self,otro):
        centro = CentroSalud(str(self.nombre_archivo))
        centro.datos = pd.concat([self.datos,otro.datos])
        centro.nombre_archivo = str(self.nombre_archivo.rstrip('.csv'))+"_"+str(otro.nombre_archivo)
        return centro