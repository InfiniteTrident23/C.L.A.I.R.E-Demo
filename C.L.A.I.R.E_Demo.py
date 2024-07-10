import datetime
import os
import random
import smtplib
import subprocess
#import pyfirmata
import time
import webbrowser

import psutil
import pyttsx3
import speech_recognition as sr
import wikipedia

#from lsHotword import ls    
# import PyAudio

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
voice_id = "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-US_ZIRA_11.0"
engine.setProperty('voice', voice_id)
engine.runAndWait()
engine.stop()

emails = {
    "xyz":"xyz@gmail.com",
    "abc":"abc@outlook.com"
}

def checkIfProcessRunning(processName):
    '''
    Check if there is any running process that contains the given name processName.
    '''
    #Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False;

def speaking(audio):
    engine.say(audio)
    engine.runAndWait()

def take_command():
    # It takes microphone input from user

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Processing....")
        query = r.recognize_google(audio, language='en-in')
        print("User said: " + query)
    except Exception as e:
        print(e)
        return "None"
    return query

def shutdown():
    print('Are You Sure?')
    speaking('Are You Sure?')
    reply = take_command().lower()
    if "yes" in reply or 'ok' in reply or 'yup' in reply or 'ya' in reply:
        print('Shutting Down!.')
        speaking('Ok! Shutting Down in a Minute.')
        os.system('shutdown -s')
        exit(0)
    else:
        print("Okay! Don't Worry.")
        speaking("Okay! Don't Worry")

def wish_me():
    hour = int(datetime.datetime.now().hour)
    if hour < 12 and hour >= 0:
        print("Good Morning,")
        speaking("Good Morning,")
    elif hour >= 12 and hour <= 17:
        print("Good Afternoon,")
        speaking("Good Afternoon,")
    elif hour >= 17:
        print("Good Evening,")
        speaking("Good Evening,")
    print("I am Claire. How may I be of assistance?")
    speaking("I am Claire. How may I be of assistance?")

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('Your sending email id Here', '<Your email password Here>') #Change This
    server.sendmail('Your sending email id Here', to, content) #Change This
    server.close()

def note(text):
    date = datetime.datetime.now()
    file_name = str(date).replace(":", "-")+ "-note.txt"
    with open(file_name, "w") as f:
        f.write(text)                               

    subprocess.Popen(["notepad.exe", file_name])

def Work():
    webbrowser.open('<Website you want to open>', new=2) #Change This       

def AutoOn2():
    strtime = int(datetime.datetime.now().strftime("%H"))
    strtime2 = int(datetime.datetime.now().strftime("%M"))
    if strtime == 18 and 45 < strtime2 < 59:
        if checkIfProcessRunning('discord'):
            pass
        else:
            print("Will you be gaming today?")
            speaking("Will you be gaming today?")
            gaming_confirmation = take_command()
            if 'yes' in gaming_confirmation:
                    DiscordPath = "C:\\Users\\admin\\AppData\\Local\\Discord\\app-0.0.308\\Discord.exe"
                    os.startfile(DiscordPath)
                    print("Which Game are you going to play today?")
                    speaking("Which Game are you going to play today?")
                    game_name = take_command().lower()
                    bluestackpath = "C:\\Program Files\\BlueStacks\\Bluestacks.exe"
                    if 'among us' in game_name:
                        print("Opening Bluestacks for Among us")
                        speaking("Opening Bluestacks for Among us")
                        os.startfile(bluestackpath)
                    elif 'minecraft' in game_name:
                        print("Opening Bluestacks for Minecraft")
                        speaking("Opening Bluestacks for Minecraft")
                        os.startfile(bluestackpath)
                    elif 'rocket league' in game_name:
                        print("Opening Epic Games Launcher for Rocket League....")
                        speaking("Opening Epic Games Launcher for Rocket League")
                        EpicPath = "C:\\Program Files (x86)\\Epic Games\\Launcher\\Portal\\Binaries\Win32\\EpicGamesLauncher.exe"
                        os.startfile(EpicPath)
            if 'no' in gaming_confirmation:
                print('ok')
                speaking('ok')
    else:
        pass

if __name__ == '__main__':
    wish_me()
    while True:
        strtime = int(datetime.datetime.now().strftime("%H"))
        strtime2 = int(datetime.datetime.now().strftime("%M"))
        if checkIfProcessRunning('teams'):
            pass
        else:
            if strtime == 8 and 45 < strtime2 < 59:
                print("Time to Work, So Opening Teams and ERP...")
                speaking("Time to Work, So Opening Teams and ERP")
                Work()
        AutoOn2()
        def orders():
            query = take_command().lower()
            if 'wikipedia' in query:
                print("Searching Wikipedia....")
                speaking("searching Wikipedia")
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speaking("According to wikipedia")
                print(results)
                speaking(results)

            elif 'open spotify' in query:
                print("Opening Spotify....")
                speaking("Opening Spotify")
                webbrowser.open('https://open.spotify.com/', new=2)

            elif 'open youtube' in query:
                print("Opening YouTube....")
                speaking("Opening YouTube")
                webbrowser.open('https://www.youtube.com/', new=2)

            elif 'work time' in query:
                print("Ready for work?")
                speaking("Ready for work?")
                Work()

            elif 'open browser' in query:
                print("Opening Firefox....")
                speaking("Opening Firefox")
                BrowserPath = "C:\\Program Files\\Mozilla Firefox\\firefox.exe" # You can specify any other browser here as well
                os.startfile(BrowserPath)

            elif 'open whatsapp' in query:
                print("Opening WhatsApp....")
                speaking("Opening WhatsApp")
                webbrowser.open('https://web.whatsapp.com/', new=2)

            elif 'open google' in query:
                print("Opening Google....")
                speaking("Opening Google")
                webbrowser.open('https://www.google.com/', new=2)

            elif 'open erp' in query:
                print('Opening ERP....')
                speaking("Opening ERP")
                webbrowser.open('<Your ERP website here>', new=2) # Change this

            elif 'google search' in query:
                print('Googling....')
                speaking('Googling')
                query2 = query.replace("google search", "")
                url = 'https://google.com/search?q=' + query2
                webbrowser.get().open(url)
                print("Here is what I found for " + query2)
                speaking("Here is what I found for " + query2)

            elif 'youtube' in query:
                print('Searching YouTube....')
                speaking('Searching YouTube')
                query3 = query.replace("youtube", "")
                url2 = 'https://www.youtube.com/results?search_query=' + query3
                webbrowser.get().open(url2)
                print("Here is what I found for " + query3 + "on YouTube")
                speaking("Here is what I found for " + query3 + "on youtube")

            elif 'open hotstar' in query:
                print("Opening Hotstar.....")
                speaking("Opening Hotstar")
                webbrowser.open('https://www.hotstar.com/in', new=2)

            elif 'find location' in query:
                print('What\'s the location?')
                speaking('What\'s the location?')
                location = take_command()
                url = "https://google.nl/maps/place/" + location + "/&amp;"
                webbrowser.get().open(url)
                print("Here\'s the location of " + location)
                speaking("Here\'s the location of " + location)

            elif 'terminate program' in query:  
                print("Thank You for using Claire.\nI Hope I was of assistance!")
                speaking("Thank You for using Claire. I Hope I was of assistance!")
                hour = int(datetime.datetime.now().hour)
                if 12 > hour >= 0:
                    print("Have a Good day!")
                    speaking("Have a Good day!")
                    exit()

                elif 12 <= hour <= 17:
                    print("Have a pleasant evening!")
                    speaking("Have a pleasant evening!")
                    exit()

                elif hour >= 17:
                    print("Have a good night!")
                    speaking("Have a good Night!")
                    exit()
            elif 'bye' in query:
                print("Thank You for using Claire.\nI Hope I was of assistance!")
                speaking("Thank You for using Claire. I Hope I was of assistance!")
                hour = int(datetime.datetime.now().hour)
                if 12 > hour >= 0:
                    print("Have a Good day!")
                    speaking("Have a Good day!")
                    exit()

                elif 12 <= hour <= 17:
                    print("Have a pleasant evening!")
                    speaking("Have a pleasant evening!")
                    exit()

                elif hour >= 17:
                    print("Have a good night!")
                    speaking("Have a good Night!")
                    exit()
            elif 'adios' in query:
                print("Thank You for using Claire.\nI Hope I was of assistance!")
                speaking("Thank You for using Claire. I Hope I was of assistance!")
                hour = int(datetime.datetime.now().hour)
                if 12 > hour >= 0:
                    print("Have a Good day!")
                    speaking("Have a Good day!")
                    exit()

                elif 12 <= hour <= 17:
                    print("Have a pleasant evening!")
                    speaking("Have a pleasant evening!")
                    exit()

                elif hour >= 17:
                    print("Have a good night!")
                    speaking("Have a good Night!")
                    exit()
            elif 'goodbye' in query:
                print("Thank You for using Claire.\nI Hope I was of assistance!")
                speaking("Thank You for using Claire. I Hope I was of assistance!")
                hour = int(datetime.datetime.now().hour)
                if 12 > hour >= 0:
                    print("Have a Good day!")
                    speaking("Have a Good day!")
                    exit()

                elif 12 <= hour <= 17:
                    print("Have a pleasant evening!")
                    speaking("Have a pleasant evening!")
                    exit()

                elif hour >= 17:
                    print("Have a good night!")
                    speaking("Have a good Night!")
                    exit()
            elif 'good night' in query:
                print("Thank You for using Claire.\nI Hope I was of assistance!")
                speaking("Thank You for using Claire. I Hope I was of assistance!")
                hour = int(datetime.datetime.now().hour)
                if 12 > hour >= 0:
                    print("Have a Good day!")
                    speaking("Have a Good day!")
                    exit()

                elif 12 <= hour <= 17:
                    print("Have a pleasant evening!")
                    speaking("Have a pleasant evening!")
                    exit()

                elif hour >= 17:
                    print("Have a good night!")
                    speaking("Have a good Night!")
                    exit()
            elif 'sayonara' in query:
                print("Thank You for using Claire.\nI Hope I was of assistance!")
                speaking("Thank You for using Claire. I Hope I was of assistance!")
                hour = int(datetime.datetime.now().hour)
                if 12 > hour >= 0:
                    print("Have a Good day!")
                    speaking("Have a Good day!")
                    exit()

                elif 12 <= hour <= 17:
                    print("Have a pleasant evening!")
                    speaking("Have a pleasant evening!")
                    exit()

                elif hour >= 17:
                    print("Have a good night!")
                    speaking("Have a good Night!")
                    exit()

            elif 'take a note' in query:
                print('What should I say?')
                speaking('What should I say?')
                o = sr.Recognizer()
                with sr.Microphone() as source2:
                    o.pause_threshold = 1
                    audio2 = o.listen(source2)
                try:
                    m = o.recognize_google(audio2, language='en-in').lower()
                    print(m)                                
                except Exception as e:
                    # print(e)
                    print("Say that again please...") 
                note(m)

            elif 'open discord' in query:
                try:
                    print("Opening Discord...")
                    speaking("Opening Discord")
                    DiscordPath = "C:\\Users\\admin\\AppData\\Local\\Discord\\app-0.0.308\\Discord.exe" #Specify your own Path for Discord.exe
                    os.startfile(DiscordPath)
                except Exception as e:
                    print(e)

            elif 'close discord' in query:
                if checkIfProcessRunning('discord'):
                    print("Closing Discord...")
                    speaking("Closing Discord")
                    os.system("TASKKILL /F /IM discord.exe")
                else:
                    print("Discord is not running.")
                    speaking("Discord is not running.")

            elif 'is discord running' in query:
                if checkIfProcessRunning('discord'):
                    print('Yes, Discord is running')
                else:
                    print('No, Discord is not running')

            elif 'open epic games' in query:
                print("Opening Epic Games Launcher....")
                speaking("Opening Epic Games Launcher")
                EpicPath = "C:\\Program Files (x86)\\Epic Games\\Launcher\\Portal\\Binaries\Win32\\EpicGamesLauncher.exe" #Specify your own Path for Epic games
                os.startfile(EpicPath)

            elif 'open teams' in query:
                try:
                    print("Opening Teams...")
                    speaking("Opening Teams")
                    teamspath = "C:\\Users\\admin\\AppData\\Local\\Microsoft\\Teams\\current\\Teams.exe" #Specify your own path for Teams
                    os.startfile(teamspath)
                except Exception as e:
                    print(e)

            elif 'close teams' in query:
                if checkIfProcessRunning('teams'):
                    print("Closing Teams...")
                    speaking("Closing Teams")
                    os.system("TASKKILL /F /IM Teams.exe")
                else:
                    print("Teams is not running.")
                    speaking("Teams is not running.")

            elif 'open zoom' in query:
                print("Opening Zoom...")
                speaking("Opening Zoom")
                zoompath = "C:\\Users\\admin\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe" #Specify your own path for zoom meetings
                os.startfile(zoompath)

            elif 'open source code' in query:
                print("Opening Source Code...")
                speaking("Opening Source Code")
                Code_path = "C:\\Users\\admin\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe" #Specify the path to the code downloaded on your machine
                os.startfile(Code_path)

            elif 'open bluestacks' in query:
                print("Opening Bluestacks...")
                speaking("Opening Bluestacks")
                bluestackpath = "C:\\Program Files\\BlueStacks\\Bluestacks.exe" #Specify the path to your own Bluestack or any other program
                os.startfile(bluestackpath)
            
            elif 'how are you' in query:
                print('I am fine. How are you doing?')
                speaking("I am fine, How are you doing?")

            elif 'what\'s up' in query:
                print("Nothing much. Just hangin\' around. Assisting you.")
                speaking("Nothing much. Just hanging around. Assisting you.")

            elif 'introduce yourself' in query:
                def Intro():
                    print("I am Claire. A local pc assistant designed by InfiniteTrident.\nWould you like to know what all I can do?")
                    speaking("I am Claire. A local pc assistant designed by Infinite Trident.\n Would you like to know what all I can do?") 
                    y = sr.Recognizer()
                    with sr.Microphone() as source1:
                        y.pause_threshold = 1
                        audio1 = y.listen(source1)
                    try:
                        t = y.recognize_google(audio1, language='en-in')
                        print(t)
                    except Exception as e:
                        # print(e)
                        print("Say that again please...")
                    if 'yes' in t:
                        print("I was designed to be able to do the following things:\n  1.I can open sites such as YouTube or google.\n  2.I can do brief wikipedia searchs.\n  3.I can find location of a place on Google maps.\n  4.I can take notes from voice command.\n  5.I can tell you the exact time.\n  6.I can send email to people defined to me by you all by voice command.\n")
                        speaking("I was designed to be able to do the following things: Number 1 I can open sites such as YouTube or google. Number 2 I can do brief wikipedia searchs. Number 3 I can find location of a place on Google maps. number 4 I can take notes from voice command. number 5 I can tell you the exact time. number 6 I can send email to people defined to me by you all by voice command.")
                    elif 'no' in t:
                        print("Okay.")
                        speaking('Okay')
                        orders()

                Intro()

            # Emails can only be sent to those defined in the emails dictionary at the beginning of the code
            elif 'email to xyz' in query:
                try:
                    print('What should I say?')
                    speaking('What should I say?')
                    content = take_command()
                    to = emails["xyz"]
                    sendEmail(to, content)
                    print("Email has been sent!")
                    speaking("Email has been sent!")
                except Exception as e:
                    print(e)
                    print('Sorry, Something went wrong :(')
                    speaking('Sorry Something went wrong')
            elif 'email to abc' in query:
                try:
                    print('What should I say?')
                    speaking('What should I say?')
                    content = take_command()
                    to = emails["abc"]
                    sendEmail(to, content)
                    print("Email has been sent!")
                    speaking("Email has been sent!")
                except Exception as e: 
                    print(e)
                    print('Sorry, Something went wrong :(')
                    speaking('Sorry Something went wrong')
            

            elif 'time' in query:
                strtime = datetime.datetime.now().strftime("%H:%M:%S")
                print("The time is:" + strtime)
                speaking("The time is:" + strtime)
            
            elif 'remind me that' in query: 
                print('What should I remind you?')
                speaking('What should I remind you?')
                data = take_command()
                data2 = data.replace("I", "you")
                data2 = data2.replace("my", "your")
                data2 = data2.replace("that", "")
                data2 = data2.replace("your", 'my')
                data2 = data2.replace("you are", "I am")
                data2 = data2.replace("you", "me")
                print('You said to remind you that ' + data2)
                speaking('You said to remind you that ' + data2)
                remember = open('data.txt','w')
                remember.write(data2)
                remember.close()

            elif 'tell you to remember' in query:
                remember = open('data.txt', 'r')
                ly = remember.read()
                if ly != "":
                    aq = 'you said to remind you that ' + ly
                    print(aq)
                    speaking(aq)
                    abc = take_command()
                    if 'clear that' in abc:
                        print("ok")
                        speaking("ok")
                        kk = open("data.txt","w")
                        kk.write(ly.replace(ly, ""))
                        kk.close()
                    elif 'ok' in abc:
                        print("Ok")
                        speaking("ok")
                    elif 'thank you' in abc:
                        print("You're welcome.")
                        speaking("you're welcome")
                elif ly == "":
                    print("No, You did not tell me to remember anything")
                    speaking("No, You did not tell me to remember anything")

            elif 'shutdown' in query or 'power off' in query:
                shutdown()

            else:
                print("say that again please")
        
        orders()
        
   