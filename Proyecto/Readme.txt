LEER DETENIDAMENTE
* Esta es la primera parte del proyecto semestral, realizada en python 3

Para ejecutar este programa ejecute MotorDetector.py

1. Se abrira una ventana de interfaz, donde se le pedira cargar una imagen, por favor seleccione el boton cargar imagen, y seleccione una imagen de la carpeta entregada. 
2. Luego seleccione el boton iniciar deteccion, con esto se le aplicara los filtros establecidos a la imagen para su posterior reconocimiento
  a) filtro 1, rgb
  b) filtro 2, una imagen tipo boceto
  c) filtro 3, deteccion de bordes con canny, mas posterior eliminacion de ruido negro

3. Se abrira un mensaje que indica cuantos objetos fueron encontrados, cierre el mensajes y dirijase a los botones filtro para ver la aplicacion de cada uno de ellos 
 
4. finalmente quite la imagen para una nueva deteccion o cierre la ventana


Importante:

El reconocimiento establecido en dicha iteracion funciona al 99.9% para objetos que estan separados, no asi para aquellos que estan amontonados entre si , donde falla completamente en la deteccion de bordes y cantidad de objetos encontrados 

El programa Entrenador.py (en proceso, fase beta) , se encarga de reconocer el tipo de manzana dado lo entregado anteriormente, pero aun no esta implementado como tal
