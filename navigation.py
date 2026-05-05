from tkinter import *
from chatbot_window import open_chat
from notifications import show_notification_popup, get_notification_count
from about_us import open_about
from admin_panel import open_admin_panel

def create_navigation(parent, role):

    # ---------- SIDEBAR ----------
    frame = Frame(parent, bg="#1f1f1f", width=200)
    frame.pack(side=LEFT, fill=Y)
    frame.pack_propagate(False)

    # ---------- TITLE ----------
    Label(
        frame,
        text="MENU",
        bg="#1f1f1f",
        fg="#00d4ff",
        font=("Helvetica", 16, "bold")
    ).pack(pady=20)

    # ---------- BUTTON STYLE ----------
    def create_nav_button(text, command=None):
        btn = Button(
            frame,
            text=text,
            anchor="w",
            command=command,
            font=("Arial", 11),
            bg="#1f1f1f",
            fg="white",
            activebackground="#2b2b3c",
            activeforeground="white",
            bd=0,
            relief="flat",
            padx=20,
            pady=8,
            cursor="hand2"
        )
        btn.pack(fill=X, pady=2)

        # Hover effect 🔥
        btn.bind("<Enter>", lambda e: btn.config(bg="#2b2b3c"))
        btn.bind("<Leave>", lambda e: btn.config(bg="#1f1f1f"))

        return btn

    # ---------- BUTTONS ----------
    create_nav_button("🏠 Dashboard")

    create_nav_button(
        "💬 Chatbot",
        lambda: open_chat(parent)
    )

    # 🔔 Notification count
    count = get_notification_count()
    notif_text = f"🔔 Notifications ({count})"

    create_nav_button(
        notif_text,
        lambda: show_notification_popup(parent)   # ✅ FIXED
    )

    create_nav_button(
        "ℹ About Us",
        lambda: open_about(parent)
    )

    # ---------- ADMIN ----------
    if role == "admin":
        Label(
            frame,
            text="ADMIN",
            bg="#1f1f1f",
            fg="#888",
            font=("Arial", 10, "bold")
        ).pack(pady=(15, 5))

        create_nav_button(
            "⚙ Admin Panel",
            lambda: open_admin_panel(parent)
        )