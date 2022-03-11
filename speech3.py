import speech_recognition as sr
r = sr.Recognizer()                                                                                   
with sr.Microphone() as source:                                                                      
    print("listening...")
    r.adjust_for_ambient_noise(source, duration = 5)
    audio = r.listen(source)
    try:
        said=r.recognize_google(audio)
        said = lower()
        print(f"Recognized {text}")
        
    except:
        print("some error occurred!")