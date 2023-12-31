import pyttsx3
import speech_recognition as sr
import os
import random
from requests import get
import webbrowser
import wikipedia
import pywhatkit as kit
import sys
import time
import pyautogui
import PyPDF2
import operator
from pywikihow import search_wikihow
import pdfreader
from wish import wish
from internet import inetrnetSpeed
from battery import battery
from temperature import temprature
from HowToDo import HowToDo

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takecommand():
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=10,phrase_time_limit=5)

    try:
        print("Recognizing")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said : {query}")

    except Exception as e:
        # print(e)

        print("Please Say that Again ..........!")    
        return "None"
    query = query.lower()
    # query_sys = query_sys.lower()
    return query



##################################### SYSTEM #####################################
def sys():
    speak("sir, now i am in system")
    while True:
        cm = takecommand().lower()
        
        if 'open notepad' in cm:
            npath = "C:\\Windows\\notepad.exe"
            speak("opening notepad")
            os.startfile(npath)

        elif 'close notepad' in cm:
            speak("okey sir, closing notepad")
            os.system("taskkill /f /im notepad.exe")

        # elif "open chrome" in cm:
        #     from chromeauto import ChromeAuto
        #     ChromeAuto(cm)


        elif 'close chrome' in cm:
            os.system("taskkill /f /im chrome.exe")



        elif "shut down the system" in cm:
            os.system("shutdown /s /t 5")


        elif "restart the system" in cm:
            os.system("shutdown /r /t 5")

        elif "Lock the system" in cm:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")



        elif "open command prompt" in cm or "open cmd" in cm:
            os.system("start cmd")

        elif "close command prompt" in cm  or "close cmd" in cm:
            os.system("taskkill /f /im cmd.exe")


        # elif "refresh" in cm:
        #     pyautogui.moveTo(1551,551, 2)
        #     pyautogui.click(x=1551, y=551, clicks=1, interval=0, button='right')
        #     pyautogui.moveTo(1620,667, 1)
        #     pyautogui.click(x=1620, y=667, clicks=1, interval=0, button='left')




        # having issue
        # elif 'read pdf' in cm:
        #     pdf_read()


# location finder having some issue


##################################### FOR LOCATION #####################################
        # elif "where i am" in cm or "where we are" in cm:
        #     speak("wait sir , let me check")
        #     try:
        #         ipadd = requests.get('https://api.ipify.org').text
        #         print(ipadd)
        #         url = 'https://get.geojs.io/v1/ip/geo'+ipadd+'.json'
        #         geo_requests = requests.get(url)
        #         geo_data = geo_requests.json()
        #         city = geo_data["city"]
        #         state = geo_data["state"]
        #         country = geo_data["country"]
        #         speak(f"sir i am not sure , but i think we are in {city} city of {state} state of {country} country")


        #     except Exception as e:
        #         speak("sorry sir , due to network issue i am not able to find our location



##################################### FOR WIKIPEDIA #####################################
        elif 'wikipedia' in cm:
            speak('Searching Wikipedia...')
            # cm = cm.lower()
            cm = cm.replace("wikipedia", "")
            results = wikipedia.summary(cm, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

###################################################################################################
##################################### FOR HIDE FILES AND FOLDERS #####################################
        elif "hide all files" in cm or "hide this folder" in cm or "visible for all" in cm:
            speak("sir please tell ne you want to hide this folder or visible for all")
            condition = takecommand().lower()
            if 'hide' in condition :
                os.system("attrib +h /s /d")
                speak("your all files in this folder are hidden now")
            elif 'visible' in condition:
                os.system("attrib -h /s /d")
                speak("your all files are visible for all")

            elif 'leave it' or 'leave now' in condition:
                speak("ok sir")

###################################################################################################


 # having some issue
 ##################################### FOR CALCULATION #####################################
        # elif "do some calculation" in cm or "can you calculate" in cm or "calculate" in cm:
        #     try:
        #         r = sr.Recognizer()
        #         with sr.Microphone() as source:
        #             speak("say what you want to calculate")
        #             print("Listening.....")
        #             r.adjust_for_ambient_noise(source)
        #             audio  = r.listen(source)
        #         my_string = r.recognize_google(audio)
        #         print(my_string)
        #         def get_operator_fn(op):
        #             return {
        #                 '+': operator.add,
        #                 '-' : operator.sub,
        #                 '*' : operator.mul,
        #                 'divided': operator.__truediv__,
        #             }[op]
            
        #         def eval_binary_expr(op1,oper,op2):
        #             op1,op2 = int(op1),int(op2)
        #             return get_operator_fn(oper)(op1,op2)
        #         speak("your result is")
        #         speak(eval_binary_expr(*(my_string.split())))

        #     except Exception as e:
        #         speak("sir can you tell me again.....")



##################################### FOR TAKING SCREENSHOTS #####################################
        elif "take screenshot" in cm or "take a screenshot" in cm:
            try:
                speak("sir, please tell me the name of this screenshot file  ")
                name = takecommand()
                time.sleep(3)
                img = pyautogui.screenshot()
                img.save(f"{name}.png")
                speak("anything else sir ")

            except Exception as e:
                speak("sir having some issue, can you tell me again")        
###################################################################################################



        elif 'hi' in cm or 'hello' in cm:
            speak('Hello sir, how may I help you?') 

        elif "how are you" in cm:
            speak("I am fine sir, what about you") 

        elif "also good" in cm or "fine" in cm:
            speak("that's great to hear from you.")


        elif "thank you" in cm or "thanks" in cm:
            speak("it's my pleasure sir.")


        elif "volume up" in cm:
            pyautogui.press("volumeup")

        elif "volume down" in cm:
            pyautogui.press("volumedown")

        elif "volume mute" in cm:
            pyautogui.press("volumemute")

##################################### FOR TEMPREATURE ##################################### 
        elif "temperature" in cm:
            temprature()       

###################################################################################################
##################################### FOR BATTERY PERCENTAGE #####################################
        elif "how much power left" in cm or "how much power we have" in cm or "battery" in cm:
            battery()

###################################################################################################
##################################### FOR IP ADDRESS #####################################
        elif 'ip address' in cm:
            ip = get("https://api.ipify.org").text
            print(ip)
            speak(f"your ip address is {ip}")

###################################################################################################
##################################### FOR GOOGLE SEARCH #####################################
        elif 'open google' in cm:
            speak('what can i search for you')
            cm = takecommand()
            webbrowser.open(f"{cm}")


###################################################################################################
##################################### FOR YOUTUBE SEARCH #####################################
        elif 'open youtube' in cm:
            speak('what can i search for you')
            cm = takecommand()
            kit.playonyt(f"{cm}")


###################################################################################################
##################################### FOR SET ALARM #####################################
        elif 'alarm' in cm:
            speak("sir please tell me time to set alarm. for example ,set alarm to 2:30 AM")
            tt = takecommand()
            tt = tt.replace("set alarm to ","")
            tt = tt.replace(".","")
            tt = tt.upper()
            import MyAlarm
            MyAlarm.alarm(tt)


###################################################################################################
##################################### TO ACTIVATE HOW TO DO MODE #####################################
        elif 'activate how to do mode' in cm:
            HowToDo()


###################################################################################################
##################################### FOR CHECK INTERNET SPEED #####################################
        elif "internet speed" in cm:
            inetrnetSpeed(cm)


###################################################################################################
##################################### GO TO EDUCATION MODE #####################################
        elif "education" in cm:
            education()
###################################################################################################






        elif "exit" in cm or "stop" in cm:
            speak("okey sir, i am exiting now.")
            task()

        elif "you can sleep" in cm or "sleep now" in cm:
            speak("okey sir, i am going to sleep you can call me anytime.")
            main()
        

        elif "where are you" in cm or "your path" in cm or "your present working directory" in cm or "which function" in cm or "function" in cm:
            speak("sir, now i am in system")
        


##################################### EDUCATION #####################################
def education():
    speak("sir, now i am in Education mode")
    speak("so sir what do you want to read or study")
    
    while True:
        edu = takecommand()
        

        if "online learning" in edu or "free course" in edu or "free course" in edu:
                speak("Showing you the free online courses available.")
                webbrowser.open("https://www.learnvern.com/")

        elif "html" in edu or "course on  html" in edu: #or "free course on  html" in edu:
                speak("Showing you the free course on HTML.")
                webbrowser.open("https://www.learnvern.com/html5-tutorial")
                webbrowser.open("https://youtu.be/HcOc7P5BMi4")


        elif "css" in edu or "course on  css" in edu:
                speak("Showing you the course on CSS.")
                webbrowser.open("https://youtu.be/Edsxf_NBFrw")
                webbrowser.open("https://www.learnvern.com/css3-tutorial")


##################################### FOR GOOGLE SEARCH #####################################
        elif 'open google' in edu:
            speak('what can i search for you')
            cm = takecommand()
            webbrowser.open(f"{cm}")


##################################### FOR YOUTUBE SEARCH #####################################
        elif 'open youtube' in edu:
            speak('what can i search for you')
            cm = takecommand()
            kit.playonyt(f"{cm}")

        elif "system" in edu:
            speak("okey sir, i am going to system mode")
            sys()


        elif "exit" in edu or "stop" in edu:
            speak("okey sir, i am exiting now.")
            task()

        elif "you can sleep" in edu or "sleep now" in edu:
            speak("okey sir, i am going to sleep you can call me anytime.")
            main()


        elif "where are you" in edu or "your path" in edu or "your present working directory" in edu or "which function" in edu or "function" in edu:
            speak("sir,i am in education")

        


##################################### TASK PERFORM #####################################
def task():
    wish()
    speak("sir,i am ready to doing work")
    speak("sir what work do we have to do today")
    while True:
        query =  takecommand()
        try:
            if "system" in query or "work" in query:
                sys()
            elif "education" in query:
                education()

            # elif "you can sleep" in query or "sleep now" in query:
            #     speak("okey sir, i am going to sleep you can call me anytime.")

            elif "where are you" in query or "your path" in query or "your present working directory" in query or "which function" in query or "function" in query:
                speak("sir, now i am ready to doing your work")

            elif "you can sleep" in query or "sleep now" in query:
                speak("okey sir, i am going to sleep you can call me anytime.")
                main()
        except Exception as e:
            # speak("")
            pass
            

def main():
    speak("sir to start to program say wake up or start")
    speak("to stop the program say stop or exit or goodbye")
    while True:
        permission = takecommand()
        try:
            if "wake up" in permission or "start" in permission:
                task()

            elif "goodbye" in permission or "good bye" in permission or "stop" in permission:
                speak("good bye sir,")
                sys.exit()
        except Exception as e:
            speak("please tell me again start or wake or start the program or to stop the program say stop or good bye ")
            main()



##################################### MAIN #####################################
if __name__=="__main__":
    main()

