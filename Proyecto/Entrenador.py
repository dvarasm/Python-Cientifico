from reverend.thomas import Bayes
import cv2
import numpy as np
#tratar de buscar la manzana por color
original = cv2.imread('13.png')
hsv = cv2.cvtColor(original, cv2.COLOR_BGR2HSV)

guesser =None
if guesser is None:
	guesser=Bayes()

verde_bajos = np.array([49,50,50])
verde_altos = np.array([107, 255, 255])
#entrenamiento de las caracteristicas de la manzana que quiero detectar 
guesser.train('manzana verde', 'verde')
guesser.train('manzana verde','20cm de diametro')
guesser.train('manzana amarilla','amarillo')
guesser.train('manzana roja', 'rojo')
#buscar verde en la imagen
mascara_verde = cv2.inRange(hsv, verde_bajos, verde_altos)
cv2.imshow("manzana verde", mascara_verde)
cv2.waitKey(0)
#buscar la probabilidad de que aparezca una verde
print guesser.guess('verde')