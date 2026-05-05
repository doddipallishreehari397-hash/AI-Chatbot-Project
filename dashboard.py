from tkinter import *
from navigation import create_navigation

def open_dashboard(root, role):
    print("Dashboard opened for:", role)

    # 🔥 Use Toplevel instead of Tk
    window = Toplevel(root)
    window.title("Dashboard")
    window.geometry("900x550")
    window.configure(bg="#121212")

    # ---------- NAVIGATION ----------
    nav_frame = Frame(window, bg="#1f1f1f", width=200)
    nav_frame.pack(side=LEFT, fill=Y)

    create_navigation(nav_frame, role)

    # ---------- MAIN CONTENT ----------
    content = Frame(window, bg="#181818")
    content.pack(side=RIGHT, fill=BOTH, expand=True)

    # ---------- HEADER ----------
    header = Frame(content, bg="#1f1f1f", height=60)
    header.pack(fill=X)

    Label(
        header,
        text=f"Welcome {role.capitalize()} 👋",
        font=("Helvetica", 16, "bold"),
        fg="white",
        bg="#1f1f1f"
    ).pack(pady=15)

    # ---------- BODY ----------
    body = Frame(content, bg="#181818")
    body.pack(pady=20)

    # Section title
    Label(
        body,
        text="Features",
        font=("Arial", 14, "bold"),
        fg="#00d4ff",
        bg="#181818"
    ).pack(pady=10)

    # ---------- CARD STYLE FUNCTION ----------
    def create_card(parent, text):
        card = Frame(parent, bg="#2b2b3c", bd=0, relief="flat")
        card.pack(pady=8, ipadx=10, ipady=10, fill=X, padx=50)

        Label(
            card,
            text=text,
            font=("Arial", 11),
            fg="white",
            bg="#2b2b3c",
            anchor="w"
        ).pack(fill=X, padx=10)

    # ---------- ROLE BASED FEATURES ----------
    if role == "admin":
        create_card(body, "📅 Add Timetable")
        create_card(body, "📝 Add Exams")
        create_card(body, "🔔 Send Notifications")

    else:
        create_card(body, "📅 View Timetable")
        create_card(body, "💬 Ask Chatbot")
        create_card(body, "🔔 View Notifications")

    # ---------- FOOTER ----------
    Label(
        content,
        text="AI Student Chatbot System",
        font=("Arial", 9),
        fg="#aaaaaa",
        bg="#181818"
    ).pack(side=BOTTOM, pady=10)