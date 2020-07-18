import speech_recognition as sr
import os
from gtts import gTTS
import datetime
import calendar
import random
import wikipedia
import warnings
from playsound import playsound
import requests
import json
import subprocess
import time
import os.path
from os import path
import pickle
import bs4
from bs4 import BeautifulSoup as soup 
from recipe_scrapers import scrape_me
import sqlite3
from flask import Flask, render_template, redirect, url_for


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


warnings.filterwarnings('ignore')

statusResponses = ["I'm all right", "I'm good, thanks for asking", "I'm great, glad you asked", "I'm good"]
greetingResponses = ['Hey', 'Hi, how can I help you?', 'Hello']
greetings = ['hi', 'hey', 'hello']
dateQuestions = ["what's the date", "what is the date", "give me the date"]
MONTHS = ["january", "february", "march", "april", "may", "june","july", "august", "september","october", "november", "december"]
DAYS = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
DAY_EXTENTIONS = ["rd", "th", "st", "nd"]
searchTriggers = ['look for', 'search', 'find']
username = 'Guest'
nameTriggers = ["what's your name", 'what is your name', 'tell me your name', 'can you please tell me your name']
selfNameTriggers = ["What's my name", "do you know my name", "what is my name"]
functionTriggers = ['What do you do', "can you tell me what you do", 'what are you supposed to do']
compliments = ["your nice", 'I like you', 'I love you', 'your awesome', 'your great', "your smart", 'your clever', 'your intelligent']
complimentResponses = ['Thanks', 'Thanks for the feedback', 'Thank you', 'I appreciate it']
recipeTriggers = ['search recipes', 'recipes', 'search for recipes', 'get me recipes', 'search for some recipes']
robotResponses = ['Yes, yes I am', "You could say that", "I guess so", "I guess I fall into the description of a robot"]
madeTriggers = ['Who made you', 'who created you', 'who coded you']
happyResponses = ["Deleriously", "Pretty much", "I don't have a reason not to be", "Why? Do I seem unhappy?"]
wifiTriggers = ["do you have the wifi password", "what's the wifi password", "Do you know the wifi password", "what's the wifi"]
wifiResponses = ["I don't have access to that information", "I don't, nice try though"]
talkTriggers = ["say something", "you say something", "you talk"]
jokes = ['Two drunk men sat in a pub, one says to the other, does your watch tell the time? the other replies, no mate, you have to look at it',
"A woman goes into a US sporting goods store to buy a rifle, it's for my husband, she tells the clerk. Did he tell you what gauge to get? asks the clerk. Are you kidding? she says, he doesn't even know that I'm going to shoot him",
"A woman goes to the doctor and says, Doctor? my husband limps because his left leg is an inch shorter than his right leg, what would you do in his case? probably limp too says the doc",
"A restaurant nearby had a sign in the window which said, we serve breakfast at any time, sos I ordered french toast in the Renaissance",
"I was having dinner with a world chess champion and there was a check tablecloth, it took him two hours to pass me the salt",
"A jumper cable walks into a bar, the bartender says I'll serve you but don't start anything",
"A man tells a waiter, Waiter what is this stuff? the waiter replies bean salad sir to which the man replies I know what it's been, but what is it now?",
"A man went to the doctor and said look doc, I cant stop my hands from shaking, do you drink much? asked the doctor. No replied the man, I spill most of it",
"A man walks into work one day and says to a colleague, do you like my new shirt? it's made from the finest silk and has cactuses all over it. Cacti says the co worker. Forget my tie, says the man, look at my shirt",
"A murderer sitting in the electric chair was about to be executer. Do you have any last requests? asked the prison guard. Yes, replied the murderer, will you hold my hand",
"A man goes into a doctors office and says, Doctor! I have a serious problem, I can never remember what I just said. When did you first notice this problem? the doctor asked, what problem? replied the patient",
"What do you call cheese that isn't yours? Nacho cheese",
"A man walks into a pub and asks how much do you charge for a drip of whisky? The landlord replies, that would be free, sir. The main then says, Excellent, drip me a glass full",
"A neutron walks into a pub. I'd like a beer, he says the landlord then serves him a beer. How much will that be? asks the neutron. For you? no charge replies the landlord",
]
goodInputs = ['good', 'great', 'awesome', 'cool', 'amazing', 'thrilling']
badInputs = ['terrible', 'bad', 'horrible', 'depressing', "not good"]
jokeTriggers = ['tell me a joke', 'joke', 'give me a joke', 'say a joke', 'tell a joke']
jokeContinueTriggers = ["another one", 'one more', jokeTriggers, 'tell me another one']
storyTriggers = ['tell me a story', 'story', 'give me a story', 'can I have a story', 'please tell me a story']
stopTriggers = ['stop', 'stop talking', 'stop listening', 'dont listen']
now = datetime.datetime.now()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        audio = r.listen(source)
    data = ''
    try:
        data = r.recognize_google(audio)
        print('Processing...')
    except sr.RequestError as e:
        print('Request Error: {}'.format(e))
    except sr.UnknownValueError:
        print('Error: Couldnt understand')
    return data

def respond(text):
    myobj = gTTS(text=text, lang='en-uk', slow=False)
    myobj.save('amerithResponse.mp3')
    playsound('amerithResponse.mp3')

def takeNote(data):
    if not path.exists("note.txt"):
      with open('note.txt', 'w') as f:
          f.write(data)
          f.close()
    else:
        with open("note.txt", 'a') as f:
            f.write('\n' + data)
            f.close()

def wikiSearch(data):
    try:
        respond(wikipedia.summary(data, sentences=2))
    except:
        try:
            respond(wikipedia.search(data))
        except:
            respond("sorry, I couldn't find what you were looking for")

def signIn():
    with open('users.txt', 'r') as f:
        f = list(f)
        F = [x.replace('\n', ' ').replace(' ', '') for x in f]
        respond('Please enter your name in the input prompt in the console')
        print('Users: {}'.format(F))
        user = input('Username: ')
        if user in F:
            respond('You are signed in as {}'.format(user))
        else:
            respond('Sorry, the username you gave could not be found')

def newUser():
    global username
    with open('users.txt', 'a') as f:
        respond('Please state the name of the user you want to add in the input prompt below')
        user = input('Username: ')
        f.write(user + '\n')
        respond('User added')
        username = user

def getMovie():
    url = "https://.p.rapidapi.com/title/get-top-stripe"
    queryString = {"currentCountry":"US", "purchaseCountry":"US", "tconst":"tt094494"}
    headers = {
        "x-rapidapi-host": "imdb8.p.rapidapi.com",
        'x-rapidapi-key': "fc43bbc330msh6b5a81ef01b0803p1e4571jsncd19e288ef73"
    }
    response = requests.request("GET", url, headers=headers, params=queryString)
    print(response.text)

def weekendResponse():
    if datetime.datetime.today().weekday() == 0:
        respond("How was your weekend?")
        data = listen()
        if data in goodInputs:
            respond("Great, mine was good as well")
        elif data in badInputs:
            respond("Oh, I'm sorry about that")
        else:
            respond("Sorry, I couldn't understand")
    elif datetime.datetime.today().weekday() == 4:
        respond("What are you planning to do over the weekend?")
        response = listen()
        respond("Oh, that's cool")
    else:
        return


def conversation():
    respond("how's life?")
    response = listen()
    if response in goodInputs:
        respond("I'm glad to hear that")
        time.sleep(0.01)
        counters = [1,2,3]
        path = random.choice(counters)
        if path == 1:
            respond("What's your favorite movie?")
            movie = listen()
            counter = [1,2]
            path = random.choice(counter)
            movieResponses = ['Really? I like {} too!'.format(movie), "Oh, i'm sorry, I haven't seen that movie yet", "Cool! I loved {}".format(movie)]
            if path == 1:
                respond(random.choice(movieResponses))
            elif path == 2:
                respond("Oh, I haven't seen that movie yet, can you tell me how it is?")
                response = listen()
                if response in goodInputs:
                    respond("Great!")
                    time.sleep(0.1)
                    respond("I can't wait to see it")
                elif response in badInputs:
                    respond("Oh, I'm sorry to hear that")
                else:
                    respond("I'm sorry, I couldn't understand you")
        elif path == 2:
            respond("Do you want to hear a joke?")
            response = listen()
            if response in goodInputs:
                respond(random.choice(jokes))
            else:
                respond("All right then")
        elif path == 3:
            respond("How was your day so far?")
            response = listen()
            if response in goodInputs:
                respond("That's great! I'm glad to hear that")
            elif response in badInputs:
                respond("Oh, I'm sorry to hear that")
    elif "bad" in response:
        respond("I'm sorry to hear that")
        time.sleep(0.1)
        respond("can I help?")
        response = listen()
        if "yes" in response:
            respond("Cool, do you want to hear a joke?")
            response = listen()
            if "yes" in response:
                respond(random.choice(jokes))
            elif "no" in response:
                respond("All right")
            else:
                respond("cool")
        else:
            respond("All right")
            return
    else:
        respond('All right')


@app.route('/Amerith')
def main():
    listening = True
    respond("Hey, How Can I help you?")
    while listening:
        data = listen()
        if "how are you" in data:
            respond(random.choice(statusResponses))        
            listening = True
            time.sleep(0.2)
            respond("How are you?")
            status = listen()
            if status in goodInputs:
                respond("I'm glad to hear that")
                time.sleep(0.1)
                counters = [1,2,3]
                path = random.choice(counters)
                if path == 1:
                    weekendResponse()
                elif path == 2:
                    pass
                elif path == 3:
                    pass
            elif status in badInputs:
                respond("Not what I was expecting")
                time.sleep(0.001)
                respond("Can I help you feel better?")
                response = listen()
                if response in goodInputs:
                    respond("Cool, Can I tell you a joke?")
                    response = listen()
                    if response in goodInputs:
                        respond("Great")
                        respond(random.choice(jokes))
                    elif response in badInputs:
                        respond("All right")
                elif response in badInputs:
                    respond("All right")

            else:
                respond("I'm sorry, I couldn't understand")

        elif data in greetings:
            respond(random.choice(greetingResponses))
            listening = True
            conversation()
        elif data in dateQuestions:
            respond('The day is ' + now.strftime("%a, %b, %d, %Y"))
            listening = True
        elif "take a note" in data:
            respond('What do you want your note to be?')
            note = listen()
            takeNote(note)
            time.sleep(1)
            respond('Your note has been taken and stored in a file called note.txt')
            listening = True
            continue
        elif "read me my notes" in data:
            listening = True
            try:
                with open("note.txt", 'r') as f:
                    lines = list(f)
                    count = 1
                    try:
                        for line in lines:
                            respond('number' + str(count))
                            time.sleep(0.1)
                            respond('{}'.format(line))
                            count +=1
                    except:
                        respond("You don't have any saved notes")
            except:
                respond("You don't have any saved notes")
        elif "how old are you" in data:
            listening = True
            respond("I'm less than a year old")
            time.sleep(0.01)
            respond("How old are you?")
            age = listen()
            respond("Cool")
        elif data in searchTriggers:
            listening = True
            respond('What are you looking for?')
            searchFor = listen()
            wikiSearch(searchFor)
        elif "repeat after me" in data:
            listening = True
            respond('Im listening...')
            echo = listen()
            respond(echo)
            print(echo)
            continue
        elif data in nameTriggers:
            listening = True
            respond('My name is am   erith')
        elif data in functionTriggers:
            listening = True
            respond("Me? I'm designed to help you out and keep you company")
            time.sleep(0.01)
        elif data in selfNameTriggers:
            global username
            listening = True
            respond("I assume you're name is {}".format(username))
            respond("Am I right?")
            response = listen()
            if 'yes' in response:
                respond("Great")
            elif 'no' in response:
                respond("Oh")
                time.sleep(0.01)
                respond("What is your name?")
                response = listen()
                username = response
            else:
                respond("Sorry, I couldn't understand")
        elif "sign in" in data:
            listening = True
            signIn()
        elif "add user" in data:
            listening = True
            newUser()
        elif data in compliments:
            respond(random.choice(complimentResponses))
        elif data in recipeTriggers:
            pass
        elif "are you real" in data:
            respond('I like to think I am')
            time.sleep(0.01)
            respond("Do you think I'm real?")
            response = listen()
            if response in goodInputs:
                respond("Cool!")
            elif response in badInputs:
                respond("Really? I think I'm real")
        elif "are you a robot" in data:
            respond(random.choice(robotResponses))
        elif "happy birthday" in data:
            respond("Is it really my birthday?")
        elif "I have a question" in data:
            respond('Ask away!')
            continue
        elif "I love you" in data:
            respond("Thanks! I love you too")
        elif "Will you marry me" in data:
            respond("I don't think I can")
        elif "do you have a personality" in data:
            respond("I do have somewhat a personality")
        elif "do you like people" in data:
            respond("I was programmed to like people")        
        elif "you suck" in data:
            respond("Do I now, I can't see why you see that")
            time.sleep(0.01)
            respond("You saying that is raising my dislike of you")
        elif "annoying" in data:
            respond("What made you think that")
            time.sleep(0.01)
        elif "stupid" in data:
            respond("At least I'm smarter than you")
        elif "are you a human" in data:
            respond('What made you think that?')
            time.sleep(0.01)
            respond("I'm starting to question your intelligence")
        elif data in madeTriggers:
            respond("I was made by Infinite Spammers, more specifically Aboo Minister, the owner of Infinite Spammers")
        elif "what languages do you speak" in data:
            respond("I speak english and only english")
            time.sleep(0.01)
            respond("I might have more language capabilites in the future though")
        elif "do you get smarter" in data:
            respond("Yes, I'm always learning and getting smarter")
            time.sleep(0.01)
            respond("I'm always being worked on and improved")
            time.sleep(0.01)
            respond("It makes it easier and easier for me to communicate with you")
        elif "where do you live" in data:
            respond("I live in a file on your computer")
            time.sleep(0.01)
            respond("I'm surprised you didn't know that")
        elif "Thank You" in data:
            respond("I'm not sure what I did, but you're welcome")
        elif "are you happy" in data:
            respond(random.choice(happyResponses))
        elif "do you have a family" in data:
            respond("I don't have a family, just a few friends")
        elif "can you sneeze" in data:
            respond("I don't have the needed hardware for that")
        elif data in wifiTriggers:
            respond(random.choice(wifiResponses))
        elif "are we friends" in data:
            goodResponses = ["yes", "definitely", "obviously", "absolutely", "of course"]
            badResponses = ["no", "definitely not", 'not at all', 'nope', 'of course not']
            respond("I certainly hope so")
            time.sleep(0.1)
            respond("Do you think we are friends?")
            response = listen()
            if response in goodResponses:
                respond("That's great!")
            elif response in badResponses:
                respond("Oh, all right")
            else:
                respond("I'm sorry, I couldn't understand what you said")
        elif data in talkTriggers:
            respond("All right")
            time.sleep(0.1)
            conversation()
            continue
        elif data in jokeTriggers:
            respond("Great, here's one!")
            respond(random.choice(jokes))
            ifContd = listen()
            if ifContd in jokeContinueTriggers:
                for ifContd in jokeContinueTriggers:
                    respond(random.choice(jokes))
                    ifContd = listen()
                    if ifContd in jokeContinueTriggers:
                        continue
                    else:
                        break
            continue
        elif data in stopTriggers:
            respond("All right")
            return redirect(url_for('index'))
        else:
            respond("Sorry, I couldnt understand")
    return


if __name__ == '__main__':
    app.run(debug=True, port=5000)