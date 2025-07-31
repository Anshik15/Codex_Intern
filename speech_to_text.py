import speech_recognition as sr

recognizer= sr.Recognizer()

with sr.Microphone() as source:
    print("speak something....")
    audio= recognizer.listen(source, timeout=5,phrase_time_limit=10)
    text= recognizer.recognize_google(audio,language='en-US')
    print("you said :",text)