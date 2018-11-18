from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic
import sys,os

class App(QtWidgets.QApplication):
    def __init__(self, *args):
        QtWidgets.QApplication.__init__(self, *args)
        self.MainWindow = QtWidgets.QMainWindow()#crea la ventana
        self.MainWindow.ui = uic.loadUi('vista.ui')#carga la interfaz
        self.MainWindow.ui.setWindowTitle("Detector")#nombre de la ventana
        self.MainWindow.ui.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint|QtCore.Qt.WindowCloseButtonHint)#para no redimensionar
        self.MainWindow.ui.show()#muestra la ventana
        
        #variables globales
        self.path = '' #almacena la direccion del archivo a analizar 
        self.completed =0 #variable para la barra de carga
        self.detec = 0 #variable que almacena numero de elementos detectados
                
        #self.connect(self.MainWindow.ui.saludar, QtCore.SIGNAL('clicked()'), self.saludar)#ejemplo pyqt4
        #self.MainWindow.ui.saludar.clicked.connect(self.saludar)#ejemplo pyqt5
        
        #Listener de los Botones
        self.MainWindow.ui.Iniciar.clicked.connect(self.iniciar_det)#listener del boton iniciar deteccion
        self.MainWindow.ui.Quitar.clicked.connect(self.quitar_img)#listener del boton quitar imagen
        self.MainWindow.ui.cargar_imagen.clicked.connect(self.cargar_imagen)#listener del boton cargar imagen
        self.MainWindow.ui.original.clicked.connect(self.original)#listener del boton original
        self.MainWindow.ui.filtro1.clicked.connect(self.filtro1)#listener del boton filtro 1
        self.MainWindow.ui.filtro2.clicked.connect(self.filtro2)#listener del boton filtro 2
        self.MainWindow.ui.filtro3.clicked.connect(self.filtro3)#listener del boton filtro 3
        
        #Condiciones iniciales de la app
        self.parametros_iniciales()
        
    #Metodos
    def parametros_iniciales(self):#funcion que contrala todas los parametros iniciales de la app
        self.completed =0 #pone variable para la barra de carga en 0
        self.path = '' #pone la variable path vacia
        self.detec = 0 #pone la variable detec en 0
        self.MainWindow.ui.barra.setEnabled(False)#deshabilita la barra de carga al inicio
        self.MainWindow.ui.Quitar.setEnabled(False)#deshabilita el botton quitar
        self.MainWindow.ui.Iniciar.setEnabled(False)#deshabilita el boton iniciar
        self.MainWindow.ui.cargar_imagen.setEnabled(True)#habilita el boton cargar
        self.estado_botones(0,False)
        self.MainWindow.ui.barra.setValue(self.completed)#deja la barra de carga en 0
        self.MainWindow.ui.LCDnumber.display(self.detec)#cambia el numero del LCD

    def estado_botones(self,num,estado):#funcion para habilitar/deshabilitar botones de parametros de la imagen
        if(num == 0):
            self.MainWindow.ui.original.setEnabled(estado)#Cambia el estado True/False del boton original
            self.MainWindow.ui.filtro1.setEnabled(estado)#Cambia el estado True/False del boton filtro 1
            self.MainWindow.ui.filtro2.setEnabled(estado)#Cambia el estado True/False del boton filtro 2
            self.MainWindow.ui.filtro3.setEnabled(estado)#Cambia el estado True/False del boton filtro 3
        if(num ==1):    
            self.MainWindow.ui.original.setEnabled(estado)#Cambia el estado True/False del boton original
        if(num ==2):    
            self.MainWindow.ui.filtro1.setEnabled(estado)#Cambia el estado True/False del boton filtro 1
        if(num ==3):    
            self.MainWindow.ui.filtro2.setEnabled(estado)#Cambia el estado True/False del boton filtro 2
        if(num ==4):
            self.MainWindow.ui.filtro3.setEnabled(estado)#Cambia el estado True/False del boton filtro 3  

    def iniciar_det(self):#funcion del boton iniciar
        if(self.path!=''):
            self.MainWindow.ui.barra.setEnabled(True)#habilita la barra
            self.completed = 0
            tmp = False #flag para ver si la barra llego a 100% y poder continuar
            while self.completed < 100:
                self.completed += 0.0001
                self.MainWindow.ui.barra.setValue(self.completed)#cambia el valor de la barra de progreso
                tmp = True
            if(tmp==True):
                self.MainWindow.ui.Iniciar.setEnabled(False)#deshabilita el botor iniciar cuando ya fue apretado 1 vez
                self.MainWindow.ui.Quitar.setEnabled(True)#habilita el boton Quitar imagen
                self.detec += 1 #elemento variable
                self.MainWindow.ui.LCDnumber.display(self.detec)#cambia el numero LCD
                pixmap = QtGui.QPixmap(self.path)#carga la imagen
                pixmap = pixmap.scaled(600, 400)#redmensiona la imagen
                self.MainWindow.ui.imagen_an.setPixmap(pixmap)#cambia la imagen
                self.estado_botones(0,True)
        else:
            QtWidgets.QMessageBox.about(self.MainWindow, "Error","No hay imagen cargada para analizar")

    def quitar_img(self):#funcion del boton quitar
        if(self.path!=''):
            self.MainWindow.ui.imagen_an.setText('Agregar imagen a analizar')#Cambia el label 
            self.parametros_iniciales()
            QtWidgets.QMessageBox.about(self.MainWindow, " ","Se quito imagen analizada")
        else:
            QtWidgets.QMessageBox.about(self.MainWindow, "Error","No hay imagen cargada")

    def cargar_imagen(self):#funcion del boton cargar imagen
        self.path,m = QtWidgets.QFileDialog.getOpenFileName(self.MainWindow, 'Abrir Imagen',"","Image files (*.jpg *.png)")
        if(self.path!= ''):
            self.MainWindow.ui.cargar_imagen.setEnabled(False)#deshabilita el boton
            self.MainWindow.ui.Iniciar.setEnabled(True)#habilita el boton
            self.MainWindow.ui.Quitar.setEnabled(True)#habilita el boton
            pixmap = QtGui.QPixmap(self.path)#carga la imagen
            pixmap = pixmap.scaled(600, 400)#redmensiona la imagen
            self.MainWindow.ui.imagen_an.setPixmap(pixmap)#cambia la imagen
        else:
            QtWidgets.QMessageBox.about(self.MainWindow, " ","No selecciono ninguna imagen para cargar")

    def original(self):
        if(self.path!= ''):
            pixmap = QtGui.QPixmap(self.path)#carga la imagen
            pixmap = pixmap.scaled(600, 400)#redmensiona la imagen
            self.MainWindow.ui.imagen_an.setPixmap(pixmap)#cambia la imagen
            self.estado_botones(0,True)
            self.estado_botones(1,False)
        else:
            QtWidgets.QMessageBox.about(self.MainWindow, "Error","No hay imagen cargada")
    
    def filtro1(self):
        if(self.path!= ''):    
            pixmap = QtGui.QPixmap(self.path)#carga la imagen
            pixmap = pixmap.scaled(600, 400)#redmensiona la imagen
            self.MainWindow.ui.imagen_an.setPixmap(pixmap)#cambia la imagen
            self.estado_botones(0,True)
            self.estado_botones(2,False)
        else:
            QtWidgets.QMessageBox.about(self.MainWindow, "Error","No hay imagen cargada")

    def filtro2(self):
        if(self.path!= ''):
            pixmap = QtGui.QPixmap(self.path)#carga la imagen
            pixmap = pixmap.scaled(600, 400)#redmensiona la imagen
            self.MainWindow.ui.imagen_an.setPixmap(pixmap)#cambia la imagen
            self.estado_botones(0,True)
            self.estado_botones(3,False)
        else:
            QtWidgets.QMessageBox.about(self.MainWindow, "Error","No hay imagen cargada")

    def filtro3(self):
        if(self.path!= ''):
            pixmap = QtGui.QPixmap(self.path)#carga la imagen
            pixmap = pixmap.scaled(600, 400)#redmensiona la imagen
            self.MainWindow.ui.imagen_an.setPixmap(pixmap)#cambia la imagen
            self.estado_botones(0,True)
            self.estado_botones(4,False)
        else:
            QtWidgets.QMessageBox.about(self.MainWindow, "Error","No hay imagen cargada")
                
## Se crea una funcion que cree un objeto aplicacion, entregandole argumentos de sistema.
def main(args):
    app = App(args)
    app.exec_()

## Se ejecuta
if __name__ == "__main__":
    main(sys.argv)
