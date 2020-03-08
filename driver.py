import commands
import pyttsx3
import sys
import speech_recognition as sr


def findCommand(command):
    print(command)
    if "weather" in command:
        commands.runWeatherCommand()

    elif "food" in command:
        if "add" in command:
            commands.runAddRecipe()
            return
        elif "get" in command:
            commands.runGetRecipe()
            return
        elif ("delete" in command) or ("remove" in command):
            commands.runDeleteRecipe()
            return

        voiceEngine.say("What would you like to do?")
        voiceEngine.runAndWait()
        newCommand = command + (input(">").strip().lower().split(" "))
        findCommand(newCommand)


voiceEngine = pyttsx3.init()
voiceEngine.setProperty(
    "voice",
    r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0",
)
while True:
    voiceEngine.say("What can I help you with today?")
    voiceEngine.runAndWait()

    #    r = sr.Recognizer()
    # initialize recognizer
    #    with sr.Microphone() as source:
    #        r.adjust_for_ambient_noise(
    #            source, duration=1
    #        )  # mention source it will be either Microphone or audio files.3

    #        audio = r.listen(source)  # listen to the source
    #    print("heard")
    #    try:
    #       text = r.recognize_google(audio)
    #        print("{}".format(text))  # use recognizer to convert our audio into text part.
    #    except:
    #        print("Sorry could not recognize your voice")
    #    command = text.strip().lower().split(" ")
    command = input(">").strip().lower().split(" ")
    if "done" in command:
        sys.exit()
    else:
        findCommand(command)

