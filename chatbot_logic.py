import json
import os
from datetime import datetime

# ---------- PATH SETUP ----------
base_path = os.path.dirname(__file__)
dataset_path = os.path.join(base_path, "..", "dataset")

timetable_file = os.path.join(dataset_path, "timetable.json")
exam_file = os.path.join(dataset_path, "exams.json")
data_file = os.path.join(dataset_path, "data.json")


# ---------- LOAD JSON ----------
def load_json(file):
    try:
        with open(file, "r") as f:
            return json.load(f)
    except:
        return {}


# ---------- MAIN CHATBOT ----------
def chatbot_response(user_input):
    user_input = user_input.lower().strip()

    timetable_data = load_json(timetable_file)
    exam_data = load_json(exam_file)
    new_data = load_json(data_file)

    # ---------- GREETING ----------
    if any(word in user_input for word in ["hi", "hello", "hey"]):
        return "Hello! How can I help you? 😊"

    # ---------- THANK YOU ----------
    elif any(word in user_input for word in ["thank", "thanks", "thx"]):
        return "You're welcome 😊"

    # ---------- BYE ----------
    elif any(word in user_input for word in ["bye", "goodbye", "see you"]):
        return "Goodbye! Have a nice day 👋"

    # ---------- HOW ARE YOU ----------
    elif "how are you" in user_input:
        return "I'm doing great! How can I assist you?"

    # ---------- TIMETABLE ----------
    elif "timetable" in user_input:

        tt = timetable_data.get("timetable", {})
        timings = timetable_data.get("timings", {})

        if not tt:
            return "No timetable available."

        response = "📅 Weekly Timetable:\n"

        for day, subjects in tt.items():
            response += f"\n{day}:\n"
            for hour, sub in subjects.items():
                if sub:
                    time_range = timings.get(f"hour_{hour}", "")
                    response += f"  Hour {hour} ({time_range}) → {sub}\n"

        return response

    # ---------- TODAY TIMETABLE ----------
    elif "today timetable" in user_input:
        today = datetime.now().strftime("%a").upper()[:3]
        tt = timetable_data.get("timetable", {})

        if today in tt:
            response = f"📅 Today's Timetable ({today}):\n"
            for hour, sub in tt[today].items():
                if sub:
                    response += f"Hour {hour} → {sub}\n"
            return response
        else:
            return "No timetable for today."

    # ---------- EXAMS ----------
    elif "exam" in user_input:

        schedule = exam_data.get("schedule", [])

        if not schedule:
            return "No exam data available."

        response = "📝 Upcoming Exams:\n"

        for item in schedule:
            date = item.get("date_text", "")
            subject = item.get("course_name", "")
            response += f"- {date} → {subject}\n"

        return response

    # ---------- NEXT EXAM ----------
    elif "next exam" in user_input:
        schedule = exam_data.get("schedule", [])
        if schedule:
            next_exam = schedule[0]
            return f"Next exam: {next_exam.get('date_text')} → {next_exam.get('course_name')}"
        else:
            return "No upcoming exams."

    # ---------- NOTIFICATIONS ----------
    elif "notification" in user_input or "update" in user_input:

        if isinstance(new_data, list) and new_data:
            response = "🔔 Latest Updates:\n"

            for item in new_data:
                typ = item.get("type", "")
                msg = item.get("message", "")
                response += f"- ({typ}) {msg}\n"

            return response
        else:
            return "No new updates."

    # ---------- DATE ----------
    elif "date" in user_input:
        return datetime.now().strftime("Today's date is %d-%m-%Y")

    # ---------- TIME ----------
    elif "time" in user_input:
        return datetime.now().strftime("Current time is %H:%M")

    # ---------- DEFAULT ----------
    else:
        return "Sorry, I didn't understand. Try 'timetable', 'exam', or 'notifications'."