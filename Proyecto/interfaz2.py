from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic
import sys

class App(QtWidgets.QApplication):
    def __init__(self, *args):
        QtWidgets.QApplication.__init__(self, *args)
        self.MainWindow = QtWidgets.QMainWindow()
        self.MainWindow.ui = uic.loadUi('interfaz.ui')#carga la interfaz
        self.MainWindow.ui.setWindowTitle("Detector")#nombre de la ventana
        self.MainWindow.ui.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint|QtCore.Qt.WindowCloseButtonHint)#para no redimensionar
        self.MainWindow.ui.show()
                
        #self.connect(self.MainWindow.ui.saludar, QtCore.SIGNAL('clicked()'), self.saludar)#ejemplo pyqt4
        #self.MainWindow.ui.saludar.clicked.connect(self.saludar)#ejemplo pyqt5
        
        #botones
        self.MainWindow.ui.Iniciar.clicked.connect(self.funcion_b1)#listener del boton iniciar
        self.MainWindow.ui.Detener.clicked.connect(self.funcion_b2)#listener del boton parar

        #imagen
        pixmap = QtGui.QPixmap('m.png')#carga la imagen
        pixmap = pixmap.scaled(600, 400)#redimensiona la imagen
        self.MainWindow.ui.imagen_an.setPixmap(pixmap)#agrega imagen
        
        self.sosp = 0 #elemento a obtener 
        
    # metodos

    def funcion_b1(self):#funcion del boton iniciar
        print ("Iniciar")
        self.sosp += 1 #elemento variable
        self.MainWindow.ui.LCDnumber.display(self.sosp)#cambia el numero LCD
        pixmap = QtGui.QPixmap('fuji.png')#carga la imagen
        pixmap = pixmap.scaled(600, 400)#redmensiona la imagen
        self.MainWindow.ui.imagen_an.setPixmap(pixmap)#cambia la imagen


    def funcion_b2(self):#funcion del boton parar
        print ("Parar")
        pixmap = QtGui.QPixmap('m.png')#carga la imagen
        pixmap = pixmap.scaled(600, 400)#redmensiona la imagen
        self.MainWindow.ui.imagen_an.setPixmap(pixmap)#cambia la imagen
        if(self.sosp>0):
            self.sosp -= 1 #elemento variable
        self.MainWindow.ui.LCDnumber.display(self.sosp)#cambia el numero LCD
                    
## Se crea una funcion que cree un objeto aplicacion, entregandole argumentos de sistema.
def main(args):
    app = App(args)
    app.exec_()

## Se ejecuta
if __name__ == "__main__":
    main(sys.argv)
