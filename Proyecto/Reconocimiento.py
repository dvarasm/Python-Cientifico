from PIL import Image
import numpy as np
import cv2
import scipy
#from skimage import filters
import matplotlib.pyplot as plt
from imageai.Detection import ObjectDetection
import os
class Detector:
    def __init__(self,nombre_archivo):
        self.nombre_archivo = nombre_archivo
        # Cargamos la imagen
        self.original = cv2.imread(self.nombre_archivo)
        #transformamos a escala de grises
        self.gris = cv2.cvtColor(self.original, cv2.COLOR_BGR2GRAY)
        #variables que se usan mas adelante
        self.mygris=None
        self.cont = 0
        self.trans2 = ''
        self.det = None
        self. obj_sosp = False
        
    def detec(self):
        execution_path = os.getcwd()
        detector = ObjectDetection()
        detector.setModelTypeAsRetinaNet()
        detector.setModelPath( os.path.join(execution_path , "resnet50_coco_best_v2.0.1.h5"))
        detector.loadModel()
        detections = detector.detectObjectsFromImage(input_image=os.path.join(execution_path , self.nombre_archivo), output_image_path=os.path.join(execution_path , "imagenew.jpg"))
        self.det = detections
        for eachObject in detections:
            if(eachObject["name"] != 'apple'):
                self.obj_sosp = True

    def transformacion1(self):    
        #transformacion a rgb
        gris1=cv2.cvtColor(self.original, cv2.COLOR_BGR2RGB)
       
        #transformacion a otra escala de grises para cuerpos que estan muy juntos
        #gris1=cv2.equalizeHist(self.gris)
        #hacerla igual a otra imagen para poder llamarla desde afuera de la funcion 
        self.mygris=gris1

        #muestra la imagen 
        #cv2.imshow("imagen",gris1) 
        #convierte a imagen el numpy.ndarray que se creo de la transformacion
        img_th1 = Image.fromarray(gris1)
        #retorna la imagen para la interfaz    
        return img_th1
        
        
    def transformacion2(self):
        #transforma la imagen en una especie de boceto

        trans = cv2.adaptiveThreshold(self.gris,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
        cv2.THRESH_BINARY,11,2)
        #convierte a imagen el numpy.ndarray que se creo de la transformacion
        img_trans = Image.fromarray(trans)
        #se iguala el numpy.ndarray obtenido a una global, para llamarla desde otra funcion
        self.trans2 = trans
        #se retorna la imagen para que la interfaz la muestre
        return img_trans        
        
        
    def bordes(self):
      
        # Detectamos los bordes con Canny, en la imagen de escala de grises entregada al principio
        canny = cv2.Canny(self.gris, 10, 100,3)
        #eliminamos el ruido , o manchas negras de mas en la foto 
        kernel = np.ones((3,3),np.uint8)
        canny= cv2.morphologyEx(canny,cv2.MORPH_CLOSE,kernel)
 
        # Buscamos los contorno
        (_,contornos,_) = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        self.cont = format(len(contornos))
        # Mostramos el numero de objetos por consola
        #print ("He encontrado {} objetos".format(len(contornos)))
        #dibujamos los contornos encontrados en la imagen original
        cv2.drawContours(self.original,contornos,-1,(0,0,255), 2)
        #cv2.imshow("contornos", self.original)
        #convierte a imagen el numpy.ndarray
        img_cont = Image.fromarray(self.original)
        #se retorna la imagen para la interfaz
        return img_cont

    def num_objetos(self):
        #retorna el numero de objetos encontrados por las transformaciones correspondientes 
        return int(len(self.det))

    def objetos_sosp(self):
        if(self.obj_sosp == True):
            return True
        else:
            return False

        
