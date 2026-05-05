import pyttsx3

engine = pyttsx3.init()

# Voice settings
engine.setProperty('rate', 150)
engine.setProperty('volume', 1.0)

# Change voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(text):
    print("Bot:", text)
    engine.say(text)
    engine.runAndWait()
if __name__ == "__main__":
    speak("Hello, I'm working!")