import json
import os
from datetime import datetime


# =========================================
# PATHS
# =========================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATASET_DIR = os.path.join(
    BASE_DIR,
    "..",
    "dataset"
)

TIMETABLE_FILE = os.path.join(
    DATASET_DIR,
    "timetable.json"
)

EXAM_FILE = os.path.join(
    DATASET_DIR,
    "exams.json"
)

DATA_FILE = os.path.join(
    DATASET_DIR,
    "data.json"
)


# =========================================
# LOAD JSON FILE
# =========================================

def load_json(file_path):

    try:

        with open(
            file_path,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)

    except Exception as e:

        print(f"JSON Error: {e}")

        return {}


# =========================================
# FORMAT TIMETABLE
# =========================================

def format_timetable(timetable, timings):

    response = "\n📅 WEEKLY TIMETABLE\n"

    response += "\n" + "━" * 35 + "\n"

    for day, subjects in timetable.items():

        response += f"\n📘 {day.upper()}\n\n"

        for hour, subject in subjects.items():

            if subject:

                timing = timings.get(
                    f"hour_{hour}",
                    ""
                )

                response += (
                    f"{hour}. "
                    f"{timing} "
                    f"→ {subject}\n"
                )

        response += "\n"

    return response


# =========================================
# FORMAT TODAY TIMETABLE
# =========================================

def format_today_timetable(
    timetable,
    timings
):

    today = datetime.now() \
        .strftime("%a") \
        .upper()[:3]

    if today not in timetable:

        return "No timetable available for today."

    response = (
        f"\n📅 TODAY'S TIMETABLE "
        f"({today})\n"
    )

    response += "\n" + "━" * 35 + "\n\n"

    for hour, subject in timetable[today].items():

        if subject:

            timing = timings.get(
                f"hour_{hour}",
                ""
            )

            response += (
                f"{hour}. "
                f"{timing} "
                f"→ {subject}\n"
            )

    return response


# =========================================
# FORMAT EXAMS
# =========================================

def format_exams(schedule):

    if not schedule:

        return "No exams available."

    response = "\n📝 UPCOMING EXAMS\n"

    response += "\n" + "━" * 35 + "\n\n"

    for i, item in enumerate(schedule, start=1):

        date = item.get(
            "date_text",
            "No Date"
        )

        subject = item.get(
            "course_name",
            "Unknown Subject"
        )

        response += (
            f"{i}. "
            f"{date} "
            f"→ {subject}\n"
        )

    return response


# =========================================
# FORMAT NOTIFICATIONS
# =========================================

def format_notifications(data):

    if not isinstance(data, list) or not data:

        return "No new notifications."

    response = "\n🔔 LATEST NOTIFICATIONS\n"

    response += "\n" + "━" * 35 + "\n\n"

    for i, item in enumerate(data, start=1):

        msg = item.get(
            "message",
            ""
        )

        typ = item.get(
            "type",
            "General"
        )

        response += (
            f"{i}. "
            f"[{typ}] "
            f"{msg}\n"
        )

    return response


# =========================================
# MAIN CHATBOT FUNCTION
# =========================================

def chatbot_response(user_input):

    user_input = \
        user_input.lower().strip()


    # =====================================
    # LOAD DATA
    # =====================================

    timetable_data = load_json(
        TIMETABLE_FILE
    )

    exam_data = load_json(
        EXAM_FILE
    )

    notification_data = load_json(
        DATA_FILE
    )


    # =====================================
    # GREETINGS
    # =====================================

    greetings = [
        "hi",
        "hello",
        "hey"
    ]

    if any(
        word in user_input
        for word in greetings
    ):

        return (
            "Hello 👋\n"
            "How can I help you today?"
        )


    # =====================================
    # THANKS
    # =====================================

    if any(
        word in user_input
        for word in [
            "thank",
            "thanks",
            "thx"
        ]
    ):

        return "You're welcome 😊"


    # =====================================
    # HOW ARE YOU
    # =====================================

    if "how are you" in user_input:

        return (
            "I'm doing great 😊\n"
            "Ready to help you."
        )


    # =====================================
    # BYE
    # =====================================

    if any(
        word in user_input
        for word in [
            "bye",
            "goodbye"
        ]
    ):

        return "Goodbye 👋"


    # =====================================
    # FULL TIMETABLE
    # =====================================

    if (
        "timetable" in user_input
        and "today" not in user_input
    ):

        timetable = timetable_data.get(
            "timetable",
            {}
        )

        timings = timetable_data.get(
            "timings",
            {}
        )

        if not timetable:

            return "No timetable available."

        return format_timetable(
            timetable,
            timings
        )


    # =====================================
    # TODAY TIMETABLE
    # =====================================

    if (
        "today timetable" in user_input
        or "today class" in user_input
    ):

        timetable = timetable_data.get(
            "timetable",
            {}
        )

        timings = timetable_data.get(
            "timings",
            {}
        )

        return format_today_timetable(
            timetable,
            timings
        )


    # =====================================
    # EXAMS
    # =====================================

    if (
        "exam" in user_input
        or "tests" in user_input
    ):

        schedule = exam_data.get(
            "schedule",
            []
        )

        return format_exams(schedule)


    # =====================================
    # NEXT EXAM
    # =====================================

    if "next exam" in user_input:

        schedule = exam_data.get(
            "schedule",
            []
        )

        if not schedule:

            return "No upcoming exams."

        next_exam = schedule[0]

        return (
            f"📝 NEXT EXAM\n\n"
            f"{next_exam.get('date_text')}\n"
            f"→ "
            f"{next_exam.get('course_name')}"
        )


    # =====================================
    # NOTIFICATIONS
    # =====================================

    if (
        "notification" in user_input
        or "update" in user_input
        or "announcement" in user_input
    ):

        return format_notifications(
            notification_data
        )


    # =====================================
    # DATE
    # =====================================

    if "date" in user_input:

        return datetime.now().strftime(
            "📅 Today's date is %d-%m-%Y"
        )


    # =====================================
    # TIME
    # =====================================

    if "time" in user_input:

        return datetime.now().strftime(
            "⏰ Current time is %H:%M"
        )


    # =====================================
    # HELP
    # =====================================

    if "help" in user_input:

        return (
            "\n🤖 AVAILABLE COMMANDS\n\n"

            "• timetable\n"
            "• today timetable\n"
            "• exams\n"
            "• next exam\n"
            "• notifications\n"
            "• date\n"
            "• time\n"
        )


    # =====================================
    # DEFAULT
    # =====================================

    return (
        "Sorry 😅\n"
        "I didn't understand that.\n\n"
        "Try:\n"
        "• timetable\n"
        "• exams\n"
        "• notifications"
    )