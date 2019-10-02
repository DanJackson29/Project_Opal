import commands
import pyttsx3
import sys
import refrigerator

voiceEngine = pyttsx3.init()
voiceEngine.setProperty(
    "voice",
    r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0",
)

while True:
    voiceEngine.say("What can I help you with today?")
    voiceEngine.runAndWait()

    command = input(">").strip().lower().split(" ")

    if "weather" in command:
        commands.runWeatherCommand()
    elif "food" in command:
        voiceEngine.say("What would you like to do?")
        voiceEngine.runAndWait()
        command = input(">").strip().lower().split(" ")
        if "add" in command:
            commands.runAddRecipe()
        elif "get" in command:
            commands.runGetRecipe()
    elif "done" in command:
        sys.exit()

