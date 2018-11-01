import Tkinter as Tk

v = Tk.Tk()
v.title('Detector')
v.geometry('400x100+600+100')
boton1 = Tk.Button(v,text="Iniciar",bg='red')
boton1.grid(row=1,column=1)
boton2 = Tk.Button(v,text="Detener",bg='blue')
boton2.grid(row=1,column=2)
v.mainloop()