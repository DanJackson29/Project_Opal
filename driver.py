import commands
import pyttsx3
import sys


while True:
    print("What can I help you with today?")

    #    r = sr.Recognizer()
    # initialize recognizer
    #    with sr.Microphone() as source:
    #        r.adjust_for_ambient_noise(
    #            source, duration=1
    #        )  # mention source it will be either Microphone or audio files.3

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
    else:
        findCommand(command)
