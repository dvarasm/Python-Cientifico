# -*- coding: utf-8 -*-
#from __future__ import unicode_literals
import numpy as np
import pandas as pd
import time,collections,random,webbrowser

class CentroSalud:
    def __init__(self,nombre_archivo):
        self.nombre_archivo = nombre_archivo
        self.datos = pd.read_csv(self.nombre_archivo,sep=';')
        
    def nombre_centro(self):
        return str(self.nombre_archivo.rstrip('.csv'))

    def estadisticas_especialidad (self,especialidad,parametro):
        p = np.asarray(self.datos.set_index('especialidad').loc[especialidad,parametro])
        desviacion = int(p.std())
        promedio = round(float(p.mean()),2)
        return str(promedio)+"+-"+str(desviacion)       
        
    def especialidad_imc (self,especialidad):
        m = np.asarray(self.datos.set_index('especialidad').loc[especialidad,"masa"])
        a = np.asarray(self.datos.set_index('especialidad').loc[especialidad,"altura"])
        IMC,obeso = [],0
        for i in range(len(m)):
           IMC.append((float(m[i])/((float(a[i])/100.0)**2)))
           if(IMC[i]>=30):
               obeso+=1
        imc_a = np.array(IMC)
        promedio = round(float(imc_a.mean()),2)
        desviacion = int(imc_a.std())
        print "Promedio IMC: "+str(promedio)+"+-"+str(desviacion)+" Pacientes con obesidad: "+str(obeso)        
        
    def especialidad_pam (self,especialidad):
        pas = np.asarray(self.datos.set_index('especialidad').loc[especialidad,"pas"])
        pad = np.asarray(self.datos.set_index('especialidad').loc[especialidad,"pad"])
        PAM,normal = [],0
        for i in range(len(pas)):
           PAM.append(((float(2*pad[i]))+float(pas[i]))/3)
           if(PAM[i]>=70 and PAM[i]<=105):
               normal+=1
        pam_a = np.array(PAM)
        promedio = round(float(pam_a.mean()),2)
        desviacion = int(pam_a.std())
        print "Promedio PAM: "+str(promedio)+"+-"+str(desviacion)+" Pacientes con un rango normal: "+str(normal)
    
    def nuevo_paciente(self):
        id = int(random.randrange(min(self.datos['ID']),max(self.datos['ID'])))       
        new = pd.DataFrame(columns=['ID','especialidad','masa','altura','pas','pad'])
        esp = raw_input("Especialidad: ")
        masa = int(input("Masa: "))
        altura = int(input("Altura: "))
        pas = int(input("PAS: "))
        pad = int(input("PAD: "))
        new = new.append([{'ID':id,'especialidad':esp,'masa':masa,'altura':altura,'pas':pas,'pad':pad}])
        self.datos = pd.concat([self.datos,new],ignore_index=True)
        print 'Paciente Agregado'
        
    def guardar_datos(self,nombre_archivo_csv):
        self.datos.set_index('ID').to_csv(nombre_archivo_csv,sep=str(';'))        
        print 'Archivo Guardado'
        
    def reporte(self):
        file = open(str(self.nombre_centro())+"_"+str(time.strftime("%d_%m_%y"))+".txt", "w")        
        file.write("Reporte\nCentro de Salud: "+str(self.nombre_centro())+"\nEstadisticas por especialidad:\n\n")
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
        ar = webbrowser.open(str(self.nombre_centro())+"_"+str(time.strftime("%d_%m_%y"))+".txt")
        if ar is True:
            print 'Reporte Desplegado de '+self.nombre_centro()
        else:
            print 'Error al abrir reporte de '+self.nombre_centro()
            
    def __add__(self,otro):
        centro = CentroSalud(str(self.nombre_archivo))
        centro.datos = pd.concat([self.datos,otro.datos])
        centro.nombre_archivo = str(self.nombre_centro())+"_"+str(otro.nombre_centro())
        return centro