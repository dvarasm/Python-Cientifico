# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import CentroSalud as cs

c1 = cs.CentroSalud("centro_A.csv")
c2 = cs.CentroSalud("centro_B.csv")
#c1.imprimir()
print c1.estadisticas_especialidad("cirugia","masa")
c1.especialidad_imc("cirugia")
c1.especialidad_pam("cirugia")
c1.especialidad_imc("cardiologia adulto")
c1.especialidad_pam("cardiologia adulto")
c1.guardar_datos("hoa.csv")
c2.especialidad_imc("cardiologia adulto")
c1.reporte()
c3 = c1 +c2
#c3.imprimir()
c3.especialidad_imc("cardiologia adulto")