import speech_recognition as sr
import webbrowser
import time
import playsound
import os
import random
from gtts import gTTS

from time import ctime

r = sr.Recognizer()

def grabar_audio(ask=False): 
    with sr.Microphone() as source:
        if ask:
            print(ask)
        audio = r.listen(source)
        voz_data = ''

        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            print('Lo siento, no capto lo que dices')
        except sr.RequestError:
            print('Lo siento, mi servicio de reconocimiento no está funcionando')
        return voz_data


def diana_dice(audio_string):
    tts = gTTS(text=audio_string, lang='es')
    r = random.randint(1, 10000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove()


def respuesta(voz_data):
    if 'Cuál es tu nombre?' in voz_data:
        print('Mi nombre es Diana')
    if 'Qué hora es?' in voz_data:
        print(ctime())
    if 'busca' in voz_data:
        busca = grabar_audio('¿Qué quieres buscar?')
        url = 'https://google.com/search?q=' + busca
        webbrowser.get().open(url)
        print('Esto es lo que encontré '+busca)
    if 'busca lugar' in voz_data:
        lugar = grabar_audio('¿Qué lugar?')
        url = 'https://google.nl/maps/place/' + lugar + '/&amp;'
        webbrowser.get().open(url)
        print('Se encuentra en: '+lugar)
    if 'terminamos' in voz_data:
        exit()


time.sleep(1)
print('¡Hola! ¿Cómo puedo ayudarte?')

while 1:
    voz_data = grabar_audio()
    respuesta(voz_data)


    