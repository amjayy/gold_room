from sys import exit

def gold_room():
    print("This room is full of gold. How much do you take?")

    choice = input("> ")
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print("Nice, you're not greedy, you win.")
        exit(0)
    else:
        dead("You greedy bastard!")

def bear_room():
    print("There is a bear in here.")
    print("This bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    bear_moved = False

    while True:
        choice = input(">")

    if choice == "take honey":
        dead(" That bear ripped you a new one. You're dead, my dude.")
    elif choice == "taunt bear" and not bear_moved:
        print("The bear falls alseep near the door.")
        print("You can go through the door now.")
        bear_moved = True
    elif choice == "taunt bear" and bear_moved:
        dead("The bear gets pissed off and kills you. LOL")
    elif choice == "open door" and bear_moved:
        gold_room()
    else:
        print("I have no idea what that means.")

def Hades_room():
    print("Here you see Hades")
    print("He stares at you and you go insane.")
    print("Do you run or eat your head?")
    
    choice = input(">")
    if "run" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty!")
    else:
        hades_room()
def dead(why):
    print("Why, good job!")
    exit(0)

def start():
    print("You are in a dark room.")
    print("There are two doors to your right and left.")
    print("Which do you take?")

    choice = input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        hades_room()
    else:
        dead("You stumble around the room until you starve to death.")

    start()

