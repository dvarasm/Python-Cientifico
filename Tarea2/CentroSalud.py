# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import pandas as pd

class CentroSalud:
    def __init__(self,nombre_archivo):
        self.nombre_archivo = nombre_archivo
        self.datos = pd.read_csv(self.nombre_archivo,sep=';', index_col =['especialidad'])
        
    def imprimir(self):
        print self.datos
        print self.datos.loc["cirugia", "masa"]
        print len(self.datos.loc["cirugia", "masa"])

    def estadisticas_especialidad (self,especialidad,parametro):
        p = np.asarray(self.datos.loc[especialidad,parametro])
        desviacion = p.std()
        promedio = p.mean()
        solucion = str(int(promedio))+"+-"+str(int(desviacion))
        return solucion         
        #return {'Promedio':int(promedio),'DesEst':int(desviacion)}
        
    def especialidad_imc (self,especialidad):
        m = np.asarray(self.datos.loc[especialidad,"masa"])
        a = np.asarray(self.datos.loc[especialidad,"altura"])
        print a,m        
        IMC = []
        j=0
        obeso=0
        for i in range(len(m)):
           IMC.append((float(m[i])/((float(a[j])/100.0)**2)))
           if(IMC[i]>=30):
               obeso+=1
           j+=1
        imc_a = np.array(IMC)
        print imc_a
        promedio = imc_a.mean()
        desviacion = imc_a.std()
        print "Promedio IMC: "+str(int(promedio))+"+-"+str(int(desviacion))+" Pacientes con obesidad: "+str(obeso)        
        
    def especialidad_pam (self,especialidad):
        return None
    
    def nuevo_paciente(self):
        return None
        
    def guardar_datos(self,nombre_archivo_csv):
        return None
        
    def reporte(self):
        return None
    
    def __add__(self):
        return None