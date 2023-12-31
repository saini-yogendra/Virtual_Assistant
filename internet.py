import pyttsx3
import speedtest
import speech_recognition as sr


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
    # cm_sys = cm_sys.lower()
    return query





def inetrnetSpeed():
    # while True:
        # cm = takecommand().lower()
       
        # if "internet speed" in cm or "check internet speed" in cm:
        speak("sir, wait i am checking our internet speed")
        st = speedtest.Speedtest()
        dl = st.download()/1048576
        up = st.upload()/1048576
        speak(f"sir , we have {dl} bits per second downloading speed and {up} bits per second uploading speed")
        # speak("sir, can i show downloading speed or not")
        print(dl)
        print(up)


        # cm = takecommand().lower()

        # if 'yes' in cm:
            
        #     print(f"Downloading speed is {dl} byts per second and uploading speed is {up} byts per second")

        # else:
        #     speak("ok sir")



# if __name__=="__main__":
#     inetrnetSpeed()