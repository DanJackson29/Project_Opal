import commands
import pyttsx3
import sys


while True:
    print("What can I help you with today?")

    command = input(">").strip().lower().split(" ")

    if "weather" in command:
        commands.runWeatherCommand()
    # elif "food" in command:
    #     voiceEngine.say("What would you like to do?")
    #     voiceEngine.runAndWait()
    #     command = input(">").strip().lower().split(" ")
    #     if "add" in command:
    #         commands.runAddRecipe()
    #     elif "get" in command:
    #         commands.runGetRecipe()
    elif "done" in command:
        sys.exit()
