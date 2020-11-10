# TAREA 2 - INF331
##### por Gabriela Sepúlveda

### ACERCA DE textRekognition
**textRekognition** es un programa que surge en el marco de una tarea para el ramo **INF331-Pruebas de Software**, y que determina si el texto contenido en una *imagen de control* se encuetra también en una 'imagen de prueba'. Para esto hace uso de [AWS Rekognition](https://aws.amazon.com/es/rekognition/). Este programa fue desarrollado en `Python 3.8`

### PRIMEROS PASOS
Para descargar **textRekognition** utilice el comando`git`:
```
git clone https://github.com/Gabitak9/Tarea2-INF331.git
```

Realice la instalación de los módulos necesarios con el siguiente comando:
```
pip3 -r install requeriments.txt
```

### USO DEL PROGRAMA
Puede consultar el manual de uso del programa con el comando `-h`:
```
$ python3 textRekognition.py -h
usage: textRekognition.py [-h] -b BUCKET -c CONTROL -i IMAGE -p PERCENTAGE

optional arguments:
  -h, --help            show this help message and exit
  -p PERCENTAGE, --percentage PERCENTAGE
                        Confidence Percentage

required arguments:
  -b BUCKET, --bucket BUCKET
                        Bucket Name
  -c CONTROL, --control CONTROL
                        Control Image
  -i IMAGE, --image IMAGE
                        Test Image
```

Por tanto el modo de uso queda determinado por el siguiente comando:
```
$ python3 textRekognition.py [-h] -b BUCKET -c CONTROL -i IMAGE -p PERCENTAGE
```
donde,
- BUCKET: Es el nombre del bucket S3 que contiene sus imágenes
- CONTROL: Es el nombre de la imagen de control
- IMAGE: Es el nombre de la imagen para realizar el test
- PERCENTAGE: Es el porcentaje de confianza que desea determinar para la detección de palabras. Su valor por defecto es de 97%

### RESULTADOS
Por consola se mostrará e resultado del análisis que incluirá el porcentaje de detección del texto dentro de la imagen de prueba. Para mayores detalles puede consultar el archivo de `logs` generado durante la ejecución del programa. Se creará un archivo por cada ejecución de éste (El nombre será la fecha y hora de ejecución).
