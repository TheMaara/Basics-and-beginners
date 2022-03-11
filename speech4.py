import speech_recognition as sr

recognizer = sr.Recognizer()


try:
    with sr.Microphone(0) as source:
        print('Speak Now')
        recognizer.adjust_for_ambient_noise(source)#(Problem Solved)
        voice= recognizer.listen(source)
        text= recognizer.recognize_google(voice)
        print(text)

except:
     pass