import speech_recognition as sr
import pyttsx3
r = sr.Recognizer()
m = sr.Microphone()

engine = pyttsx3.init() 

print('Start ')

try:
    with m as source: #r.adjust_for_ambient_noise(source)
#     i=0
    while True:
#         i+=1
        with m as source: audio = r.listen(source)
#         print(i)

        try:

            value = r.recognize_google(audio)

            if str is bytes: 
                result = u"{}".format(value).encode("utf-8")

            else: 
                result = "{}".format(value)
            print(result)
            engine.say("You said"+result ) 
            engine.runAndWait()
           
            

        except sr.UnknownValueError:
            print("")
        except sr.RequestError as e:
            print("{0}".format(e))
             
            
except KeyboardInterrupt:
    pass
