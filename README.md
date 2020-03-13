# Yoga Pose Detector

![alt text](https://github.com/meryreddoor/yogagame_/blob/primeraRama/src/templates/img/paisaje.png)

Yoga Pose Detector es una app  de `deep learning` desarrollado en `Python` con un ` modelo CNN (Convolutional Neural network)` de `Keras` para ayudar a las personas con poco tiempo a mejorar sus posturas de yoga.

La idea parte de un dataset de `GitHub` con más de un 1GB en imágenes donde se muestran diferentes posturas de yoga.   
`Yoga Pose Detector` es capaz de sacar el `Accuracy` de una postura concreta de yoga.

## Preparación de las imágenes

Organicé el dataset de imágenes, tratando las imágenes con las librerías `Numpy`, `OpenCV` y `Pandas` para que todas tuvieran el formato adecuado para su procesamiento y entrenamiento en el modelo CNN.

## Entrenamiento 

`Convolutional Neural Network Model` fue la red neuronal de clasificación de `Keras` que mejores métricas obtuvo a la hora de hacer la predicción en las poses. Utilicé los siguientes capas:
 
1. `Conv2D` 
2. `MaxPooling2D`
3. `Dropout`
4. `Flatten`

La clase que utilicé fue `Sequential` y usé `Flatten` para aplanar los datos.

Con lo parámetros comentados anteriormente, he obtenido los mejores resultados a la hora de entrenar el modelo, ya que se consigue un accuracy de más del 90%.

## API
Finalmente integré el modelo predictivo en una api desarrollada con `Flask` en entorno local, que permite cargar una imagen y devuelve una predicción y el accuracy de dicha imagen.

### Demo

Primero, tenemos que hacer una foto, recortarla y subirla a la App:

![alt text](https://github.com/meryreddoor/yogagame_/blob/primeraRama/src/templates/img/primera_img.png)

Una vez cargada la imagen, se envía la consulta y devuelve el diagnóstico:

![alt text](https://github.com/meryreddoor/yogagame_/blob/primeraRama/src/templates/img/segunda_img_web.png)

## Fuentes

A continuación se muestran las fuentes que se han utilizado durante el trabajo:

- [Dataset](https://github.com/DhruvJawalkar/yoga-poses-dataset) - Dataset usado para entrenar el modelo.

- [Artículo sobre CNN](https://towardsdatascience.com/building-a-convolutional-neural-network-cnn-in-keras-329fbbadc5f5) - Artículo sobre CNN

- [Predicción en Yoga](https://github.com/amarchenkova/yoga-pose-CNN) -  Predicción en GitHub de poses de yoga usando el modelo CNN
