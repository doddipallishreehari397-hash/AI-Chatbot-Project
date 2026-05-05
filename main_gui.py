import tkinter as tk
from tkinter import messagebox, PhotoImage
import json
import os

from dashboard import open_dashboard

# ---------- CREATE ROOT ----------
root = tk.Tk()
root.withdraw()

# ---------- FILE PATH ----------
base_path = os.path.dirname(__file__)
users_file = os.path.join(base_path, "..", "dataset", "users.json")

# ---------- LOAD USERS ----------
def load_users():
    try:
        with open(users_file, "r") as f:
            return json.load(f)
    except:
        return {"users": []}

users_data = load_users()

# ---------- SPLASH SCREEN ----------
def splash_screen():
    splash = tk.Toplevel()
    splash.title("Welcome")
    splash.geometry("420x320")
    splash.configure(bg="#121212")

    container = tk.Frame(splash, bg="#121212")
    container.pack(expand=True)

    try:
        logo_path = os.path.join(base_path, "logo.png")
        logo = PhotoImage(file=logo_path)
        logo = logo.subsample(3, 3)
        tk.Label(container, image=logo, bg="#121212").pack(pady=10)
        splash.image = logo
    except:
        tk.Label(container, text="🎓 AI Chatbot",
                 font=("Helvetica", 18, "bold"),
                 fg="white", bg="#121212").pack(pady=20)

    tk.Label(container, text="AI Student Chatbot",
             font=("Arial", 14),
             fg="#00d4ff", bg="#121212").pack()

    tk.Label(container, text="Loading...",
             font=("Arial", 11),
             fg="#bbbbbb", bg="#121212").pack(pady=10)

    splash.after(2000, lambda: open_login(splash))

# ---------- LOGIN ----------
def open_login(splash):
    splash.destroy()

    login = tk.Toplevel()
    login.title("Login")
    login.geometry("420x350")
    login.configure(bg="#121212")

    # ---------- CONTAINER ----------
    frame = tk.Frame(login, bg="#1e1e2f", padx=20, pady=20)
    frame.place(relx=0.5, rely=0.5, anchor="center")

    # ---------- TITLE ----------
    tk.Label(frame, text="🔐 Login",
             font=("Helvetica", 18, "bold"),
             fg="white", bg="#1e1e2f").pack(pady=10)

    # ---------- USERNAME ----------
    tk.Label(frame, text="Username",
             fg="#00d4ff", bg="#1e1e2f",
             font=("Arial", 11, "bold")).pack(anchor="w")

    username = tk.Entry(frame,
                        font=("Arial", 11),
                        bg="#2b2b3c",
                        fg="white",
                        insertbackground="white",
                        bd=0)
    username.pack(fill="x", pady=5, ipady=6)

    # ---------- PASSWORD ----------
    tk.Label(frame, text="Password",
             fg="#00d4ff", bg="#1e1e2f",
             font=("Arial", 11, "bold")).pack(anchor="w", pady=(10, 0))

    password = tk.Entry(frame,
                        show="*",
                        font=("Arial", 11),
                        bg="#2b2b3c",
                        fg="white",
                        insertbackground="white",
                        bd=0)
    password.pack(fill="x", pady=5, ipady=6)

    # ---------- STATUS ----------
    status = tk.Label(frame, text="",
                      font=("Arial", 10),
                      bg="#1e1e2f")
    status.pack(pady=5)

    # ---------- LOGIN FUNCTION ----------
    def check_login():
        user = username.get().strip().lower()
        pwd = password.get().strip()

        for u in users_data.get("users", []):
            if u["username"].lower() == user and u["password"] == pwd:
                login.destroy()
                open_dashboard(root, u["role"])
                return

        status.config(text="❌ Invalid Login", fg="red")

    # ---------- BUTTON ----------
    tk.Button(frame,
              text="Login",
              command=check_login,
              font=("Arial", 11, "bold"),
              bg="#00d4ff",
              fg="black",
              relief="flat",
              padx=10,
              pady=6,
              cursor="hand2").pack(pady=10)

# ---------- START ----------
if __name__ == "__main__":
    splash_screen()
    root.mainloop()