# Amerith-1.1
### By Rayyan Cyclegar

Amerith is a virtual assistant designed to talk and have conversations with you. Amerith has commands and triggers which can start up a conversation or trigger features. Amerith can have a continued conversation with the user and can ask and respond to questions. This is currently a beta version of Amerith, so some phrases may not be picked up or understood. Amerith has the following features:
* The ability to take and read out notes, saving them to a `.txt` file. She currently doesn't have the ability to delete notes, only to read out loud.
* The ability to search and derive terms from Wikipedia to respond to the users query about something.
* The ability to sign in and add users.
* The ability to set nicknames.

## Dependencies
Amerith can support a continuous conversation and query the user with questions to which the user can answer with multiple different answers. She can greet and do smalltalk with the user. Amerith in beta development and still has a multitude of bugs. The program is continually being updated and improved. You can set and add users with the `add user` command. You can also edit the text file where the users are kept. Currently Amerith can't delete notes, only take them. In order to delete notes you have to manually go to the `.txt` file and delete them from there. Amerith has the following dependencies needed to run:
* SpeechRecognition
* PyAudio
* gTTS
* Playsound
* wikipedia
* subprocess
* requests
* newspaper
* youtube_search
 > Some of these dependencies aren't in use yet, they are for future updates to the program.
 
## Commands & Phrases
Amerith has multiple commands and phrases that the program understands. They are listed below:
* Greetings
  * `How are you?`
  * `hi`
  * `hey`
  * `hello`
* Search Commands
  * `look for`
  * `search`
  * `find`
* Name
  * `what's your name`
  * `what is your name`
  * `tell me your name`
  * `can you please tell me your name`
  * `What's my name`
  * `what is my name`
  * `do you know my name`
* What can you do?
  * `what do you do`
  * `can you tell me what you do`
  * `what are you supposed to do`
* Compliments
  * `you're nice`
  * `I like you`
  * `I love you`
  * `you're awesome`
  * `you're great`
  * `you're smart`
  * `you're clever`
  * `you're intelligent`
* Who made you?
  * `who made you`
  * `who created you`
  * `who coded you`
* What's the wifi password?
  * `what's the wifi password`
  * `do you have the wifi password`
  * `do you know the wifi password`
  * `what's the wifi`
* Say something
  * `say something`
  * `you say something`
  * `you talk`
* Jokes
  * `tell me a joke`
  * `joke`
  * `give me a joke`
  * `say a joke`
  * `tell a joke`
  * Follow up jokes:
    * All of the above
    * `another one`
    * `one more`
    * `tell me another one`
* Date (The date feature is not too accurate, Do not rely on it for the actual date)
  * `what's the date`
  * `what is the date`
  * `give me the date`
* `take a note`
* `read me my notes`
* `how old are you`
* `repeat after me`
* `sign in` (This command and the one below it are experimental, and may have some bugs)
* `add user`
* `are you real`
* `are you a robot`
* `happy birthday`
* `I have a question`
* `I love you`
* `will you marry me`
* `do you have a personality`
* `do you like people`
* Insults
  * `you suck`
  * `you're annoying`
  * `you're stupid`
* `are you a human`
* `what languages do you speak`
* `do you get smarter`
* `where do you live`
* `thank you`
* `are you happy`
* `do you have a family`
* `can you sneeze`
* `are we friends`
* Stop Program
  * `stop`
  * `stop listening`
  * `stop talking`
  * `don't listen`

## Quick Start Guide
To start up Amerith download the dependencies and the code file onto your computer, and then run the program in an IDE of some sort. The file is not an executable file yet, and will become one in a few updates. After you run the program, make sure you have a working mic and speaker, and wait for the program to greet you. It will greet you by saying; *Hey, How Can I Help You?* and then will proceed to pring out logs in the console. In the console you should see `listening` which means that the program is waiting for you to say something. If it has picked up something, then the console should pring out `processing` which means the program is processing your answer and figuring out how to respond to you. If the program didn't understand what you said, it should print out `Error: Couldn't understand` in the console and say; *Sorry, I couldn't understand*. You will need a wifi connection to run this.

  
  
