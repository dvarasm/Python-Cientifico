import Tkinter as Tk

v = Tk.Tk()
v.title('Detector')#titulo de ventana
v.geometry('800x600')#tamano de ventana

def funcion_b1():#funcion del boton 1
    
    print "Iniciar"

def funcion_b2():#funcion del boton 2
    print "Parar"

numero = 8
var_sos = "Elementos\nsospechosos: "+str(numero)

boton1 = Tk.Button(v,text="Iniciar Deteccion",command=funcion_b1,width=13, height=1,bg='green')
boton1.grid(row=1,column=1)#posicion boton 1
boton2 = Tk.Button(v,text="Parar Deteccion",command=funcion_b2,width=13, height=1,bg='red')
boton2.grid(row=2,column=1)#posicion boton 2
texto = Tk.Label(v,text=var_sos,bg='grey')
texto.grid(row=4,column=1)

v.mainloop()#para qe se vea la ventana