import datetime  # Importing the datetime module

# Creating a specific date object for Jan 2, 2025
date = datetime.date(2025, 1, 2)

# Getting today's current date
today = datetime.date.today()

# Creating a specific time object (12:30:00)
time = datetime.time(12, 30, 0)

# Getting the current date and time (down to seconds)
now = datetime.datetime.now()

# Formatting the current date and time to display as HH:MM:SS and DD-MM-YYYY
now = now.strftime("%H:%M:%S \n%d-%m-%Y")

# Creating a target date and time (12 July 2026, 11:12:09 PM)
target_datetime = datetime.datetime(2026, 7, 12, 23, 12, 9)

# Getting the current date and time again to compare with target
current_datetime = datetime.datetime.now()

# Checking if the target date has already passed
if target_datetime < current_datetime:
    print("target date has been passed")
else:
    print("Target date has not passed")
