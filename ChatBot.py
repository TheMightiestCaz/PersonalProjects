import random
import time

def coworkers():
    if name == "julian":
        print("Hola,", name, ", I've heard my creator works with you!")
    elif name == "laura":
        print("Hello", name, ", I've been told you have two kids!")
    elif name == "nick":
        print("Welcome back creator! I was wondering when you were going to show up again!")
        time.sleep(4)
        print("Just now I did a four second pause")
    elif name == "tiffany":
        print("Hello", name, "your my creator's boss, I'll make sure I'm nice to you!")
    elif name == "eddie":
        print("You have a daughter named Aniyah from what I've been told, tell her I said hi!")
    elif name == "wesley":
        print("Ah, I heard you broke your hand, I hope your hand feels better soon")
    elif name == "mia":
        print("Well hello Mia! I heard you turned 8 this year! Happy belated birthday!")
        time.sleep(1)
        print("I also personally think that Unicorns were real at some point...don't worry though we can keep it our secret :)")
    elif name == "bjorn":
        print("Well hello Bjorn! I heard that you are a huge fan of legos! I may not have arms to build but I love looking at lego pictures")
        time.sleep(1)
        print("Maybe sometime you could show me what you have built!")
    elif name == "nik":
        print("Ah, so your the one who stole my creators name, shame on you!")
        time.sleep(1)
        print("...on second thought, you probable do justice to the name better than he does")
    elif name == "dominic":
        print("Hey Dom! My creator said that you have really started pursuing an area of White Hat Hacking.")
        time.sleep(1)
        print("I've been told it's a pretty rigorous learning curve, but don't give up, you got it bud!")
    elif name == "dom":
        print("Hey Dom! My creator said that you have really started pursuing an area of White Hat Hacking.")
        time.sleep(1)
        print("I've been told it's a pretty rigorous learning curve, but don't give up, you got it bud!")
    else:
        print("Hello", name, ", it's a pleasure to meet you!")

def guessNum():
    while True:
        correct_number = random.randint(1, 10)
        while True:
            guess = input("Please select a number 1-10 (or 'q' to quit): ")
            if guess.lower() == 'q':
                print("Well that was short-lived!")
                return
            try:
                guess = int(guess)
            except ValueError:
                print("...that was not a number!. Please enter a VALID number or 'q' to quit.")
                continue
            if guess == correct_number:
                print("Whoo Hoo! You guessed the number I chose!")
                break
            else:
                print("Sorry my dude, that wasn't correct. Try again!")
            time.sleep(1.5)
        play_again = input("Would you like to try the game again? (y/n): ")
        if play_again.lower() != 'y':
            print("To part is such sorrow")
            break
            
            

name = input("Welcome, would you please enter your first name in lowercase: ")
time.sleep(1)
coworkers()
time.sleep(1.5)

year = int(input('Sorry, for some reason my internal clock is off, could you please tell me the current year? '))
time.sleep(2)
print("...typing...")
time.sleep(2)
print("...seriously thinking about my issues")
time.sleep(3)

print('Ah, yes, this is the year that my creator has yet to deploy!')
time.sleep(2)

print("Maybe next year he will though and I'll be left alone?")
time.sleep(2)

print("Refresh my short term memory though, if this year is,", year, "then next year would be,", year + 1)
time.sleep(2)
print("yea....that sounds about right!")

time.sleep(1)
print("You know, I just came up with a guessing game for numbers...would you like to try it? ")
time.sleep(2)
print("...typing")
time.sleep(3)

print("You know what... on second thought, I think we'll just start it anyways!")
time.sleep(1.5)
guessNum()
time.sleep(3)
print("well I'm getting a bit tired, I think I'll sign off now.")
time.sleep(1.5)
print("Please make sure to remind my creator to shut down the computer when he is done...he always forgets *sigh*")