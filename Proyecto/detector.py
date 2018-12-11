from imageai.Detection import ObjectDetection
import os
from time import time

start_time = time()
execution_path = os.getcwd()

detector = ObjectDetection()
detector.setModelTypeAsRetinaNet()
detector.setModelPath( os.path.join(execution_path , "resnet50_coco_best_v2.0.1.h5"))
detector.loadModel()
detections = detector.detectObjectsFromImage(input_image=os.path.join(execution_path , "0.jpg"), output_image_path=os.path.join(execution_path , "imagenew.jpg"))

elapsed_time = time() - start_time
print("Elapsed time: %0.10f seconds." % elapsed_time)

print("Numero de objetos:",len(detections))

for eachObject in detections:
    if(eachObject["name"] == 'apple'):
        print(eachObject["name"] , " : " , eachObject["percentage_probability"] )
    else:
        print('Objeto sospechoso',eachObject["name"])