import commands
import pyttsx3
import sys

voiceEngine = pyttsx3.init()
voiceEngine.setProperty(
    "voice",
    r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0",
)
print(5)

while True:
    voiceEngine.say("What can I help you with today?")
    voiceEngine.runAndWait()

    command = input(">").strip().lower()
    if command == "weather":
        commands.runWeatherCommand()
    elif command == "done":
        sys.exit()

