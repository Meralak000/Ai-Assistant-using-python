
import speech_recognition as sr
import webbrowser 
import pyttsx3



recognizer = sr.Recognizer() 
engine = pyttsx3.init()




def speak(text):
    engine.say(text)
    engine.runAndWait()
    

if __name__=="__main__":
    speak('initializing symbi......')
    while True:
#listen for the wake word symbi
# this code is used so that audio is obtained from mic
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source)
        

#recognize speech using google
        try:
            command = r.recognize_sphinx(audio)
            print(command)
        except sr.UnknownValueError:
            print("Sphinx could not understand audio")
        except sr.RequestError as e:
            print("Sphinx error; {0}".format(e))
