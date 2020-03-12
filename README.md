# Yoga Pose Detector

![alt text](https://github.com/meryreddoor/yogagame_/blob/primeraRama/src/templates/img/paisaje.png)

El yoga te enseña cómo cultivar tu energía mental y física. Puedes hacer clases tan cortas como de cinco minutos para recargar tu energía cuando lo necesites.
Esta App te permitirá comprobar si tu postura es la adecuada ¡No necesitarás profesor!.

Yoga Pose Destector es una app  de machine learning desarrollado en `Python` con el `el modelo CNN (Convolutional neural network)` de `Keras` para ayudar a las personas con poco tiempo a mejorar sus posturas de yoga.

La idea parte de un dataset de `GitHub` con más de un 1GB en imágenes donde se muestran diferentes posturas de yoga. 
`Yoga Pose Detector` es capaz de sacar el `Accuracy` de una postura concreta de yoga.

## Preparación de las imágenes

Organicé el dataset de imágenes, tratando las imágenes con las librerías `Numpy` y `OpenCV` para que todas tuvieran el formato adecuado para su procesamiento y entrenamiento en el modelo CNN.

## Entrenamiento 

`Convolutional Neural Network Model` fue la red neuronal de clasificación de `Keras` que mejores métricas obtuvo a la hora de hacer la predicción de los tumores. Utilicé `GridSearchCV` para obtener los mejores parámetros con los que entrenar el algoritmo, con los que el modelo consigue un accuracy de más del 80%.

## API
Finalmente integré el modelo predictivo en una api desarrollada con `Flask` en entorno local, que permite cargar una imagen y devuelve el diagnóstico de dicha imagen, confirmando si el tumor es maligno o si es benigno. Esta es la interfaz de BCD: 

![alt text](https://github.com/cprietosegura/Breast-Cancer-Detector-Model/blob/master/notebooks/api_bcd.jpg)

Una vez cargada la imagen, se envía la consulta y devuelve el diagnóstico:

![alt text](https://github.com/cprietosegura/Breast-Cancer-Detector-Model/blob/master/notebooks/api_bcd_diagnosis.jpg)

## Fuentes

- [Dataset](https://github.com/DhruvJawalkar/yoga-poses-dataset)
