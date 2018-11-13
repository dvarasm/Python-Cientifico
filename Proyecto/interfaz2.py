from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic
import sys,os

class App(QtWidgets.QApplication):
    def __init__(self, *args):
        QtWidgets.QApplication.__init__(self, *args)
        self.MainWindow = QtWidgets.QMainWindow()
        self.MainWindow.ui = uic.loadUi('vista.ui')#carga la interfaz
        self.MainWindow.ui.setWindowTitle("Detector")#nombre de la ventana
        self.MainWindow.ui.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint|QtCore.Qt.WindowCloseButtonHint)#para no redimensionar
        self.MainWindow.ui.show()
        self.path = ''
        self.completed =0
                
        #self.connect(self.MainWindow.ui.saludar, QtCore.SIGNAL('clicked()'), self.saludar)#ejemplo pyqt4
        #self.MainWindow.ui.saludar.clicked.connect(self.saludar)#ejemplo pyqt5
        
        #botones
        self.MainWindow.ui.Iniciar.clicked.connect(self.funcion_b1)#listener del boton iniciar
        self.MainWindow.ui.Quitar.clicked.connect(self.funcion_b2)#listener del boton parar
        self.MainWindow.ui.cargar_imagen.clicked.connect(self.cargar_imagen)
        self.MainWindow.ui.original.clicked.connect(self.original)
        self.MainWindow.ui.filtro1.clicked.connect(self.filtro1)
        self.MainWindow.ui.filtro2.clicked.connect(self.filtro2)
        self.MainWindow.ui.filtro3.clicked.connect(self.filtro3)
        self.MainWindow.ui.barra.setValue(self.completed)
        self.MainWindow.ui.barra.setEnabled(False)
        
        self.MainWindow.ui.original.setEnabled(False)
        self.MainWindow.ui.filtro1.setEnabled(False)
        self.MainWindow.ui.filtro2.setEnabled(False)
        self.MainWindow.ui.filtro3.setEnabled(False)

        #imagen
        #pixmap = QtGui.QPixmap('m.png')#carga la imagen
        #pixmap = pixmap.scaled(600, 400)#redimensiona la imagen
        #self.MainWindow.ui.imagen_an.setPixmap(pixmap)#agrega imagen
        
        self.sosp = 0 #elemento a obtener 
        
    # metodos

    def funcion_b1(self):#funcion del boton iniciar
        if(self.path!=''):
            self.MainWindow.ui.barra.setEnabled(True)
            self.completed = 0
            while self.completed < 100:
                self.completed += 0.0001
                self.MainWindow.ui.barra.setValue(self.completed)

            self.sosp += 1 #elemento variable
            self.MainWindow.ui.LCDnumber.display(self.sosp)#cambia el numero LCD
            pixmap = QtGui.QPixmap('fuji.png')#carga la imagen
            pixmap = pixmap.scaled(600, 400)#redmensiona la imagen
            self.MainWindow.ui.imagen_an.setPixmap(pixmap)#cambia la imagen
            self.MainWindow.ui.original.setEnabled(True)
            self.MainWindow.ui.filtro1.setEnabled(True)
            self.MainWindow.ui.filtro2.setEnabled(True)
            self.MainWindow.ui.filtro3.setEnabled(True)
        else:
            QtWidgets.QMessageBox.about(self.MainWindow, "Error","No hay imagen cargada para analizar")

    def funcion_b2(self):#funcion del boton quitar
        if(self.path!=''):
            self.path = ''
            self.MainWindow.ui.imagen_an.setText('Agregar imagen a analizar')
            QtWidgets.QMessageBox.about(self.MainWindow, " ","Se quito imagen analizada")
        else:
            QtWidgets.QMessageBox.about(self.MainWindow, "Error","No hay imagen cargada")

    def cargar_imagen(self):#funcion del boton cargar imagen
        self.path,m = QtWidgets.QFileDialog.getOpenFileName(self.MainWindow, 'Abrir Imagen',"","Image files (*.jpg *.png)")
        if(self.path!= ''):
            pixmap = QtGui.QPixmap(self.path)
            pixmap = pixmap.scaled(600, 400)
            self.MainWindow.ui.imagen_an.setPixmap(pixmap)
        else:
            QtWidgets.QMessageBox.about(self.MainWindow, " ","No selecciono ninguna imagen para cargar")

    def original(self):
        if(self.path!= ''):
            pixmap = QtGui.QPixmap(self.path)
            pixmap = pixmap.scaled(600, 400)
            self.MainWindow.ui.imagen_an.setPixmap(pixmap)
            self.MainWindow.ui.original.setEnabled(False)
            self.MainWindow.ui.filtro1.setEnabled(True)
            self.MainWindow.ui.filtro2.setEnabled(True)
            self.MainWindow.ui.filtro3.setEnabled(True)
        else:
            QtWidgets.QMessageBox.about(self.MainWindow, "Error","No hay imagen cargada")
    
    def filtro1(self):
        if(self.path!= ''):    
            pixmap = QtGui.QPixmap(self.path)
            pixmap = pixmap.scaled(600, 400)
            self.MainWindow.ui.imagen_an.setPixmap(pixmap)
            self.MainWindow.ui.filtro1.setEnabled(False)
            self.MainWindow.ui.original.setEnabled(True)
            self.MainWindow.ui.filtro2.setEnabled(True)
            self.MainWindow.ui.filtro3.setEnabled(True)
        else:
            QtWidgets.QMessageBox.about(self.MainWindow, "Error","No hay imagen cargada")

    def filtro2(self):
        if(self.path!= ''):
            pixmap = QtGui.QPixmap(self.path)
            pixmap = pixmap.scaled(600, 400)
            self.MainWindow.ui.imagen_an.setPixmap(pixmap)
            self.MainWindow.ui.filtro2.setEnabled(False)
            self.MainWindow.ui.original.setEnabled(True)
            self.MainWindow.ui.filtro1.setEnabled(True)
            self.MainWindow.ui.filtro3.setEnabled(True)
        else:
            QtWidgets.QMessageBox.about(self.MainWindow, "Error","No hay imagen cargada")

    def filtro3(self):
        if(self.path!= ''):
            pixmap = QtGui.QPixmap(self.path)
            pixmap = pixmap.scaled(600, 400)
            self.MainWindow.ui.imagen_an.setPixmap(pixmap)
            self.MainWindow.ui.filtro3.setEnabled(False)
            self.MainWindow.ui.original.setEnabled(True)
            self.MainWindow.ui.filtro2.setEnabled(True)
            self.MainWindow.ui.filtro1.setEnabled(True)
        else:
            QtWidgets.QMessageBox.about(self.MainWindow, "Error","No hay imagen cargada")
                
## Se crea una funcion que cree un objeto aplicacion, entregandole argumentos de sistema.
def main(args):
    app = App(args)
    app.exec_()

## Se ejecuta
if __name__ == "__main__":
    main(sys.argv)
