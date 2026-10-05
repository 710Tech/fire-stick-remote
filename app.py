from flask import Flask
import subprocess

app = Flask(__name__)

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

def adb_key(key):
    subprocess.run([
        "adb", "-s", FIRE_STICK,
        "shell", "input", "keyevent", key
    ])

def change_channel(value):
    value = value.lower().replace(" ", "")
    channel = CHANNELS.get(value, value)

    if channel.isdigit():
        subprocess.run([
            "adb", "-s", FIRE_STICK,
            "shell", "input", "text", channel
        ])

@app.route("/")
def home():
    return """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Fire Stick Remote</title>
<style>
body {
    background: #111;
    color: white;
    font-family: Arial, sans-serif;
    text-align: center;
    padding: 20px;
}
button {
    width: 95px;
    height: 65px;
    margin: 7px;
    font-size: 18px;
    border-radius: 15px;
    border: none;
}
#channel {
    width: 200px;
    height: 50px;
    font-size: 22px;
    text-align: center;
    border-radius: 12px;
}
.go {
    width: 80px;
    height: 55px;
}
</style>
</head>

<body>

<h1>Fire Stick Remote</h1>

<button onclick="send('up')">↑</button><br>

<button onclick="send('left')">←</button>
<button onclick="send('select')">OK</button>
<button onclick="send('right')">→</button><br>

<button onclick="send('down')">↓</button><br><br>

<button onclick="send('home')">HOME</button>
<button onclick="send('back')">BACK</button><br>

<button onclick="send('playpause')">PLAY / PAUSE</button>

<h2>Channel</h2>

<input
    id="channel"
    placeholder="ESPN or 28"
    autocomplete="off"
>

<button class="go" onclick="channel()">GO</button>

<script>

function send(command) {
    fetch("/" + command);
}

function channel() {
    const value =
        document.getElementById("channel").value;

    fetch("/channel/" + encodeURIComponent(value));
}

document
    .getElementById("channel")
    .addEventListener("keydown", function(event) {
        if (event.key === "Enter") {
            channel();
        }
    });

</script>

</body>
</html>
"""

@app.route("/up")
def up():
    adb_key("KEYCODE_DPAD_UP")
    return "", 204

@app.route("/down")
def down():
    adb_key("KEYCODE_DPAD_DOWN")
    return "", 204

@app.route("/left")
def left():
    adb_key("KEYCODE_DPAD_LEFT")
    return "", 204

@app.route("/right")
def right():
    adb_key("KEYCODE_DPAD_RIGHT")
    return "", 204

@app.route("/select")
def select():
    adb_key("KEYCODE_DPAD_CENTER")
    return "", 204

@app.route("/home")
def press_home():
    adb_key("KEYCODE_HOME")
    return "", 204

@app.route("/back")
def press_back():
    adb_key("KEYCODE_BACK")
    return "", 204

@app.route("/playpause")
def playpause():
    adb_key("KEYCODE_MEDIA_PLAY_PAUSE")
    return "", 204

@app.route("/channel/<value>")
def channel_route(value):
    change_channel(value)
    return "", 204

if __name__ == "__main__":
    subprocess.run([
        "adb",
        "connect",
        FIRE_STICK
    ])

    app.run(
        host="0.0.0.0",
        port=5000
    )
