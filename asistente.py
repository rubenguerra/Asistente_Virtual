# Asistente virtual que provee fechas, saluda y da ciertas informaciones

# BIBLIOTECAS

import speech_recognition as sr
import os
from gtts import gTTS
import datetime
import warnings
import calendar
import random
import wikipedia

# Ignorar cualquier mensaje de advertencia
warnings.filterwarnings('ignore')

# Graba audio y lo retorna en forma de string


def recordAudio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Diga algo !')
        audio = r.listen(source)

    data = ""
    try:
        data = r.recognize_google(audio)
        print('Dijo: '+data)
    except sr.UnknownValueError:
        print('No lo puedo entender')
    except sr.RequestError as e:
        print('Request results from Google Speech Recognition service error: '+e)

    return data


recordAudio()

# Función para obtener respuestas del asistente


def assistantResponse(text):
    print(text)

    # Convierte el texto en palabras
    myobj = gTTS(text=text, lang='es', slow=False)

    # Guarda el audio
    myobj.save('assistant_response.mp3')

    # Reproduce el archivo convertido
    os.system('start assistant_response.mp3')

# #text = 'hola, mi nombre es Dayana!'

# assistantResponse()

# Función para chequear palabras y frases de aviso

def wakeWord(text):
    ACTIVA_WORDS = ['hey computer', 'okay computer']
    text = text.lower()  # Convierte el texto a minúsculas

    # Chequea si la orden contiene palabras de activación
    for frase in ACTIVA_WORDS:
        if frase in text:
            return True

    return False


# Función para obtner las fechas
def getDate():
    now = datetime.datetime.now()
    my_date = datetime.datetime.today()
    weekday = calendar.day_name[my_date.weekday()]
    monthNum = now.month
    dayNum = now.day

    # Lista de meses
    month_names = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto',
                   'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
    # Lista de numeros ordinales
    ordinalNumbers = ['1', '2', '3', '4', '5',
                      '6', '7', '8', '9', '10',
                      '11', '12', '13', '14', '15',
                      '16', '17', '18', '19', '20',
                      '21', '22', '23', '24', '25',
                      '26', '27', '28', '29', '30', '31']

    return 'Hoy es ' + weekday + ' ' + ordinalNumbers[dayNum - 1] + ' de ' + month_names[monthNum - 1]

# Función que regresa saludos al azar


def greeting(text):
    SALUDOS_ENTRADAS = ['hola', 'hi', 'hey', '¿como va?', 'hello']

    SALUDOS_RESPUESTAS = ['hola', 'hi', 'todo bien',
                          'fino', 'todo fino', 'buen día']

    # Respondiendo al saludo
    for word in text.split():
        if word.lower() in SALUDOS_ENTRADAS:
            return random.choice(SALUDOS_RESPUESTAS) + '.'

    # si no hay saludo que regrese una cadena vacía
    return ''

# Función para pedir información


def getPerson(text):
    wordList = text.split()  # Separa el texto en una lista de palabras

    for i in range(0, len(wordList)):
        if i + 3 <= len(wordList) - 1 and wordList[i].lower() == 'who' and wordList[i+1].lower() == 'is':
            return wordList[i+2] + ' ' + wordList[i+3]


while True:
    # Graba el audio
    text = 'Hola, quien es Lebron James?'
    response = ''  # Sin respuesta para unir a la respuesta del asistente

    # Chequea la palabra de alerta
    if (wakeWord(text)) == True:
        # Chequea el saludo del usuario
        response = response + greeting(text)
        # Chequea si el usuario dice algo sobre la fecha
        if('fecha' in text):
            get_date = getDate()
            response = response + ' ' + get_date

        # Chequea si el usuario usa alguna palabra sobre el tiempo
        if ('tiempo' in text):
            now = datetime.datetime.now()
            meridiem = ''
            if now.hour >= 12:
                meridiem = 'p.m'
                hour = now.hour - 12
            else:
                meridiem = 'a.m'

            response = response + 'Son las ' + \
                str(hour) + ':' + str(now.minute)+' ' + meridiem+'.'

        # Chequea si el usuario dice '¿Quién es?
        if ('quien es?' in text):
            person = getPerson(text)
            wiki = wikipedia.summary(person, sentences=2)
            response = response + ' ' + wiki

        assistantResponse(response)
