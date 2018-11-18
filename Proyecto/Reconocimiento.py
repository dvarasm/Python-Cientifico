from PIL import Image
import numpy as np
import cv2
import scipy
from skimage import filters
import matplotlib.pyplot as plt
class Detector:
    def __init__(self,nombre_archivo):
        self.nombre_archivo = nombre_archivo
        # Cargamos la imagen
        self.original = cv2.imread(self.nombre_archivo)
        #self.original =cv2.medianBlur(self.original,5)
        self.gris = cv2.cvtColor(self.original, cv2.COLOR_BGR2GRAY)
        #cv2.imshow("original",self.original)
        self.mygris=None
        self.cont = 0
        self.trans2 = ''

    def transformacion1(self):    
        gris1=cv2.equalizeHist(self.gris)
        self.mygris=gris1
        #cv2.imshow("imagen",gris1)

        #ret,th1 = cv2.threshold(self.gris,127,255,cv2.THRESH_BINARY)
        #cv2.imshow("th1", th1)
        img_th1 = Image.fromarray(gris1)
        #cv2.waitKey(0)
        return img_th1
        
        
    def transformacion2(self):
        trans = ''
        trans = cv2.adaptiveThreshold(self.mygris,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
        cv2.THRESH_BINARY,11,2)
        #kernel = np.ones((3,3),np.uint8)
        #trans= cv2.morphologyEx(th3,cv2.MORPH_CLOSE,kernel)
        #img_th3 = Image.fromarray(th3)
        img_trans = Image.fromarray(trans)
        #img_trans.save('img_trans.png')
        #img_trans.show()
        #cv2.imshow("th3", th3)
        #cv2.imshow("trans", trans)
        #print type(cv2)
        #cv2.waitKey(0)
        self.trans2 = trans
        return img_trans        
        
        
    def bordes(self):
        trans = self.trans2
        # Convertimos a escala de grises
        #gris = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
 
        # Aplicar suavizado Gaussiano
        #gauss = cv2.GaussianBlur(gris, (5,5), 0)
 
        #cv2.imshow("suavizado", gauss)
 
        # Detectamos los bordes con Canny
        canny = cv2.Canny(self.gris, 10, 100,3)
        kernel = np.ones((3,3),np.uint8)
        canny= cv2.morphologyEx(canny,cv2.MORPH_CLOSE,kernel)
        
        #cv2.imshow("canny", canny)
 
        # Buscamos los contornos
        (_, contornos,_) = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        self.cont = format(len(contornos)-1)
        # Mostramos el numero de objetos por consola
        #print ("He encontrado {} objetos".format(len(contornos)-1))
        cv2.drawContours(self.original,contornos,-1,(0,0,255), 2)
        #cv2.imshow("contornos", self.original)
        img_cont = Image.fromarray(self.original)
        return img_cont

    def num_objetos(self):
        return int(self.cont)

        
