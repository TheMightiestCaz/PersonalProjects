import time
import random

#I want to develop a game for the kids or anyone to play
#It will be a basic text adventure game
#I'm thinking this first version will be for everyone to play from the work center
#Further iterations will be for the kids to play depending on how large I'm able to create it
#then eventually give it a GUI and possibly put it on my webpage (whenever I get around to making that!)

#Opening scene...

def endMessage():
    time.sleep(3)
    print("""
***********************************
*      THANKS FOR PLAYING!        *
*   I HOPE YOU HAD AS MUCH FUN    *
*  PLAYING AS I DID CREATING IT!  *
*          -NICK                  *
*                                 *
***********************************""")
    closeGame = input("to close the game please type 'q': ")
    if closeGame == 'q':
        quit
    else:
        quit

def load():
    print("*")
    time.sleep(1.5)
    print(" *")
    time.sleep(1.5)
    print("  *")
    time.sleep(1.5)
    print("   *")
    time.sleep(1.5)
    print("    *")


print("""
***********************************
*  WELCOME TO AN ADVENTURE GAME!  *
*                                 *
*         created by:             *
*        Nicholas Pepera          *
*                                 *
***********************************      
      """)

print("You wake up...it is in the middle of a forest")
time.sleep(3) #this will force the program to pause for however many seconds are in the ()
print("As you slowly look around you see some objects laid out in front of you")
time.sleep(3)
x = input("Do you want to look at what's in front of you? (y/n): ")
if x == 'y':
    print("""You see laid out in front of you the following items:
          1. Flashlight
          2. Pack of gum
          3. Stick and Rope
          4. Map""")
    item = input(print("If you would like to grab an item please enter the number or 'n' for nothing: "))
else:
    print("You feel a strange sense of euphoric that as an individual you don't need anything..")
time.sleep(3)
print("You begin to hear a humming sound")
time.sleep(3)
choice1 = input("Do you follow the sound? (y/n): ")
if choice1 == 'y':
    time.sleep(3)
    print("You begin moving towards the sound")
    load()
    time.sleep(2)
    print("The sound suddenly stops!")
    time.sleep(2)
    print("You finally have the chance to look around")
    time.sleep(2.5)
    print("You are now LOST!...")
    time.sleep(2.5)
    print("You call out for help...but the only response is the sounds of the forest as the shadows begin to close in...")
    time.sleep(4)
    print("As the darkness creeps in and you vision fades")
    time.sleep(3)
    print("You realize...the sound was just the crickets in the background...")
    time.sleep(4)
    endMessage()
if choice1 == 'n':
    print("Good idea. You are not taking risks. ")
    time.sleep(2)
    print("You begin walking in the opposite direction")
    time.sleep(3)
    load()
    print("After some time, you realize that the sound never went away")
    time.sleep(3)
    print("...it's starting to get closer")
    time.sleep(3)
    print("The sound is now behind you and you panic!")
    time.sleep(2)
    action = input("Do you start running (r), stop to yell for help (c)?: ")
    while action == 'c':
        print("No one responds to you as the sound continues to get closer!")
        action = input("Do you start running (r), stop to yell for help (c)?: ")
print("You are now running fast! The sound gets even LOUDER!")
time.sleep(2)
direction = input("Which direction do you go? north, south, east, or west: ")
if direction == 'north':
    print('You reach an abandoned cabin.')
    if item == '4':
        print("You use the map and find your way home.")
        time.sleep(2)
        print("YOU WON!!")
        endMessage()
    else:
        print("You kick yourself for not looking around and taking the map earlier")
        time.sleep(3)
        print("You are still lost...and you die of starvation.")
        endMessage()
elif direction == 'south':
    print("You reach a river with a broken bridge.")
    if item == '3':
        print("You chose an item that can fix the bridge.")
        time.sleep(2)
        print("You fix the bridge, cross over, and find your way home")
        time.sleep(2)
        print("YOU WON!!")
        time.sleep(2)
        endMessage()
    else:
        print("If you had a rope or a stick, you could fix the bridge.")
        time.sleep(2)
        print("You try to cross the river anyways")
        load()
        print("After fighting the current for what feels like hours..")
        time.sleep(2)
        print("Your skinny little arms can't do anything else and you give up..")
        time.sleep(3)
        print("As the world fades away...you think on how you should have spent that extra few minutes a day working out...")
        time.sleep(2)
        endMessage()
elif direction == 'west':
    print("You are walking and trip over a fallen log.")
    time.sleep(3)
    print("You have hurt your foot. You sit down and wait for help..")
    load()
    print("After waiting forever...you realize no one is comming to help you...")
    time.sleep(3)
    endMessage()
else:
    print('You reach the side of the highway. It is dark.')
    if item == '1':
        print('You use the flashlight to signal.')
        time.sleep(2)
        print("A car stops and gives you a ride home.")
        time.sleep(2)
        print("CONGRATS YOU WON!!")
        time.sleep(3)
        endMessage()
    else:
        print("If you had brought a flashligh, you could signal for help..")
        time.sleep(2)
        print("Because it is dark a passing vehicle comes upon you..")
        time.sleep(2)
        print("Without a way to signal the vehicle, you get hit...and bleed out on the side of the road")
        time.sleep(3)
        endMessage()