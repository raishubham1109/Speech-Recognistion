import speech_recognition as sr
r = sr.Recognizer()
harvard = sr.AudioFile('harvard.wav')
with harvard as source:
        audio1 = r.record(source, duration=4)
        audio2 = r.record(source, duration=4)
text1=r.recognize_google(audio1)
print (text1)
text2=r.recognize_google(audio2)
print(text2)
with harvard as source:
     audio = r.record(source, offset=4, duration=3)

text= r.recognize_google(audio)
print(text)
