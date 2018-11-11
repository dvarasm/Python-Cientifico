from tkinter import *
from PIL import ImageTk, Image
import os

class GUI(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        w,h = 800, 400
        master.minsize(width=w, height=h)
        master.maxsize(width=w, height=h)
        master.title('Detector')#titulo de ventana
        master.resizable(width=False, height=False)#la ventana no se puede cambiar de tamano
        numero = 8 #variable a obtener
        var_sos = "Elementos\nsospechosos: "+str(numero)

        #contenido de la ventana
        self.boton1 = Button(self,text="Iniciar Deteccion",command=self.nextImage,width=13, height=1,bg='green',foreground="white").place(x=20,y=30)
        self.boton2 = Button(self,text="Parar Deteccion",command=self.funcion_b2,width=13, height=1,bg='red',foreground="white").place(x=20,y=60)
        self.texto = Label(self,text=var_sos,bg='grey',justify="center",width=13).place(x=20,y=350)
        self.image = Image.open("ma.png")
        self.image = self.image.resize((620, 350), Image.ANTIALIAS)#redimensionar imagen
        self.img = ImageTk.PhotoImage(self.image)
        self.panel = Label(self, image = self.img,width=620, height=350).place(x=150,y=30)#panel que contiene la imagen

    def funcion_b1(self):#funcion del boton 1
        print ("Iniciar")

    def funcion_b2(self):#funcion del boton 2
        print ("Parar")

    def nextImage(self): 
        self.image2 = PhotoImage(file='fuji.png')
        self.Label.configure(image=self.image2)
        self.Label.image=self.image2


root = Tk()
app = GUI(root)
app.mainloop()