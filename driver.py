import commands
import pyttsx3
import sys


while True:
    print("What can I help you with today?")

    command = input(">").strip().lower().split(" ")

    if "weather" in command:
        commands.runWeatherCommand()
    elif "food" in command:
        print("What can the refridgerator do?")
        command = input(">").strip().lower().split(" ")
        if "add" in command:
            commands.runAddIngredient()
        if "ingred" in command:
            commands.print_current_ingredients()
    elif "done" in command:
        sys.exit()
