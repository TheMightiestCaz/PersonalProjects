import time

def end_message():
    time.sleep(3)
    print("""
***********************************
*      THANKS FOR PLAYING!        *
*   I HOPE YOU HAD AS MUCH FUN    *
*  PLAYING AS I DID CREATING IT!  *
*          -NICK                  *
*                                 *
***********************************""")
    close_game = input("To close the game, please type 'q': ")
    if close_game.lower() == 'q':
        quit()
    else:
        quit()

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

def start_game():
    print("You wake up...it is in the middle of a forest")
    time.sleep(3)
    print("As you slowly look around you see some objects laid out in front of you")
    time.sleep(3)
    x = input("Do you want to look at what's in front of you? (y/n): ")
    if x.lower() == 'y':
        print("""You see laid out in front of you the following items:
              1. Flashlight
              2. Pack of gum
              3. Stick and Rope
              4. Map""")
        item = input("If you would like to grab an item, please enter the number or 'n' for nothing: ")
    else:
        print("You feel a strange sense of euphoria that as an individual, you don't need anything...")
        item = 'n'
    return item

def play_game(item):
    print("You begin to hear a humming sound")
    time.sleep(3)
    choice1 = input("Do you follow the sound? (y/n): ")
    if choice1.lower() == 'y':
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
        print("As the darkness creeps in and your vision fades")
        time.sleep(3)
        print("You realize...the sound was just the crickets in the background...")
        time.sleep(4)
        end_message()
    elif choice1.lower() == 'n':
        print("Good idea. You are not taking risks.")
        time.sleep(2)
        print("You begin walking in the opposite direction")
        time.sleep(3)
        load()
        print("After some time, you realize that the sound never went away")
        time.sleep(3)
        print("...it's starting to get closer")
        time.sleep(3)
        print("The sound is now behind you, and you panic!")
        time.sleep(2)
        action = input("Do you start running (r) or stop to yell for help (c)?: ")
        while action.lower() == 'c':
            print("No one responds to you as the sound continues to get closer!")
            action = input("Do you start running (r) or stop to yell for help (c)?: ")

    print("You are now running fast! The sound gets even LOUDER!")
    time.sleep(2)
    direction = input("Which direction do you go? North, South, East, or West: ")
    if direction.lower() == 'north':
        print('You reach an abandoned cabin.')
        if item == '4':
            print("You use the map and find your way home.")
            time.sleep(2)
            print("YOU WON!!")
            end_message()
        else:
            print("You kick yourself for not looking around and taking the map earlier")
            time.sleep(3)
            print("You are still lost...and you die of starvation.")
            end_message()
    elif direction.lower() == 'south':
        print("You reach a river with a broken bridge.")
        if item == '3':
            print("You chose an item that can fix the bridge.")
            time.sleep(2)
            print("You fix the bridge, cross over, and find your way home.")
            time.sleep(2)
            print("YOU WON!!")
            time.sleep(2)
            end_message()
        else:
            print("If you had a rope or a stick, you could fix the bridge.")
            time.sleep(2)
            print("You try to cross the river anyways")
            load()
            print("After fighting the current for what feels like hours..")
            time.sleep(2)
            print("Your skinny little arms can't do anything else, and you give up..")
            time.sleep(3)
            print("As the world fades away...you think on how you should have spent that extra few minutes a day working out...")
            time.sleep(2)
            end_message()
    elif direction.lower() == 'west':
        print("You are walking and trip over a fallen log.")
        time.sleep(3)
        print("You have hurt your foot. You sit down and wait for help..")
        load()
        print("After waiting forever...you realize no one is coming to help you...")
        time.sleep(3)
        end_message()
    elif direction.lower() == 'east':
        print('You reach the side of the highway. It is dark.')
        if item == '1':
            print('You use the flashlight to signal.')
            time.sleep(2)
            print("A car stops and gives you a ride home.")
            time.sleep(2)
            print("CONGRATS YOU WON!!")
            time.sleep(3)
            end_message()
        else:
            print("If you had brought a flashlight, you could signal for help..")
            time.sleep(2)
            print("Because it is dark, a passing vehicle comes upon you..")
            time.sleep(2)
            print("Without a way to signal the vehicle, you get hit...and bleed out on the side of the road")
            time.sleep(3)
            end_message()

def main():
    print("""
***********************************
*  WELCOME TO AN ADVENTURE GAME!  *
*                                 *
*         created by:             *
*        Nicholas Pepera          *
*                                 *
***********************************      
      """)
    item = start_game()
    play_game(item)

if __name__ == "__main__":
    main()
