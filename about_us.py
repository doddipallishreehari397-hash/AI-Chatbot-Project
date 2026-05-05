from tkinter import *
import os

def open_about():
    about = Toplevel()
    about.title("About Us")
    about.geometry("400x550")

    Label(about, text="🤖 AI Chatbot Project", font=("Arial", 16)).pack(pady=10)

    try:
        base_path = os.path.dirname(__file__)
        logo_path = os.path.join(base_path, "logo.png")

        logo = PhotoImage(file=logo_path)

        # 🔥 Resize image (VERY IMPORTANT)
        logo = logo.subsample(3, 3)

        label = Label(about, image=logo)
        label.image = logo
        label.pack(pady=10)

    except:
        Label(about, text="(Logo Here)").pack()

    Label(about, text="Developed by:", font=("Arial", 12)).pack(pady=10)

    Label(about, text="S Harika - Frontend").pack(pady=5)
    Label(about, text="V Pallavi - Backend").pack(pady=5)
    Label(about, text="D Sreehari - AI Developer").pack(pady=5)

    Label(about, text="\nSiddharth Institute of Engineering and Technology").pack(pady=10)