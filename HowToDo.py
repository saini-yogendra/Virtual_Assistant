import pyttsx3
import speech_recognition as sr
from pywikihow import search_wikihow


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






def HowToDo():
    speak("How to do mode activated")
    while True:
        speak("please tell me what you want to know")
        how = takecommand().lower()
        try:
            if 'exit' in how or 'close' in how:
                speak("okey sir , how to do mode is closed")
                break
            else:
                max_result = 1
                how_to = search_wikihow(how,max_result)
                assert len(how_to[0].summary)
                how_to[0].print()
                speak(how_to[0].summary)

        except Exception as e:
            speak("sorry sir, i am not able to find this")



# if __name__=="__main__":
#     HowToDo()