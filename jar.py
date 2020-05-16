import pyttsx3
import datetime #pip install datetime
import speech_recognition as sr #pip install speechRecognition
import wikipedia#pip install wikipedia
import webbrowser
import smtplib 



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[0].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("GOOD morning")
    elif hour>=12 and hour<=18:
        speak("GOOD mafternoon")
    else:
        speak("GOOD Evening")
speak("hey hai..this is sumanth's assistance ..tell how may i help you")        

def takeCammand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        #r.pause_threshold= 1
        audio=r.listen(source)
    try:
        print("Recognising..")
        quary = r.recognize_google(audio,language='en-in')
        print(f"user said: {quary}\n")
    except Exception as e:
        #print(e)
        print("say again please..")
        return "None"
    return quary

def sendmail(to,connect):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('your email id','mailidpassword') #make sure that you less secure apps should be on..
    server.sendmail('your mail id',to,connect)
    server.close



if __name__ == '__main__':
    wishme()
    while True:
        quary=takeCammand().lower()
        if 'wikipedia' in quary:
           speak("searching wikipedia...pease wait")
           quary=quary.replace("wikipedia","")
           results=wikipedia.summary(quary,sentences=2)     
           speak("according to wikipedia")
           print(results)
           speak(results)
        elif  'open youtube' in quary:
           webbrowser.open("youtube.com")

        elif 'open google' in quary:
               webbrowser.open("google.com")
        
        elif 'what is the time' in quary:
           strTime= datetime.datetime.now().strftime("%H:%M:%S")
           speak(f"the time is {strTime}")

        elif 'email to sumanth' in quary:
            try:
                speak("what shoud i say")
                connect= takeCammand()
                to = "prabhusumantha77@gmail.com"
                sendmail(to,connect)
                speak("email has been sent")
            except Exception as e:
                #print(e)
                speak("not able to send")
                #you can add as many as cammands in order to perform the task like playing music,open newtab.
