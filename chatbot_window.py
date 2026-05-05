from tkinter import *
import speech_recognition as sr
import pyttsx3
import sys
import os

base_path = os.path.dirname(__file__)
backend_path = os.path.join(base_path, "..", "backend")
sys.path.append(backend_path)

from chatbot_logic import chatbot_response

# ---------- VOICE ----------
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            audio = r.listen(source, timeout=5)
            return r.recognize_google(audio)
        except:
            return "Sorry, I couldn't hear you"

# ---------- SPLASH ----------
def show_splash(parent):
    splash = Toplevel(parent)
    splash.geometry("400x250")
    splash.configure(bg="#121212")

    Label(splash, text="🤖 AI STUDENT CHATBOT",
          font=("Helvetica", 16, "bold"),
          bg="#121212", fg="white").pack(pady=40)

    Label(splash, text="Loading...",
          font=("Arial", 12),
          bg="#121212", fg="#bbbbbb").pack()

    parent.after(2000, splash.destroy)

# ---------- MAIN CHAT ----------
def open_chat(parent):

    chat = Toplevel(parent)
    chat.title("AI Chatbot")
    chat.geometry("650x600")
    chat.configure(bg="#121212")

    show_splash(chat)

    # ---------- HEADER ----------
    header = Frame(chat, bg="#1f1f1f", height=60)
    header.pack(fill=X)

    Label(header, text="💬 AI Chatbot",
          bg="#1f1f1f", fg="white",
          font=("Helvetica", 16, "bold")).pack(pady=15)

    # ---------- CHAT AREA ----------
    frame = Frame(chat, bg="#121212")
    frame.pack(fill=BOTH, expand=True, padx=10, pady=5)

    scrollbar = Scrollbar(frame)
    scrollbar.pack(side=RIGHT, fill=Y)

    text_area = Text(
        frame,
        wrap=WORD,
        yscrollcommand=scrollbar.set,
        font=("Arial", 11),
        bg="#1e1e2f",
        fg="white",
        insertbackground="white",
        bd=0,
        padx=10,
        pady=10
    )
    text_area.pack(side=LEFT, fill=BOTH, expand=True)

    scrollbar.config(command=text_area.yview)

    # ---------- INPUT AREA ----------
    bottom = Frame(chat, bg="#1f1f1f")
    bottom.pack(fill=X)

    entry = Entry(
        bottom,
        font=("Arial", 12),
        bg="#2b2b3c",
        fg="white",
        insertbackground="white",
        bd=0
    )
    entry.pack(side=LEFT, fill=X, expand=True, padx=10, pady=10, ipady=6)

    # ---------- SEND ----------
    def send_message(user_text=None):
        if user_text:
            user = user_text
        else:
            user = entry.get().strip()

        if user == "":
            return

        # USER MESSAGE (Right style)
        text_area.insert(END, "You:\n", "user_label")
        text_area.insert(END, user + "\n\n", "user_msg")

        response = chatbot_response(user)

        # BOT MESSAGE (Left style)
        text_area.insert(END, "Bot:\n", "bot_label")
        text_area.insert(END, response + "\n\n", "bot_msg")

        speak(response)

        entry.delete(0, END)
        text_area.yview_moveto(1.0)

    entry.bind("<Return>", lambda event: send_message())

    # ---------- VOICE ----------
    def voice_input():
        text_area.insert(END, "🎤 Listening...\n", "bot_msg")
        chat.update()

        user = listen()
        send_message(user)

    # ---------- CLEAR ----------
    def clear_chat():
        text_area.delete("1.0", END)

    # ---------- BUTTONS ----------
    Button(
        bottom, text="Send",
        command=send_message,
        bg="#00d4ff", fg="black",
        font=("Arial", 10, "bold"),
        relief="flat",
        padx=10, pady=5,
        cursor="hand2"
    ).pack(side=LEFT, padx=5)

    Button(
        bottom, text="🎤",
        command=voice_input,
        bg="#2ecc71",
        font=("Arial", 10),
        relief="flat",
        width=4,
        cursor="hand2"
    ).pack(side=LEFT, padx=5)

    Button(
        bottom, text="Clear",
        command=clear_chat,
        bg="#e74c3c", fg="white",
        font=("Arial", 10, "bold"),
        relief="flat",
        padx=8, pady=5,
        cursor="hand2"
    ).pack(side=RIGHT, padx=10)

    # ---------- TEXT STYLES ----------
    text_area.tag_config("user_label", foreground="#00d4ff", font=("Arial", 10, "bold"))
    text_area.tag_config("user_msg", foreground="white", background="#2b2b3c")

    text_area.tag_config("bot_label", foreground="#2ecc71", font=("Arial", 10, "bold"))
    text_area.tag_config("bot_msg", foreground="white", background="#1abc9c")