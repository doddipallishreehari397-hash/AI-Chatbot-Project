from tkinter import *
import json
import os

def show_notification():
    win = Toplevel()
    win.title("Notifications")
    win.geometry("400x400")

    Label(win, text="🔔 Notifications", font=("Arial", 16)).pack(pady=10)

    base_path = os.path.dirname(__file__)
    dataset_path = os.path.join(base_path, "..", "dataset")

    data_file = os.path.join(dataset_path, "data.json")

    # ---------- LOAD ADMIN DATA ----------
    try:
        with open(data_file, "r") as f:
            new_data = json.load(f)
    except:
        new_data = []

    frame = Frame(win)
    frame.pack(fill=BOTH, expand=True)

    # ---------- ONLY ADMIN NOTIFICATIONS ----------
    if isinstance(new_data, list) and new_data:
        for item in new_data:
            msg = item.get("message", "")
            typ = item.get("type", "")
            Label(frame, text=f"🔔 {msg}", anchor="w").pack(fill=X, padx=10, pady=5)
    else:
        Label(frame, text="No new notifications").pack(pady=20)