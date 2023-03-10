import pyttsx3
import speech_recognition as ussr
import pyjokes
import datetime
from datetime import date
import pywhatkit as pwk
import wikipedia as ggwp
#Variables
listener = ussr.Recognizer()
engine = pyttsx3.init()
voice = engine.getProperty("voices")
engine.setProperty("voice",voice[1].id)
engine.setProperty("rate", 147)
mic = ussr.Microphone()
#Make Petruha Talk
def Talk(text):
    engine.say(text)
    engine.runAndWait()
    print(text)
#Talk("Nice to meet you, young Sir. How a u doin' this beautiful noight?")
#Take Voice command
def cmnd():
    try:
        with mic as source:
            print("c'mon, talk to me...")
            GolosSixtyPlus = listener.listen(source)#Listen to microphone
            command = listener.recognize_google(GolosSixtyPlus)#Recognize Peach
            command = command.lower()
            if "petruha" in command:
                #Delete Petruha from command so command won't break
                command = command.replace("petruha","")
                print(command)
            return command
    except:
        pass

def petruha():
    command = cmnd()
    if command is None:
        petruha()
    else:
        if "pregnant" in command:
            Talk("no, I don't think so")

        elif "time" in command:
            Talk(datetime.datetime.now().strftime("%I:%M %p"))
        
        elif "date" in command:
            Talk(date.today())

        elif "where are you from" in command:
            Talk("from  Soviet Union. So,use, nyrushi me, oh wait")

        elif "what up" in command:
            Talk("why are you asking")

        elif "life" in command:
            Talk("I don't no, who you think I am")

        elif "play" in command:
            video = command.replace("play", "")
            Talk("This "+str(video)+" is for you")
            pwk.playonyt(video)

        elif "joke" in command:
            Talk(pyjokes.get_joke())
        
        elif "what is" in command:
            thing = command.replace("what is", "")
            try:
                engine.setProperty("rate", 170)
                Talk(ggwp.summary(thing,2))
            except:
                Talk("aaah, stupid wikipedia, can not find shit, I told you to use Yandex")
            engine.setProperty("rate", 147)

        elif "who is" in command:
            thing = command.replace("who is", "")
            try:
                engine.setProperty("rate", 170)
                Talk(ggwp.summary(thing,2))
            except:
                Talk("aaah, dumb wikipedia, can not find shit, I told you to use Yandex")
            engine.setProperty("rate", 147)

        else:
            Talk("formulate the question properly, bitch")




while True:
    petruha()

