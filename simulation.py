import speech_recognition as sr
from pydub import AudioSegment
import time

start = time.time()

print("Loading WhatsApp audio...")

src = "myTest.ogg" # WhatsApp audio name. In this case, i called as "myTest.ogg"
dst = "test.wav" # Converted audio name. In this case, i called as "test.wav"
sound = AudioSegment.from_ogg(src) # Open a .ogg file

print("Converting WhatsApp audio to .wav audio file...")

sound.export(dst, format="wav") # It's necessary this conversion, why the recognizer just works with .wav files
sampleAudio = sr.AudioFile('test.wav') # open the converted audio
recognizer = sr.Recognizer() # create a recognizer instance 

print("Transcribing audio...")

with sampleAudio as audio_file:
    audioContent = recognizer.record(audio_file) # Transfer the audio content
    text = recognizer.recognize_google(audioContent, language='pt-BR') # Transcribes the audio. In this case, in portugues
    # text = recognizer.recognize_google(audioContent, language='en-US') # this option allows the transcription by English language
    print("\n"+text+"\n")
end = time.time()
print("Total execution time: "+str(end-start))
