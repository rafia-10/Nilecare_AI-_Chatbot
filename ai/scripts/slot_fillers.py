import re
from datetime import datetime
import dateparser
import parsedatetime

departments = ["Cardiology", "Neurology", "Orthopedics", "General Medicine", "Pediatrics", "Dermatology", "ENT"]

def extract_name(text):
    words = text.split()
    for word in words:
        if word.istitle():
            return word
    return None

def extract_time(user_input):
    parsed_time = dateparser.parse(user_input)
    if parsed_time:
        return parsed_time.strftime("%I:%M %p")
    return None

def extract_date(text):
    cal = parsedatetime.Calendar()
    time_struct, parse_status = cal.parse(text)
    if parse_status == 1:
        date = datetime(*time_struct[:6])
        return date.strftime("%d/%m/%Y")
    return None

def extract_department(user_input):
    for department in departments:
        if department.lower() in user_input.lower():
            return department
    return None

def fill_appointment_slots(user_input, slot_tracker):
    if not slot_tracker["name"]:
        slot_tracker["name"] = extract_name(user_input)
        if slot_tracker["name"]:
            return False, "What is the appointment date?"

    if not slot_tracker["date"]:
        date = extract_date(user_input)
        if date:
            slot_tracker["date"] = date
            return False, "What time is the appointment?"

    if not slot_tracker["time"]:
        parsed_time = dateparser.parse(user_input, settings={'PREFER_DATES_FROM': 'future'})
        if parsed_time:
            slot_tracker["time"] = parsed_time.strftime("%I:%M %p")
            return False, "What department is that you wanna book?"
        else:
            return False, "Sorry, I couldn't understand the time. Try something like '3:00 pm' or 'tomorrow at 4'."

    if not slot_tracker["department"]:
        department = extract_department(user_input)
        if department:
            slot_tracker["department"] = department
            return True, "Appointment successfully booked!"

    return False, "I didn't quite get that. Can you provide more details?"
