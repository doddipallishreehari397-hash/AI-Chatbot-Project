from voice_input import listen
from voice_output import speak
from chatbot_logic import chatbot_response

def run():
    speak("Hello! I am your voice assistant. Say exit to stop.")

    while True:
        user = listen()

        if not user:
            continue

        response = chatbot_response(user)
        speak(response)

        if "bye" in user.lower() or "exit" in user.lower():
            speak("Goodbye!")
            break
        

if __name__ == "__main__":
    run()