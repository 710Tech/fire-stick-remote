import json
import queue
import subprocess
import sounddevice as sd
from vosk import Model, KaldiRecognizer

FIRE_STICK = "192.168.40.203:5555"
MODEL_PATH = "vosk-model-small-en-us-0.15"

audio_queue = queue.Queue()


def callback(indata, frames, time, status):
    audio_queue.put(bytes(indata))


def adb_key(key):
    subprocess.run([
        "adb",
        "-s",
        FIRE_STICK,
        "shell",
        "input",
        "keyevent",
        key
    ])


def open_htc():
    subprocess.run([
        "adb",
        "-s",
        FIRE_STICK,
        "shell",
        "monkey",
        "-p",
        "com.htctv.tv.platform",
        "1"
    ])


def handle_command(text):
    print("Heard:", text)

    if "open htc" in text or "htc" in text:
        print("Opening HTC TV Max")
        open_htc()

    elif "home" in text:
        print("Home")
        adb_key("KEYCODE_HOME")

    elif "back" in text:
        print("Back")
        adb_key("KEYCODE_BACK")

    elif "up" in text:
        print("Up")
        adb_key("KEYCODE_DPAD_UP")

    elif "down" in text:
        print("Down")
        adb_key("KEYCODE_DPAD_DOWN")

    elif "left" in text:
        print("Left")
        adb_key("KEYCODE_DPAD_LEFT")

    elif "right" in text:
        print("Right")
        adb_key("KEYCODE_DPAD_RIGHT")

    elif "select" in text or "okay" in text or text == "ok":
        print("Select")
        adb_key("KEYCODE_DPAD_CENTER")

    elif "play" in text or "pause" in text:
        print("Play/Pause")
        adb_key("KEYCODE_MEDIA_PLAY_PAUSE")


print("Connecting to Fire Stick...")
subprocess.run([
    "adb",
    "connect",
    FIRE_STICK
])

print("Loading voice model...")
model = Model(MODEL_PATH)

recognizer = KaldiRecognizer(
    model,
    16000
)

print("VOICE CONTROL READY")
print("Say: open HTC, home, back, up, down, left, right, select, play, pause")
print("Press Ctrl+C to stop")

with sd.RawInputStream(
    samplerate=16000,
    blocksize=8000,
    dtype="int16",
    channels=1,
    callback=callback
):

    while True:
        data = audio_queue.get()

        if recognizer.AcceptWaveform(data):
            result = json.loads(recognizer.Result())
            text = result.get("text", "").strip()

            if text:
                handle_command(text)

        else:
            partial = json.loads(recognizer.PartialResult())
            text = partial.get("partial", "").strip()

            if text:
                print("Listening:", text)
