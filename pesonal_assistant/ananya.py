import sounddevice as sd                    # To record audio from mic
import numpy as np                          # To handle audio data as arrays
import speech_recognition as sr             # To convert speech to text
import datetime                             # To get current date and time
import os                                   # To run system commands
import pyttsx3                              # For TTS

# Initialize TTS engine once globally
engine = pyttsx3.init()

def speak(text):
    print("🗣 Loki:", text)
    engine.say(text)
    engine.runAndWait()

# Record audio from microphone
def record_audio(duration=5, fs=44100):
    print("🎙 Speak now...")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()
    print("✅ Recording complete.")
    return audio, fs

# Recognize speech using Google API
def recognize_speech(audio_data, fs):
    recognizer = sr.Recognizer()
    try:
        audio_bytes = audio_data.astype(np.int16).tobytes()
        audio = sr.AudioData(audio_bytes, sample_rate=fs, sample_width=2)
        print("🧠 Recognizing speech...")
        text = recognizer.recognize_google(audio)
        print("🗣 You said:", text)
        return text
    except sr.UnknownValueError:
        speak("Sorry, I couldn't understand that.")
    except sr.RequestError:
        speak("There was an issue contacting the recognition service.")

# Process user commands
def process_command(text):
    text = text.lower()

    if "hello" in text or "hi" in text:
        reply = "Hello! I am Loki. How can I help you?"
        speak(reply)

    elif "time" in text:
        now = datetime.datetime.now().strftime("%I:%M %p")
        reply = f"The current time is {now}."
        speak(reply)

    elif "open notepad" in text:
        os.system("notepad.exe")
        reply = "Opening Notepad."
        speak(reply)

    elif "open command prompt" in text or "open cmd" in text:
        os.system("start cmd")  # more reliable on some systems
        reply = "Opening Command Prompt."
        speak(reply)

    else:
        reply = f"Sorry, I don't understand that command."
        speak(reply)

# Main loop
def main():
    while True:
        audio, fs = record_audio(duration=4)
        text = recognize_speech(audio, fs)

        if text:
            if "exit" in text.lower() or "quit" in text.lower():
                speak("Goodbye! Shutting down.")
                break
            else:
                process_command(text)

# Run the assistant
if __name__ == "__main__":
    main()