# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import CentroSalud as cs

c1 = cs.CentroSalud("centro_A.csv")

#c1.imprimir()
print c1.estadisticas_especialidad("cirugia","masa")
c1.especialidad_imc("cirugia")

