from flask import Flask, render_template, request, jsonify
from backend.chatbot_logic import chatbot_response

import json
import os
import time

app = Flask(__name__)

@app.context_processor
def inject_now():
    return {'now': int(time.time())}

app = Flask(__name__)


# ==================================================
# HOME PAGE
# ==================================================

@app.route("/")
def home():
    return render_template("index.html")


# ==================================================
# ADMIN PAGE
# ==================================================

@app.route("/admin")
def admin():

    # admin.html must be inside templates folder
    return render_template("admin.html")


# ==================================================
# LOGIN
# ==================================================

@app.route("/login", methods=["POST"])
def login():

    data = request.get_json()

    username = data.get("username", "")
    password = data.get("password", "")

    # ADMIN LOGIN
    if username == "admin" and password == "1234":

        return jsonify({
            "success": True,
            "role": "admin",
            "redirect": "/admin"
        })

    # STUDENT LOGIN
    elif username == "student" and password == "1234":

        return jsonify({
            "success": True,
            "role": "student",
            "redirect": "/"
        })

    # INVALID LOGIN
    return jsonify({
        "success": False,
        "message": "Invalid Credentials"
    })


# ==================================================
# CHATBOT
# ==================================================

@app.route("/chat", methods=["POST"])
def chat():

    try:

        data = request.get_json()

        user_message = data.get("message", "")

        response = chatbot_response(user_message)

        return jsonify({
            "success": True,
            "response": response
        })

    except Exception as e:

        print("Chat Error:", e)

        return jsonify({
            "success": False,
            "response": "Server Error"
        })


# ==================================================
# GET NOTIFICATIONS
# ==================================================

@app.route("/notifications", methods=["GET"])
def notifications():

    file_path = os.path.join(
        "dataset",
        "data.json"
    )

    # FILE NOT FOUND
    if not os.path.exists(file_path):

        return jsonify([])

    try:

        with open(
            file_path,
            "r",
            encoding="utf-8"
        ) as f:

            data = json.load(f)

        return jsonify(data)

    except Exception as e:

        print("Notification Error:", e)

        return jsonify([])


# ==================================================
# ADD NOTIFICATION
# ==================================================

@app.route("/add_notification", methods=["POST"])
def add_notification():

    file_path = os.path.join(
        "dataset",
        "data.json"
    )

    data = request.get_json()

    new_notification = {

        "type": data.get(
            "type",
            "general"
        ),

        "message": data.get(
            "message",
            ""
        )
    }

    # LOAD OLD DATA
    if os.path.exists(file_path):

        try:

            with open(
                file_path,
                "r",
                encoding="utf-8"
            ) as f:

                notifications = json.load(f)

        except:

            notifications = []

    else:

        notifications = []

    # ADD NEW DATA
    notifications.append(
        new_notification
    )

    # SAVE FILE
    try:

        with open(
            file_path,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                notifications,
                f,
                indent=4
            )

        return jsonify({

            "success": True,

            "message":
            "Notification added successfully"
        })

    except Exception as e:

        print("Save Error:", e)

        return jsonify({

            "success": False,

            "message":
            "Failed to save notification"
        })


# ==================================================
# RUN APP
# ==================================================

if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )