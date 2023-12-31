import pyttsx3
import psutil



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()




def battery():
    battery = psutil.sensors_battery()
    percentage = battery.percent
    speak(f"sir, uor system have {percentage} percent battery")
    if percentage>=75:
        speak("sir, we have enough power to continue our work")
    elif percentage>=40 and percentage<=75:
        speak("sir, we should connect our system to charging port to charge our battery")
    elif percentage<=15 and percentage<=30:
        speak("sir,we don't have enough power to work, please connect to charging ")
    elif percentage<=15:
        speak("sir, we have very low power, please connect to charging the system will shutdown very soon")



# if __name__=="__main__":
#     battery()