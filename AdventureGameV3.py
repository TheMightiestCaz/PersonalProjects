import time
import tkinter as tk
from tkinter import messagebox

def end_message():
    messagebox.showinfo("Game Over", "THANKS FOR PLAYING!\n\nI HOPE YOU HAD AS MUCH FUN PLAYING AS I DID CREATING IT!\n\n-NICK")
    root.destroy()

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
    messagebox.showinfo("Welcome", "You wake up...it is in the middle of a forest")
    time.sleep(3)
    messagebox.showinfo("Welcome", "As you slowly look around you see some objects laid out in front of you")
    time.sleep(3)
    messagebox.showinfo("Welcome", "You see laid out in front of you the following items:\n\n1. Flashlight\n2. Pack of gum\n3. Stick and Rope\n4. Map")
    messagebox.showinfo("Welcome", "Choose an item by clicking the corresponding button.")

def play_game(item):
    messagebox.showinfo("Game", "You begin to hear a humming sound")
    time.sleep(3)
    choice1 = messagebox.askyesno("Game", "Do you follow the sound?")
    if choice1:
        time.sleep(3)
        messagebox.showinfo("Game", "You begin moving towards the sound")
        load()
        time.sleep(2)
        messagebox.showinfo("Game", "The sound suddenly stops!")
        time.sleep(2)
        messagebox.showinfo("Game", "You finally have the chance to look around")
        time.sleep(2.5)
        messagebox.showinfo("Game", "You are now LOST!...")
        time.sleep(2.5)
        messagebox.showinfo("Game", "You call out for help...but the only response is the sounds of the forest as the shadows begin to close in...")
        time.sleep(4)
        messagebox.showinfo("Game", "As the darkness creeps in and your vision fades")
        time.sleep(3)
        messagebox.showinfo("Game", "You realize...the sound was just the crickets in the background...")
        time.sleep(4)
        end_message()
    else:
        messagebox.showinfo("Game", "Good idea. You are not taking risks.")
        time.sleep(2)
        messagebox.showinfo("Game", "You begin walking in the opposite direction")
        time.sleep(3)
        load()
        messagebox.showinfo("Game", "After some time, you realize that the sound never went away")
        time.sleep(3)
        messagebox.showinfo("Game", "...it's starting to get closer")
        time.sleep(3)
        messagebox.showinfo("Game", "The sound is now behind you, and you panic!")
        time.sleep(2)
        action = messagebox.askyesno("Game", "Do you start running?")
        while not action:
            messagebox.showinfo("Game", "No one responds to you as the sound continues to get closer!")
            action = messagebox.askyesno("Game", "Do you start running?")
    
    messagebox.showinfo("Game", "You are now running fast! The sound gets even LOUDER!")
    time.sleep(2)
    direction = messagebox.askquestion("Game", "Which direction do you go? North, South, East, or West?")
    if direction == "yes":
        messagebox.showinfo("Game", "You reach an abandoned cabin.")
        if item == '4':
            messagebox.showinfo("Congratulations!", "You use the map and find your way home.\n\nYOU WON!!")
            end_message()
        else:
            messagebox.showinfo("Game Over", "You kick yourself for not looking around and taking the map earlier.\n\nYou are still lost...and you die of starvation.")
            end_message()
    elif direction == "no":
        messagebox.showinfo("Game", "You reach a river with a broken bridge.")
        if item == '3':
            messagebox.showinfo("Congratulations!", "You chose an item that can fix the bridge.\n\nYou fix the bridge, cross over, and find your way home.\n\nYOU WON!!")
            end_message()
        else:
            messagebox.showinfo("Game Over", "If you had a rope or a stick, you could fix the bridge.\n\nYou try to cross the river anyways")
            load()
            messagebox.showinfo("Game Over", "After fighting the current for what feels like hours..\n\nYour skinny little arms can't do anything else, and you give up..\n\nAs the world fades away...you think on how you should have spent that extra few minutes a day working out...")
            end_message()

def item_selected(selected_item):
    root.withdraw()  # Hide the main window
    play_game(selected_item)

def main():
    global root
    root = tk.Tk()
    root.title("Text Adventure Game")

    start_game_button = tk.Button(root, text="Start Game", command=start_game)
    start_game_button.pack()

    item_frame = tk.Frame(root)
    item_frame.pack()

    item_buttons = []
    item_labels = ["Flashlight", "Pack of Gum", "Stick and Rope", "Map"]
    for i, item_label in enumerate(item_labels):
        button = tk.Button(item_frame, text=item_label, command=lambda item=item_label: item_selected(item))
        button.grid(row=0, column=i, padx=10, pady=10)
        item_buttons.append(button)

    root.mainloop()

if __name__ == "__main__":
    main()
