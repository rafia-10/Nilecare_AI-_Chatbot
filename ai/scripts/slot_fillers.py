{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2567cdab-d329-4cd2-b61a-bae769e68aa9",
   "metadata": {},
   "outputs": [],
   "source": [
    "import re\n",
    "from datetime import datetime\n",
    "import dateparser"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "f3d935f2-ce2e-4110-9843-1ca493372f13",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Slot tracker dictionary to store user input for different slots\n",
    "slot_tracker = {\n",
    "    \"name\": None,\n",
    "    \"date\": None,\n",
    "    \"time\": None,\n",
    "    \"department\": None\n",
    "}\n",
    "\n",
    "# List of departments for slot filling (this can be dynamic or fetched from a database)\n",
    "departments = [\"Cardiology\", \"Neurology\", \"Orthopedics\", \"General Medicine\", \"Pediatrics\", \"Dermatology\", \"ENT\"]\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "01576388-7c5d-4f38-9268-4197adae68cf",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Function to extract a name from the user input using a simple regex\n",
    "def extract_name(text):\n",
    "    # Simplified name extraction\n",
    "    words = text.split()\n",
    "    for word in words:\n",
    "        if word.istitle():\n",
    "            return word\n",
    "    return None\n",
    "# extract name\n",
    "def extract_time(user_input):\n",
    "    parsed_time = dateparser.parse(user_input)\n",
    "    if parsed_time:\n",
    "        return parsed_time.strftime(\"%I:%M %p\")\n",
    "    return None\n",
    "# Function to extract the date (improved regex for better date recognition)\n",
    "def extract_date(text):\n",
    "    cal = parsedatetime.Calendar()\n",
    "    time_struct, parse_status = cal.parse(text)\n",
    "    if parse_status == 1:\n",
    "        date = datetime(*time_struct[:6])\n",
    "        return date.strftime(\"%d/%m/%Y\")\n",
    "    return None\n",
    "\n",
    "\n",
    "# Function to extract department from the user input\n",
    "def extract_department(user_input):\n",
    "    # Loop through departments and check if mentioned in user input\n",
    "    for department in departments:\n",
    "        if department.lower() in user_input.lower():\n",
    "            return department\n",
    "    return None\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6a38841f-1e08-4ca8-a334-8b2cec667073",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Function to fill the appointment slots based on the user input\n",
    "def fill_appointment_slots(user_input, slot_tracker):\n",
    "    # Check if the name slot is filled\n",
    "    if not slot_tracker[\"name\"]:\n",
    "        slot_tracker[\"name\"] = extract_name(user_input)\n",
    "        if slot_tracker[\"name\"]:\n",
    "            return False, \"What is the appointment date?\"\n",
    "\n",
    "    # Check if the date slot is filled\n",
    "    if not slot_tracker[\"date\"]:\n",
    "        date = extract_date(user_input)\n",
    "        if date:\n",
    "            slot_tracker[\"date\"] = date\n",
    "            return False, \"What time is the appointment?\"\n",
    "\n",
    "    # Check if the time slot is filled\n",
    "    if not slot_tracker[\"time\"]:\n",
    "        parsed_time = dateparser.parse(user_input, settings={'PREFER_DATES_FROM': 'future'})\n",
    "\n",
    "        if parsed_time:\n",
    "            slot_tracker[\"time\"] = parsed_time.strftime(\"%I:%M %p\")  # format like '03:00 PM'\n",
    "            return False, \"What department is that u wanna book?\"\n",
    "        else:\n",
    "            return False, \"Sorry, I couldn't understand the time. Try something like '3:00 pm' or 'tomorrow at 4'.\"\n",
    "\n",
    "\n",
    "    # Check if the department slot is filled\n",
    "    if not slot_tracker[\"department\"]:\n",
    "        department = extract_department(user_input)\n",
    "        if department:\n",
    "            slot_tracker[\"department\"] = department\n",
    "            return True, \"Appointment successfully booked!\"\n",
    "\n",
    "    return False, \"I didn't quite get that. Can you provide more details?\"\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0e68a31f-b747-4589-91a2-abf844ebf873",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Start the appointment booking process\n",
    "def appointment_booking():\n",
    "    slot_tracker = {\"name\": None, \"department\": None, \"date\": None, \"time\": None}\n",
    "    \n",
    "    print(\"\\nBot: Hi! I'd be happy to help you book a medical appointment.\")\n",
    "    while not all(slot_tracker.values()):\n",
    "        user_input = input(\"You: \")\n",
    "        done, message = fill_appointment_slots(user_input, slot_tracker)\n",
    "        print(\"Bot:\", message)\n",
    "        if done:\n",
    "            break\n",
    "\n",
    "# Just call this anytime to test again\n",
    "appointment_booking()\n",
    "\n",
    "# Print the filled slots for confirmation\n",
    "print(\"\\nFinal appointment details:\")\n",
    "for slot, value in slot_tracker.items():\n",
    "    print(f\"{slot.capitalize()}: {value}\")\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.1"
  },
  "widgets": {
   "application/vnd.jupyter.widget-state+json": {
    "state": {},
    "version_major": 2,
    "version_minor": 0
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
