import sounddevice as sd                    #To record audio from mic
import numpy as np                          #To handle audio data as arrays
import speech_recognition as sr             #To convert speech to text
import datetime                             #To get current date and time
import os                                   #To run system commands like opening apps
import pyttsx3

# Initialize text-to-speech engine once (not inside function)
engine = pyttsx3.init()

# Function to speak out loud using TTS
def speak(text):
    engine.say(text)
    engine.runAndWait()

#define audio recording function 
def record_audio(duration=5, fs=44100):
    print("🎙️Speak now...")
    audio =sd.rec(int(duration *fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait() #wait until recording is finished
    print("✅ Recording complete.")
    return audio, fs

#Now we use speech_recognition to convert the audio to text
def recognize_speech(audio_data, fs):
    recognizer = sr.Recognizer()

 # Convert numpy array to bytes (raw PCM format expected by recognizer)
    audio_no = np.array(audio_data, dtype='int16')   #ensure format
    
 # Wrap audio bytes into recognizer-compatible format
    audio_bytes = audio_no.tobytes()                 #Convert to bytes
    audio= sr.AudioData(audio_bytes, sample_rate=fs,sample_width=2)
 
    try:
        text = recognizer.recognize_google(audio)
        print("🗣️You said:", text)
        return text
    except sr.UnknownValueError:
        print("😥 Sorry, could not understand your speech.")
    except sr.RequestError:
        print("🚫 Could not request results from Google Speech Recognition service.")

def process_command(text):
    #step 1: convert the text to lower case for easy matching
    text = text.lower()

    if "hello" in text or "hi" in text:
        reply = "Hello! i am friday, How can I help you?"

    #check for the word "time"
    elif "time" in text:
        from datetime import datetime
        now = datetime.now().strftime("%I:%M %p")
        reply = f"The curernt time is {now}"

# step 3: Check if the user said "open notepad"
    elif "open notepad" in text:
        os.system("notepad.exe")
        reply = "Opening Notepad"
    
    elif "open command prompt" in text or "open cmd" in text:
        os.system("cmd.exe")
        reply = "Opening Command Prompt"

#step 4 if none of the above matched
    else:
        reply = "🥹  Sorry, I don't understand that command."
        
        
    print("🤖:", reply)
    speak(reply)

#Glue together
def main():
    WAKE_WORD = "friday"
    speak("Yes, Sir I am here for you")
    
    while True:
      print("waiting for wake word...")
    # First listen for wake word
      audio, fs = record_audio(duration=2)
      text = recognize_speech(audio, fs)

      if text and WAKE_WORD in text.lower():
          print("✅Wake word detected. Listening for command.")
          speak("Yes?")
    #Now record the actual
      duration_seconds = 4  #Adjust if needed
      audio, sample_rate = record_audio(duration=duration_seconds)
      text = recognize_speech(audio, sample_rate)
      
      if text:
        if "exit" in text.lower() or "quit" in text.lower():
            print("👋 Exiting...")
            speak("Goodbye! Shutting down.")
            break #exit the while loop
        else:
            process_command(text)

#Run if this is the main file
if __name__=="__main__":
    main()