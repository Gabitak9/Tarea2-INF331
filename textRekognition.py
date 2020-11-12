#!/usr/bin/python3
#
# INF331 - TAREA2
# AWS Rekognition
# {Programa que determina si una imagen contiuene el texto contenido en otra imagen de control mediante el uso
# de AWS Rekognition}
#
# @gabitak9
#

import datetime
import boto3
import argparse
import sys
import re

from libs import libLogHandler as handler

FILENAME = 'logs/[LOG] '+str(datetime.datetime.now()).replace(":","-").replace(".","-")

# -------------------------------------------------------------------------------------

def getText(bucket,image, percentage):

    handler.getLog(4,FILENAME,image)

    try:
        client = boto3.client('rekognition')
        response = client.detect_text(Image={'S3Object':{'Bucket':bucket,'Name':image}})               
        detections = response['TextDetections']

        words = []

        for word in detections:

            line = word['DetectedText']
            confidence = word['Confidence']

            if confidence >= percentage:
                infoLog = 'Palabra {%s} aceptada con un %f %% de confianza'%(line,confidence)
                handler.getLog(6,FILENAME,infoLog)
                words.append(line)
            else:
                infoLog = 'Palabra {%s} rechazada por un %f %% de confianza'%(line,confidence)
                handler.getLog(6,FILENAME,infoLog)
        
        handler.getLog(5,FILENAME,None)

    except Exception as e:
        print(e)
        handler.getLog(3,FILENAME,str(e))
        print("[!] Cerrando programa ... ")
        sys.exit()

    return words

def getAnalysis(control, image):

    count = 0
    lenControl = len(control)

    control = [re.sub(r'[^(á-ú)*\w*@*]','',x).lower()  for x in control]
    image = [re.sub(r'[^(á-ú)*\w*@*]','',x).lower() for x in image]

    for word in control:
        if word not in image:
            count += 1
    
    if count == 0:
        print("[*] Se ha encontrado el texto completo\n{True}")
        infoLog = 'Resultado: {True}. 100% del texto encontrado'
    else:
        porcentageGet = 100. - ((100. / lenControl) * count)
        print("[*] No se ha encontrado el texto completo. Se ha encontrado un %d%% del texto.\n{False}"%(porcentageGet))
        infoLog = 'Resultado: {False}. %d%% del texto encontrado'%(porcentageGet)

    handler.getLog(7,FILENAME,infoLog)

    return None

# -------------------------------------------------------------------------------------

if __name__ == "__main__":

    #Init tool log
    handler.getLog(0,FILENAME,None)

    # Parse Args
    parser = argparse.ArgumentParser()
    required = parser.add_argument_group('required arguments')
    required.add_argument('-b','--bucket', help='Bucket Name', required=True)
    required.add_argument('-c','--control',help='Control Image', required=True)
    required.add_argument('-i','--image', help='Test Image', required=True)
    parser.add_argument('-p','--percentage', help='Confidence Percentage', type=int, default=97)
    args = parser.parse_args()
    params = "{bucket: %s, control: %s, image: %s, percentage: %s}"%(args.bucket,args.control,args.image,args.percentage)
    handler.getLog(2,FILENAME,params)

    print('============================================== INF331 - Tarea')
    print('                                                    @gsepulve\n')
    print('PARAMS:\t[-] Bucket Name: %s\n\t[-] Control Image: %s\n\t[-] Test Image: %s\n\t[-] Confidence Percentage: %s%%'%(args.bucket,args.control,args.image,args.percentage))
    print('\nGeting Text ...')

    # Get control image text
    controlText = getText(args.bucket,args.control, args.percentage)
    print('[*] Control Image Text: '+str(controlText))

    # Get image text
    imageText = getText(args.bucket, args.image, args.percentage)
    print('[*] Image Text: '+str(imageText))

    # Get Analysis
    print('\nGeting Analysis ...')
    getAnalysis(controlText, imageText)

    #Close tool log
    handler.getLog(1,FILENAME,None)