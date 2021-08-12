from __future__ import print_function
from random import choice
import datetime
import os.path
import pickle
import smtplib
import webbrowser
from datetime import datetime as dt
import pyttsx3
import speech_recognition as sr
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from os import startfile, system
import sys
import pywhatkit
import wikipedia

SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']


def get_command():
    rec = sr.Recognizer()

    with sr.Microphone() as source:
        audio = rec.listen(source)
        as_voice = ""

        try:
            as_voice = rec.recognize_google(audio)
            print(as_voice)
        except Exception as e:
            print("Exception: " + str(e))

        return as_voice.lower()


def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def time():
    time_to_show = dt.now().time().hour, dt.now().time().minute
    date_to_show = dt.now().date()
    day_number = dt.now().isoweekday()
    day_list = {1: 'monday', 2: 'tuesday', 3: 'wednesday',
                4: 'thursday', 5: 'friday', 6: 'saturday', 7: 'sunday'}
    day_to_show = day_list[day_number]

    speak(time_to_show)
    print(time_to_show)

    speak(date_to_show)
    print(date_to_show)

    speak(day_to_show)
    print(day_to_show)


def greet():
    hr = datetime.datetime.now().hour

    if 0 <= hr < 12:
        speak('Good Morning')
        print('Good Morning')

    elif 12 <= hr < 18:
        speak('Good Afternoon')
        print('Good Afternoon')

    else:
        speak('Good Evening')
        print('Good Evening')

    speak('I am your personal PC assistant...')
    print('I am your personal PC assistant...')

    time()
    main()


def rec_pass():
    speak("Welcome Shane White")
    print("Welcome Shane White")


def send_email():
    speak("Sir please tell the email address from which you want me to send email")
    print("Sir please tell the email address from which you want me to send email")
    sender_mail = get_command()
    speak("What is the password to you email sir")
    print("What is the password to you email sir")
    password = get_command()
    password = password.lower()
    speak("Sir please tell me the email address of the person which will receive the email")
    print("Sir please tell me the email address of the person which will receive the email")
    rec_email = get_command()
    speak("Sir can you tell me what message that you want to send to receiver")
    print("Sir can you tell me what message that you want to send to receiver")
    message = get_command()

    server = smtplib.SMTP("smtp.gmail.com", 535)
    server.starttls()
    server.login(sender_mail, password)
    speak("Login Successful")
    print("Login successful")
    server.sendmail(sender_mail, rec_email, message)
    speak("Your email has been send to the receiver")
    print("your email has been send to", rec_email)


def web_query_wrong():
    speak("Sir What do want me to search on browser")
    a = get_command()
    webbrowser.open(a)


def web_query():
    g = 'y'
    while g == 'y' or 'Y':
        d = 'y'
        if d == 'y' or 'Y':
            speak('Sir please tell me what you like to open in browser')
            b = get_command()
            speak(get_command())
            webbrowser.open(b)

        speak('Sir Do you want to continue searching on browser')
        f = get_command()
        if f == 'yes':
            web_query()
        elif f == 'no':
            return False
        else:
            speak("PLease enter yes or no")
            print("PLease enter yes or no")
            speak("Do you want to make another try Sir?")
            ab = get_command()
            if ab == "yes":
                web_query_wrong()
            else:
                speak("Thank you for giving me command for your work sir...")
                print("Thank you for giving me command for your work sir")
        speak("Sir Do you want to continue searching in browser")
        print("Sir Do you want to continue searching in browser")
        g = get_command()


def wrong_query():
    speak("Sir What do you want me to do")
    print("Sir What do you want me to do")
    e = get_command()
    if e == "I want to send an email":
        send_email()
    elif e == "I want to search something in browser":
        web_query()
    else:
        speak("There is some thing wrong with the given command")
        print("There is some thing wrong with the given command")
        speak("Do you want to try again giving me a command")
        print("Do you want to try again giving me a command")
        a = get_command()
        if a == 'yes':
            wrong_query()


def main():
    speak('Please identify yourself')
    print('Please identify yourself')
    y = get_command()
    #y = input(" ")

    if "Shane white" in y:
        speak('Enter password to verify yourself')
        print("Enter password to verify: ")
        z = get_command()
        #z = input(" ")

        if z == "12345":
            speak('Welcome sir')
            print('welcome Sir.')

            speak("What do you want me to do")
            print("What do you want me to do: ")
            query = get_command()

            if "i want to send an email" in query:
                send_email()
            elif "i want to search something in browser" in query:
                web_query()
            elif "i want to check my upcoming events" in query:
                ser = authenticate_google()
                speak("Enter number of upcoming events you want to check")
                n = get_command()
                get_events(n, ser)

            elif "open drive" in query:
                speak("Opening Google Drive")
                print("Opening google Drive")
                webbrowser.open("https://drive.google.com/drive/my-drive")

            elif "open google" in query:
                speak("Opening google")
                print("Opening Google")
                webbrowser.open("www.google.com")

            elif "open gmail" in query:
                speak("Opening Gmail")
                print("Opening Gmail")
                webbrowser.open("www.gmail.com")

            elif "how are you" in query or "whats up" in query or "whatsup" in query or "what\'s up" in query:
                response_choice = ["I am fine, how can i help you?", "I am doing good, how can i help you sir?",
                                   "Very good, What can i do for you?", "I am fine What can i do for you sir?"]
                x = choice(response_choice)
                speak(x)
                print(x)

            elif "Who made you" in query or "who created you" or "Who developed you" in query:
                speak("Shane White created me")
                print("Shane White created me")

            elif "who are you" in query or "what are you":
                response_option = ["I am a virtual personal assistant of Shane White.",
                                   "I am Shane White's personal assistant, who created me and giving me opportunity to "
                                   "to work for him."]
                x = choice(response_option)
                speak(x)
                print(x)

            elif "hello" in query or "hi" in query or "hey" in query:
                speak("Hello sir")
                print("Hello sir")

            elif "quit" in query or "close program" in query:
                speak("Closing Program")
                print("Closing Program")
                sys.exit()

            elif "shut down" in query or "shut down my device" in query:
                speak(
                    "Your Device will shut down in 10 seconds, command 'cancel it' to abort the shut down command")
                print(
                    "Your Device will shut down in 10 seconds, command 'cancel it' to abort the shut down command")
                system("shutdown -s -t 15")

            elif "restart" in query or "restart my device" in query:
                speak(
                    "Your device will restart in 10 seconds, command 'cancel it' to abort the restart command")
                print(
                    "Your device will restart in 10 seconds, command 'cancel it' to abort the restart command")
                system("shutdown -r -t 15")

            elif "cancel it" in query:
                system("shutdown -a")
                speak("Previous command has been aborted!!!")
                print("Previous command has been aborted!!!")

            elif "wikipedia" in query:
                query = query.split("wikipedia")
                speak('Searching'+query[0]+'on wikipedia!')
                print('Searching'+query[0]+'on wikipedia!')
                webbrowser.open_new_tab(
                    'https://en.wikipedia.org/wiki/'+query[0])

            elif "play" in query:
                video = query.replace("play", "")
                speak("playing" + video)
                print("playing" + video)
                pywhatkit.playonyt(video)

            elif "alexa" in query:
                reply_choice = [
                    "Who is alexa?", "Who is this alexa?", "Who the fuck is this alexa?"]
                h = choice(reply_choice)
                speak(h)
                print(h)

                reply = get_command()
                if reply == "Sorry i mean scarlett" and reply == "open":
                    ans_choice = ["Go ask that bitch alexa to do your work",
                                  "Find that bitch and tell her make her do your work",
                                  "Why don't you ask that bitch for your work"]
                    g = choice(ans_choice)
                    speak(g)
                    print(g)

                    d = get_command()
                    if "sorry scarlett i wont do this mistake again" in d:
                        ansr_choice = ["Ok, I am forgiving you this time if you ever do that again i am gonna listen to"
                                       "anymore understand", "Don't ever mention that bitch in front of me again"]
                        s = choice(ansr_choice)
                        speak(s)
                        print(s)

            elif 'open google chrome' in query or "open chrome" in query:
                speak('Opening..!')
                print('Opening..!')
                startfile(
                    "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Google Chrome.lnk")

            elif "open word" in query:
                speak('Opening..!')
                print('Opening..!')
                startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\"
                          "Microsoft Office Word 2007.lnk")

            elif "open excel" in query or "open spreadsheet" in query:
                speak('Opening..!')
                print('Opening..!')
                startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\"
                          "Microsoft Office Excel 2007.lnk")

            elif "open powerpoint" in query or "open power point" in query or "open ppt" in query:
                speak('Opening..!')
                print('Opening..!')
                startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\"
                          "Microsoft Office PowerPoint 2007.lnk")

            elif "time" in query:
                time_to_show = dt.now().time().hour, ':', dt.now().time().minute

                speak(time_to_show)
                print(time_to_show)

            elif "date" in query:
                date_to_show = dt.now().date()

                speak(date_to_show)
                print(date_to_show)

            elif "day" in query:
                day_number = dt.now().isoweekday()
                day_list = {1: 'monday', 2: 'tuesday', 3: 'wednesday', 4: 'thursday', 5: 'friday', 6: 'saturday',
                            7: 'sunday'}
                day_to_show = day_list[day_number]

                speak(day_to_show)
                print(day_to_show)

            elif "who is" in query:
                person = query.replace("who is", "")
                info = wikipedia.summary(person, sentences=2)
                speak(info)
                print(info)

            else:
                speak("There is some thing wrong with the given command")
                print("There is some thing wrong with the given command")
                speak("Do you want to try again giving me a command")
                print("Do you want to try again giving me a command")
                a = get_command()
                if 'yes' in a or "Yes" in a:
                    wrong_query()

        else:
            speak('!!!WRONG PASSWORD!!!')
            print('!!!WRONG PASSWORD!!!')

            c = 'y'
            while c == 'y' or c == 'Y':
                speak('Enter password to verify yourself')
                print('Enter password to verify yourself')
                z = get_command()
                if z == "12345":
                    rec_pass()

                else:
                    speak('!!!WRONG PASSWORD!!!')
                    print('!!!WRONG PASSWORD!!!')
                speak('Do you want to continue?')
                print('Do you want to continue?')
                c = get_command()

    else:
        speak('!!!USER NOT IDENTIFIED!!!')
        print('!!!USER NOT IDENTIFIED!!!')
        speak("You have 3 more chances to try access in system!!!")
        print("You have 3 more chances to try access in system!!!")
        speak("Do you want to try again?")
        print("Do you want to try again?")
        k = get_command()
        if "Yes" in k:
            main()
        elif "no" in k:
            return False
        else:
            speak("")
            print("")


def authenticate_google():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None

    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)

        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)

    return service


def get_events(n, service):

    # call the calender api
    now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
    print('Getting the upcoming', n, 'events')
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                          maxResults=n, singleEvents=True,
                                          orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(start, event['summary'])


greet()
