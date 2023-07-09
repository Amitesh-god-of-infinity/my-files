import pyttsx3      # audio to Infinity
import datetime
import speech_recognition as sr         # pip install speechRecognition   for taking voice commands
import wikipedia
import webbrowser       # for accessing webbrowser of your device...
import os           # accessing your os ...
import smtplib      # You have to enable less secuere apps for sending email through python...

engine = pyttsx3 . init("sapi5")        # sapi5 is the speech API form microsoft ...
voices = engine . getProperty("voices")
engine . setProperty("voice", voices[1] . id)       # voice[1] for girl and voice[0] for boy...

def speak(audio) :
    """
    for Infinity's voice ...
    """
    engine . say(audio)
    engine . runAndWait()

def wish_me() :
    """
    Greeting to master according to time ...
    """
    hour = int(datetime . datetime . now() . hour)
    if hour >= 0 and hour < 12 :
        speak("Good Morning")
    elif hour >= 12 and hour < 18 :
        speak("Good Afternoon")
    else :
        speak("Good Evening")

def take_command() :
    """
    Taking commands form the user ...
    """
    r = sr . Recognizer()
    with sr . Microphone() as source :
        print("Listening...")
        r . pause_threshold = 1
        audio = r . listen(source)

    try :
        print("Recognizing...")
        query = r . recognize_google(audio, language = 'en-in')
        print(f"User said : {query} \n")

    except Exception as e :
        # print(e)
        print("Say that again please : ")
        return "None"
    return query
    
def send_email(to, content) :
    server = smtplib . SMTP("smntp.gmail.com", 587)
    server . ehlo()
    server . starttls()
    server . login("youremail@gmail.com", "Your password")
    server . sendmail("youremail@gmail.com", to, content)
    server . close()

def opening_commands() :
    global query
    if "wikipedia" in query :
        speak("Searching Wikipedia...")
        query = query . replace("wikipedia", "")
        results = wikipedia . summary(query, sentences = 2)
        speak("According to wikipedia...")
        print(results)
        speak(results)
    elif "open youtube" in query :
        speak("Opening Youtube")
        webbrowser . open("youtube.com")
    elif "open google" in query :
        speak("Opening google")
        webbrowser . open("google.com")
    elif "open a typing" in query :
        speak("Opening monkeytype typing website")
        webbrowser . open("monkeytype.com")
    elif "open chat gpt" in query :
        speak("Opening chat gpt")
        webbrowser . open("chat.openai.com")
    elif "open code" in query : # to be check 
        code_path = "C:\\Users\\sriva\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        speak("opening visual studio code")
        os . startfile(code_path)
    else :
        pass
            
def play_commands() :
    global query
    if "play my song" in query :
        speak("playing your favourite bollywood song shukriya")
        webbrowser . open("https://www.youtube.com/watch?v=bZUZSLYxK5A")
    elif "play bhajan" in query :
        speak("playing your favourite bhakti song")
        webbrowser . open("https://www.youtube.com/watch?v=sUG9AkDHYx8")
    else :
        pass

if __name__ == "__main__" :
    wish_me()
    speak("I am Infinity sir. Please tell me how may I help you")
    while True :
        query = take_command() . lower()
        if "open" in query :
            opening_commands()
        elif "play" in query :
            play_commands()
        elif "local songs" in query :
            music_dir = " "
            songs = os . listdir(music_dir)
            print(songs)
            os . startfile(os . path . join(music_dir, songs[0]))
        elif "time" in query :
            str_time = datetime . datetime . now() . strftime("%H hour : %M minutes and : %S seconds")
            print(str_time)
            speak(f"Sir, The time is {str_time}")
        elif "email to amitesh" in query :
            try :
                speak("what should I say")
                content =  take_command()
                to = "youremail@gmail.com"
                send_email(to, content)
                speak("Email has been sent!")
            except Exception as e :
                print (e)
                speak("Sorry master I am unable to send email at the moment")
        elif "hello" in query :
            speak("Hello sir. Hope you are good!")
        elif "all for the day" in query :
            speak("Thank you master. I hope I have helped you throughout your work.")
            wish_me()
            speak("and Have a great day master.")
            break
            
        else :
            pass