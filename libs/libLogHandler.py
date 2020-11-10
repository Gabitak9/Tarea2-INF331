#!/usr/bin/python3
#
# libLogHandler es un modulo que contiene las funciones para la generación de logs
#

import time
import datetime

#---------------------------------------------------------------------------------

def initTool(date,filename,info):
    """Generación de entrada de inicialización del programa
    Args:
        date (timestamp): fecha y hora
        info (list): informacion requerida
        filename (string): nombre del archivo de logs
    Returns:
        None
    """
    newLog = str(date)+' >> Inicialización de Programa\n'

    with open(filename, 'a') as file:
       file.write(newLog)

    return None

def endTool(date,filename,info):
    """Generación de entrada de término del programa
    Args:
        date (timestamp): fecha y hora
        info (list): informacion requerida
        filename (string): nombre del archivo de logs
    Returns:
        None
    """
    newLog = str(date)+' >> Ejecución sin errores terminada\n'

    with open(filename, 'a') as file:
       file.write(newLog)

    return None

def setParams(date,filename,info):
    """Generación de entrada de seteo de parámetros
    Args:
        date (timestamp): fecha y hora
        info (list): informacion requerida
        filename (string): nombre del archivo de logs
    Returns:
        None
    """
    newLog = '\t|---'+str(date)+' >> Parámetros Ingresados: '+info+'\n'

    with open(filename, 'a') as file:
       file.write(newLog)

    return None

def awsError(date,filename,info):
    """Generación de entrada de errores desde el servicio de aws
    Args:
        date (timestamp): fecha y hora
        info (list): informacion requerida
        filename (string): nombre del archivo de logs
    Returns:
        None
    """
    newLog = '\t\t|---'+str(date)+' >> Error desde el cliente AWS: '+info+'\n\t\t|--- CERRANDO PROGRAMA\n'

    with open(filename, 'a') as file:
       file.write(newLog)

    return None

def getText(date,filename,info):
    """Generación de entrada de obtención de texto de imagen
    Args:
        date (timestamp): fecha y hora
        info (list): informacion requerida
        filename (string): nombre del archivo de logs
    Returns:
        None
    """
    newLog = '\t|---'+str(date)+' >> Obteniendo texto de: '+info+'\n'

    with open(filename, 'a') as file:
       file.write(newLog)

    return None

def doneText(date,filename,info):
    """Generación de entrada de obtención de texto de imagen
    Args:
        date (timestamp): fecha y hora
        info (list): informacion requerida
        filename (string): nombre del archivo de logs
    Returns:
        None
    """
    newLog = '\t\t|---'+str(date)+' Obtención de palabras realizada\n'

    with open(filename, 'a') as file:
       file.write(newLog)

    return None

def getWord(date,filename,info):
    """Generación de entrada de obtención de texto de imagen
    Args:
        date (timestamp): fecha y hora
        info (list): informacion requerida
        filename (string): nombre del archivo de logs
    Returns:
        None
    """
    newLog = '\t\t|---'+str(date)+' '+info+'\n'

    with open(filename, 'a') as file:
       file.write(newLog)

    return None

def analysisResult(date,filename,info):
    """Generación de entrada de obtención de texto de imagen
    Args:
        date (timestamp): fecha y hora
        info (list): informacion requerida
        filename (string): nombre del archivo de logs
    Returns:
        None
    """
    newLog = '\t|---'+str(date)+' Realizando análisis\n\t\t|--- '+info+'\n'

    with open(filename, 'a') as file:
       file.write(newLog)

    return None

#---------------------------------------------------------------------------------

# Switcher para introducir logs
switcher = {
        0: initTool,
        1: endTool,
        2: setParams,
        3: awsError,
        4: getText,
        5: doneText,
        6: getWord,
        7: analysisResult,
    }

#---------------------------------------------------------------------------------

def getLog(code, filename, info):
    """getLog() es un handler que recibe desde el programa principal el código
    e información que necesita para generar una entrada en el archivo de logs
    Args:
        code (int): código identidicador del log
        filename (string): nombre del archivo donde registrar el log
        info (list): listado con información util para la generación de log
    Returns:
        None
    """    

    date = datetime.datetime.now()
    func = switcher.get(code)
    func(date,filename,info)
    
    return None