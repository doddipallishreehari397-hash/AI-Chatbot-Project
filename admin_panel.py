from tkinter import *
import json
import os

def open_admin_panel(parent):

    admin = Toplevel(parent)
    admin.title("Admin Panel")
    admin.geometry("420x420")
    admin.configure(bg="#1e1e2f")  # 🔥 Dark background

    # ---------- TITLE ----------
    Label(
        admin,
        text="⚙️ Admin Panel",
        font=("Helvetica", 18, "bold"),
        fg="#ffffff",
        bg="#1e1e2f"
    ).pack(pady=15)

    # ---------- FRAME (for better alignment) ----------
    form_frame = Frame(admin, bg="#1e1e2f")
    form_frame.pack(pady=10)

    # ---------- LABEL ----------
    Label(
        form_frame,
        text="Enter Notification",
        font=("Arial", 12, "bold"),
        fg="#00d4ff",
        bg="#1e1e2f"
    ).pack(anchor="w", pady=5)

    # ---------- ENTRY ----------
    entry = Entry(
        form_frame,
        width=35,
        font=("Arial", 11),
        bd=2,
        relief="flat",
        bg="#2b2b3c",
        fg="white",
        insertbackground="white"  # cursor color
    )
    entry.pack(pady=5, ipady=6)

    # ---------- STATUS LABEL ----------
    status_label = Label(
        admin,
        text="",
        font=("Arial", 10),
        bg="#1e1e2f"
    )
    status_label.pack(pady=5)

    # ---------- SAVE FUNCTION ----------
    def save_data():
        message = entry.get().strip()

        if message == "":
            status_label.config(text="⚠️ Please enter a message", fg="orange")
            return

        base_path = os.path.dirname(__file__)
        file_path = os.path.join(base_path, "..", "dataset", "data.json")

        try:
            with open(file_path, "r") as f:
                data = json.load(f)
        except:
            data = []

        data.append({
            "type": "notification",
            "message": message
        })

        with open(file_path, "w") as f:
            json.dump(data, f, indent=4)

        entry.delete(0, END)

        status_label.config(text="✅ Saved successfully!", fg="lightgreen")

    # ---------- BUTTON ----------
    Button(
        admin,
        text="💾 Save Notification",
        command=save_data,
        font=("Arial", 11, "bold"),
        bg="#00d4ff",
        fg="black",
        activebackground="#00aacc",
        relief="flat",
        padx=10,
        pady=6,
        cursor="hand2"
    ).pack(pady=15)

    # ---------- CLOSE BUTTON ----------
    Button(
        admin,
        text="Close",
        command=admin.destroy,
        font=("Arial", 10),
        bg="#444",
        fg="white",
        relief="flat",
        padx=8,
        pady=4,
        cursor="hand2"
    ).pack()