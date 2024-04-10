import datetime


def wish():
    hour = int(datetime.datetime.now().hour)
    if hour > 0 and hour < 12:
        return "Morning"
    elif hour >= 12 and hour < 16:
        return "Afternoon"
    else:
        return "Evening"