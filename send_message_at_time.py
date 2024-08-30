import subprocess
import time
from datetime import datetime, timedelta

# phone #
# for testing
recipient = "insert phone #"

# message to send
message = """FIRST! 👋

I know this is first because it's sent via a Python script running on my computer somewhere... though I'm not exactly sure where I (or my computer, for that matter) will be at this time haha. Happy birthday kid, you are a wonderful person and I always enjoy laughing together. I know you have a great day ahead of ya. Hopefully this worked? 

With love, 
Jacob

🛠️ Oh and here's the source code, since we all know you LOVE coding... right? https://github.com/jacob-tucker/send-birthday-message/blob/main/send_message_at_time.py"""

# Function to send the message using osascript
def send_message(recipient, message):
    script = f'''
    tell application "Messages"
        set targetBuddy to "{recipient}"
        set targetService to 1st service whose service type = iMessage
        set targetBuddy to buddy targetBuddy of targetService
        send "{message}" to targetBuddy
    end tell
    '''
    subprocess.run(["osascript", "-e", script])

# set the target time to midnight (12:00 AM)
# target_time = (datetime.now()).replace(hour=23, minute=57, second=0, microsecond=0)
target_time = (datetime.now() + timedelta(days=1)).replace(hour=0, minute=0, second=0, microsecond=0)

# calculate the number of seconds until midnight
seconds_until_midnight = (target_time - datetime.now()).total_seconds()

# wait until midnight
time.sleep(seconds_until_midnight)

# send the message at midnight
send_message(recipient, message)
