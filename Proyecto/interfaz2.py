from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic
import sys

class App(QtWidgets.QApplication):
    def __init__(self, *args):
        QtWidgets.QApplication.__init__(self, *args)
        self.MainWindow = QtWidgets.QMainWindow()
        self.MainWindow.ui = uic.loadUi('interfaz.ui')
        self.MainWindow.ui.setWindowTitle("Detector")
        self.MainWindow.ui.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)#para no redimensionar
        self.MainWindow.ui.show()
                
        #ACA van los widgets para las funciones
        #self.connect(self.MainWindow.ui.saludar, QtCore.SIGNAL('clicked()'), self.saludar)#pyqt4
        #self.MainWindow.ui.saludar.clicked.connect(self.saludar)#pyqt5
        self.MainWindow.ui.Iniciar.clicked.connect(self.funcion_b1)
        self.MainWindow.ui.Detener.clicked.connect(self.funcion_b2)

        
        pixmap = QtGui.QPixmap('m.png')
        pixmap = pixmap.scaled(600, 400)
        self.MainWindow.ui.imagen_an.setPixmap(pixmap)

        
    # metodos

    def funcion_b1(self):#funcion del boton 1
        print ("Iniciar")
        sosp = 1 #elemento variable
        self.MainWindow.ui.LCDnumber.display(sosp)
        pixmap = QtGui.QPixmap('fuji.png')
        pixmap = pixmap.scaled(600, 400)
        self.MainWindow.ui.imagen_an.setPixmap(pixmap)


    def funcion_b2(self):#funcion del boton 2
        print ("Parar")
        pixmap = QtGui.QPixmap('m.png')
        pixmap = pixmap.scaled(600, 400)
        self.MainWindow.ui.imagen_an.setPixmap(pixmap)
        sosp = 0 
        self.MainWindow.ui.LCDnumber.display(sosp)
                    
## Se crea una funcion que cree un objeto aplicacion, entregandole argumentos de sistema.
def main(args):
    app = App(args)
    app.exec_()

## Se ejecuta
if __name__ == "__main__":
    main(sys.argv)
