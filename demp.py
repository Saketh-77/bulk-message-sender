import pywhatkit
from datetime import datetime

#print(datetime.now().minute)
numbers = [
    "+919381396591",
    "+919182595469",
    "+917416593482",
]

counter = len(numbers)
def is_last_message(counter):

    return counter == 0

for number in numbers:
    scheduled_hour = datetime.now().hour
    scheduled_minute = 0
    if not is_last_message(counter):
        scheduled_minute = (datetime.now().minute + 2)%60
    else:
        scheduled_minute = (datetime.now().minute + 4)%60
    
    pywhatkit.sendwhatmsg(f"{number}",f"Message ID #{counter}! This is an automated test message which is scheduled to deliver at {scheduled_hour}:{scheduled_minute}",scheduled_hour,scheduled_minute)
    counter = counter - 1

    # Need to autoclose the tab after each message is sent