import speech_recognition as sr
import time
import os

mic = sr.Microphone()
r = sr.Recognizer()

def callback(recognizer, audio):
    try:
        ses = r.recognize_google(audio, language='tr-tr')
        ses = ses.lower()
        youtube = ses.find('youtube')
        google = ses.find('google')
        yandex = ses.find('yandex')
        ses = ses.replace("youtube ", "")
        ses = ses.replace("google ", "")
        ses = ses.replace("yandex ", "")
        ses = ses.replace(" ", "+")
        if(youtube == 0):
            komut = "opera https://www.youtube.com/results?search_query=" + ses
            os.system(komut)
        elif(google == 0):

            komut = "opera https://www.google.com/search?q=" + ses
            os.system(komut)
        elif(yandex ==0):
            komut = "opera https://yandex.com.tr/search/?text="+ses
            os.system(komut)


    except sr.WaitTimeoutError:
        print("")

    except sr.UnknownValueError:
        print("")

    except sr.RequestError:
        print("")

r.listen_in_background(mic, callback)
while True: time.sleep(0.1)
