import sys
import subprocess

FIRE_STICK = "192.168.40.203:5555"

CHANNELS = {
    "fox": "7",
    "nbc": "10",
    "cbs": "13",
    "abc": "15",
    "tnt": "25",
    "usa": "27",
    "espn": "28",
    "espn2": "29",
    "discovery": "31",
    "comedy": "34",
    "tbs": "47",
    "foxnews": "61",
    "natgeo": "64",
    "id": "71",
    "nfl": "180",
    "redzone": "181"
}

if len(sys.argv) < 2:
    print("Use: python3 channel.py espn")
    print("Or:  python3 channel.py 28")
    sys.exit()

choice = sys.argv[1].lower()

# If we know the channel name, get its number.
# Otherwise use whatever number was entered.
channel = CHANNELS.get(choice, choice)

print("Changing to channel:", channel)

subprocess.run([
    "adb",
    "-s",
    FIRE_STICK,
    "shell",
    "input",
    "text",
    channel
])
