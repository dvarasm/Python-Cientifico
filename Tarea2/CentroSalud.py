import numpy as np
import pandas as pd

class CentroSalud:
    def __init__(self,nombre_archivo):
        self.archivo = nombre_archivo

    def abrir_archivo (self):
        datos = pd.read_csv('archivo',sep=';')
        return datos
        
    def estadisticas_especialidad (self,especialidad,parametro):
        return None
        
    def especialidad_imc (self,especialidad):
        return None
        
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