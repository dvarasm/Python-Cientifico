import numpy as np
import cv2
 
# Cargamos la imagen
original = cv2.imread("manzana5.jpg")
cv2.imshow("original", original)
#original =cv2.medianBlur(original,5)
gris = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
#ret,th1 = cv2.threshold(gris,127,255,cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(gris,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
            cv2.THRESH_BINARY,11,2)
th3 = cv2.adaptiveThreshold(gris,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,11,2)
#Morphologic, para unir contornos incompletos

kernel = np.ones((3,3),np.uint8)

trans= cv2.morphologyEx(th3,cv2.MORPH_CLOSE,kernel)
trans= cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))

#cv2.imshow("th1", th1)
cv2.imshow("th2", th2)
cv2.imshow("th3", th3)
cv2.imshow("trans", trans)

# Convertimos a escala de grises
#gris = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
 
# Aplicar suavizado Gaussiano
#gauss = cv2.GaussianBlur(gris, (5,5), 0)
 
#cv2.imshow("suavizado", gauss)
 
# Detectamos los bordes con Canny
canny = cv2.Canny(th3, 50, 150)

cv2.imshow("canny", canny)
dilated = cv2.dilate(canny, trans)

cv2.imshow("dilatado",dilated) 
# Buscamos los contornos
( contornos,_) = cv2.findContours(canny.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
 
# Mostramos el numero de monedas por consola
print "He encontrado {} objetos".format(len(contornos))
 
cv2.drawContours(original,contornos,-1,(0,0,255), 2)
cv2.imshow("contornos", original)
 
cv2.waitKey(0)
