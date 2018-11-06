from tkinter import *
from PIL import ImageTk, Image
import os

v = Tk()#ventana de tipo tkinter
v.title('Detector')#titulo de ventana
v.geometry('800x400')#tamano de ventana
v.resizable(width=False, height=False)#la ventana no se puede cambiar de tamano

def funcion_b1():#funcion del boton 1
    print ("Iniciar")

def funcion_b2():#funcion del boton 2
    print ("Parar")

numero = 8 #variable a obtener
var_sos = "Elementos\nsospechosos: "+str(numero)

#contenido de la ventana
boton1 = Button(v,text="Iniciar Deteccion",command=funcion_b1,width=13, height=1,bg='green',foreground="white").place(x=20,y=30)
boton2 = Button(v,text="Parar Deteccion",command=funcion_b2,width=13, height=1,bg='red',foreground="white").place(x=20,y=60)
texto = Label(v,text=var_sos,bg='grey',justify="center",width=13).place(x=20,y=350)
image = Image.open("ma.png")
image = image.resize((620, 350), Image.ANTIALIAS)#redimensionar imagen
img = ImageTk.PhotoImage(image)
panel = Label(v, image = img,width=620, height=350).place(x=150,y=30)#panel que contiene la imagen
v.mainloop()#para qe se vea la ventana