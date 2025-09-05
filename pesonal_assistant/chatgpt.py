import sounddevice as sd                    # For recording microphone audio
import numpy as np                          # To handle audio as numerical data
import speech_recognition as sr             # For converting speech to text
import datetime                             # For getting the current date/time
import os                                   # For opening applications
import pyttsx3                              # For converting text to speech

# Initialize text-to-speech engine once (not inside function)
engine = pyttsx3.init()

# Function to speak out loud using TTS
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to record audio from microphone
def record_audio(duration=5, fs=44100):
    print("🎙️ Speak now...")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()  # Wait till recording is complete
    print("✅ Recording complete.")
    return audio, fs

# Function to recognize speech using Google API
def recognize_speech(audio_data, fs):
    recognizer = sr.Recognizer()
    audio_array = np.array(audio_data, dtype='int16')  # Ensure proper format
    audio_bytes = audio_array.tobytes()
    audio = sr.AudioData(audio_bytes, sample_rate=fs, sample_width=2)
    
    try:
        text = recognizer.recognize_google(audio)
        print("🗣️ You said:", text)
        return text
    except sr.UnknownValueError:
        print("😥 Sorry, could not understand your speech.")
    except sr.RequestError:
        print("🚫 Google Speech Recognition service is unavailable.")

# Respond to commands
def process_command(text):
    text = text.lower()  # Normalize to lowercase

    if "hello" in text or "hi" in text:
        reply = "Hello! I am Loki. How can I help you?"
    elif "time" in text:
        now = datetime.datetime.now().strftime("%I:%M %p")
        reply = f"The current time is {now}"
    elif "open notepad" in text:
        os.system("notepad.exe")
        reply = "Opening Notepad."
    elif "open command prompt" in text or "open cmd" in text:
        os.system("cmd.exe")
        reply = "Opening Command Prompt."
    else:
        reply = "🥹 Sorry, I don't understand that command."

    print("🤖", reply)
    speak(reply)

# Main assistant logic
def main():
    WAKE_WORD = "friday"
    speak("Yes Sir, I am here for you.")

    while True:
        print("Waiting for wake word...")

        # First listen for wake word
        audio, fs = record_audio(duration=2)
        text = recognize_speech(audio, fs)

        if text and WAKE_WORD in text.lower():
            print("✅ Wake word detected. Listening for your command.")
            speak("Yes?")

            # Now record the actual command
            audio, fs = record_audio(duration=4)
            command_text = recognize_speech(audio, fs)

            if command_text:
                if "exit" in command_text.lower() or "quit" in command_text.lower():
                    print("👋 Exiting...")
                    speak("Goodbye! Shutting down.")
                    break
                else:
                    process_command(command_text)

# Run this script
if __name__ == "__main__":
    main()
