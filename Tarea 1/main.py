# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import modulo as m 

guion = m.leer_archivo()

per = m.personajes_principales(guion)
dicc = m.crea_diccionario(guion,per)

print 'Numero de personajes: %s' %(str(len(per)))
print 'Personajes: '
for i in range(len(per)):
    print ' ',str(m.filtrar_texto(per[i]))
print 'Personaje que tiene el dialogo mas largo: ',str(len(m.mas_extenso(dicc))), 'personajes' 
print m.mas_extenso(dicc)
print 'Personaje que tiene el dialogo mas corto: ', str(len(m.menos_extenso(dicc))), 'personajes'
print m.menos_extenso(dicc)
print 'Personaje que tiene mas dialogo en el guion: ',m.mas_dialogo(dicc)
print 'Personaje que tiene menos dialogo en el guion: ',m.menos_dialogo(dicc)
print 'Ingrese personaje para ver con quien interactua: '
p= raw_input()
pp = p.upper()
pers = []
for i in range(len(per)):
    pers.append(m.filtrar_texto(per[i]))
tmp = 0
for i in pers:
    if pp in i:
        print pp, ' Interactua con : ',len(m.dialogos(pp,guion)),' personajes'
        print m.dialogos(pp,guion)
        tmp +=1
if tmp == 0:        
    print 'No existe el personaje!!'