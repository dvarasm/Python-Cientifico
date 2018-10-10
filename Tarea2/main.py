# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import CentroSalud as cs

esp_a = ['broncopulmonar', 'cirugia', 'endocrinologia', 'neurologia', 'cardiologia adulto'
]
esp_b = ['cirugia', 'urologia', 'endocrinologia', 'cardiologia adulto', 'nefrologia', 'broncopulmonar'
]
esp_ab = esp_a + esp_b
para = ['masa','altura','pas','pad']

c1 = cs.CentroSalud("centro_A.csv")
c2 = cs.CentroSalud("centro_B.csv")

print '\n-------------'+c1.nombre_centro()+'-------------\n'
for i in esp_a:
    print '***'+i+': '
    for j in para:
        print j+'= '+c1.estadisticas_especialidad(i,j)
    c1.especialidad_imc(i)
    c1.especialidad_pam(i)
    print'\n'
    
#c1.nuevo_paciente()
#c1.reporte()
#c1.guardar_datos("newDataCentroA.csv")
print '---------------------------------------'

print '\n-------------'+c2.nombre_centro()+'-------------\n'
for i in esp_b:
    print '***'+i+': '
    for j in para:
        print j+'= '+c2.estadisticas_especialidad(i,j)
    c2.especialidad_imc(i)
    c2.especialidad_pam(i)
    print'\n'

#c2.nuevo_paciente()
#c2.reporte()
#c2.guardar_datos("newDataCentroB.csv")
print '---------------------------------------'

c3 = c1 + c2 #Sumar Centros

print '\n-------------'+c3.nombre_centro()+'-------------\n'
for i in esp_ab:
    print '***'+i+': '
    for j in para:
        print j+'= '+c3.estadisticas_especialidad(i,j)
    c3.especialidad_imc(i)
    c3.especialidad_pam(i)
    print'\n'

#c3.nuevo_paciente()
#c3.reporte()
#c3.guardar_datos("newDataCentroAB.csv")
print '---------------------------------------'