import time
import sys
items =[]

def printDelay(s):
    time.sleep(0.75)
    for c in s:
        if c =="\n":
            time.sleep(0.75)
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)
    
    print("")

def train():
    for i in (0,2):
        printDelay("...")
        time.sleep(1)
        printDelay("Clank-clank...Clank-clank")
        time.sleep(1)
    printDelay("...")

def cabooseGood():
    time.sleep(1)
    printDelay("You successfully clean up the clock. It's not spotless, but at least the clock hands can move forward")
    printDelay("The fog has started to clear up, and you can finally see around you in the car.\nA woman dressed in an old-fashioned dress and holding a suitcase appears in front of you.")
    printDelay("She smiles and says, \"Thank you for fixing my clock. Now I can finally make it back home in time\"\nShe disappears and the train finally jerks to a stop.")
    time.sleep(1)
    printDelay("You look out the window and finally see a sign for your hometown. You go back to your car to get your bags and make your way home.")
    printDelay("YOU WIN")

def clock():
    time.sleep(1)
    printDelay("The clock looks old. Like, really old. Probably at least 100 years old. Which is weird because this is a new train.")
    time.sleep(1)
    printDelay("You step closer to take a better look at the clock.")
    time.sleep(1)
    printDelay("Gross, there's some dirt lodged between the clock hands. It looks like the gunk is keeping the clock from moving forward.")
    
    printDelay("Clean the clock?\n(1) Yes\n(2) No: ")
    answer = input()
    while answer != "1" and answer !="2":
        printDelay("Try again. Choose from 1 or 2: ")
        answer = input()
    if answer == "2":
        printDelay("This is getting really creepy. You turn around to leave the caboose.")
        cabooseBad()
                
    elif answer == "1": #clean the clock
        if "spoon" in items:
            printDelay("You remember that you picked up a spoon earlier.\nYou wouldn't want to touch an old clock with your bare hands.\nYou start to carefully scratch away at the dirt with the spoon.")
            if "phone" in items: #phone makes you drop clock
                printDelay("!!!\nSuddenly your phone rings, startling you and making you drop and shatter the clock")
            else:
                cabooseGood()

        else: #NO SPOON
            printDelay("You try to scratch away at the dirt with your fingernail.")
            cabooseBad()

def cabooseBad():
    time.sleep(1)
    printDelay("!!!")
    printDelay("You hear another voice gasp into your ear, and you jump with surprise, dropping and shattering the clock.")
    time.sleep(1)
    printDelay("...")
    time.sleep(1)
    printDelay("\"What did you do to my clock...? Now I'll never make it home in time...\"")
    time.sleep(1)
    printDelay("Just when the room can't get any colder, you feel a freezing rush so cold you can barely move.")
    time.sleep(1)
    printDelay("Somehow the cold makes you sleepy...It can't hurt to close your eyes for just a bit...")
    sleepEnd()

def sleepEnd():
    
    time.sleep(1.5)
    printDelay("You see a ghostly figure in your dream. The figure lulls you to sleep within your dream.")
    time.sleep(1.5)
    printDelay("You feel so peaceful...It would be nice to sleep forever and never wake up again, you think.")
    time.sleep(1.5)
    printDelay("...")
    time.sleep(1.5)
    printDelay("GAME OVER")

def caboose():
    printDelay("You make your way to the back of the train. As you get through each car, you notice that you haven't seen anybody else on the train.")
    printDelay("You can't be the only passenger, right?")
    time.sleep(1)
    printDelay("You keep walking. This train feels like a mile long, you're getting pretty tired.")
    printDelay("You make it to the snack car.")

    printDelay("Stop for a snack break?\n(1) Yes\n(2) No: ")
    answer=input()
    
    while answer != "1" and answer !="2":
        printDelay("Try again. Choose from 1 or 2: ")
        answer = input()
    if answer =="1":
        printDelay("You sit down at the snack bar and stare at the donut on the menu.")
        printDelay("Before you know it, a huge jelly donut appears on a plate in front of you.")
        time.sleep(1)
        printDelay("You take a bite of the fluffy donut and savor the sweet jelly.")
        time.sleep(1)
        printDelay("The donut in your belly is making you feel sleepy, and your eyes drift closed.")
        sleepEnd()
    
    elif answer =="2":
        printDelay("You ignore the sweet smell of the snack bar but you notice a single silver spoon on one of the tables.")
        printDelay("It looks clean, and it's so shiny you can clearly see your own face in it.")
        time.sleep(1)

        printDelay("Take the spoon?\n(1) Yes\n(2) No: ")
        answer=input()
        while answer != "1" and answer !="2":
            printDelay("Try again. Choose from 1 or 2: ")
            answer = input()
        if answer == "1":
            items.append("spoon")
            printDelay("You put the spoon in your bag. Kinda gross to keep a random spoon, but OK")
        elif answer == "2":
            printDelay("You leave the spoon on the table. Gross, you don't want a random spoon.")
        time.sleep(1)
        printDelay("You move on and continue towards the back of the train.")

        train()
        printDelay("!!!")
        time.sleep(1)
        printDelay("You hear a harsh whisper in your ear, and you turn around.")
        time.sleep(1)
        printDelay("The car is empty, except for you.")
        printDelay("It's weird that you still haven't seen a single other person on this train.")
        time.sleep(1)
        printDelay("You should keep moving. You ignore what just happened and move towards the caboose.")
        printDelay("You finally reach the back of the train, the luggage car.")
        time.sleep(1)
        printDelay("You try to look into a small window in the door, but for some reason the glass is all fogged up.")
        printDelay("You put your hand on the door knob to open it.")
        time.sleep(1)
        printDelay("The handle is ice cold, even though the temperature outside feels perfectly normal.")
        time.sleep(1)

        #inside the car
        printDelay("You open the door and go inside the car, but you can't see anything.")
        printDelay("The entire car is filled with fog. And it's freezing, you can't stop shivering.")
        time.sleep(1)

        if "flashlight" in items:
            printDelay("Luckily you brought your flashlight. You turn it on and point it around the car.")

        else: #phone
            printDelay("Luckily you brought your phone. You turn on the flashlight feature and point it around the car.")
        
        printDelay("You find a clock hanging on the wall.")
        clock()

def conductorEnd():
    train()
    printDelay("You finally made it the conductor car. You open the door to find the someone controlling the train. \nIt's hard to tell in the dark, but it looks like they aren't wearin a uniform, just regular clothes. That's weird, you thought that conductors usually wear uniforms.\nThey're standing with their back to you. It seems that they haven't noticed you yet.")
    
    printDelay("Should you try and get their attention?\n(1) Yes \n(2)No")
    answer = input()
    while answer != "1" and answer !="2":
        printDelay("Try again. Choose from 1 or 2: ")
        answer = input()
    if answer =="1":
        printDelay("You tap the \"conductor's\" shoulder. \nWhen they turn around, you see that their eyes are glowing. They've been possessed!")
        printDelay("You don't have any time to react, and the ghost jumps from its previous victim and possesses you instead! \nAs the next victim of the ghost train, you've been doomed to conduct the train forever.\nGAME OVER")
    elif answer =="2":
        printDelay("Something is a bit off. You stare at the \"conductor\" and notice their reflection in the glass in front of them. Their eyes are glowing, it's a ghost!")
        printDelay("You have to move carefully here...")
        printDelay("...")
        if "phone" in items:
            printDelay("Suddenly your phone's alarm goes off, playing the annoying siren sound that wakes you up in the morning!\nThe ghost screams and puts its hands over its ears to try and block the sound, but it isn't enough.")
            printDelay("This is the distraction you need!")
            printDelay("You quickly move in front of the ghost and hold your silver mirror in front of its face before it can get you. The ghost screams louder as it leaves the body and is trapped inside the mirror.")
            printDelay("The tran is finally free from the ghost, and you carefully place the mirror on the ground. It looks like the ghost was possessing people in order to keep the train running forever.\nYou press the emergency brakes on the train controls and the train slows to a stop, luckily you can see the next station up ahead.\nYOU WIN")


def loungeGhost():
    printDelay("You look out the window and see your reflection. But next to your reflection you see an old man.\nYou turn around and see nobody else in the car. It's a ghost!")
    printDelay("You look back at the ghostly reflection and the ghost man starts to come after you.")

    if "mirror" in items:
        printDelay("Quickly you hold the silver mirror out in front of you and the ghost disappears.\nYou look in the mirror and see the ghost man staring back at you. He's trapped in the mirror.\nYou breathe a sigh of relief and keep moving.")
        conductorEnd()
    else:
        printDelay("You have nothing you can use to defend yourself! The ghost looks at you with glowing eyes and possesses you.\nGAME OVER")

def conductor():
    printDelay("You start walking towards the front of the train. Maybe the conductor knows what's going on.")
    printDelay("On the way to the conductor car, you arrive at the lounge car.\nComfy looking chairs line up along the wall.\nYou look down and see a silver mirror on one of the tables.")
    
    printDelay("What do you do?\n(1) Pick up the mirror.\n(2) Leave it alone.")
    answer = input()
    while answer != "1" and answer !="2":
        printDelay("Try again. Choose from 1 or 2: ")
        answer = input()
    if answer == "1":
        items.append("mirror")
        printDelay("You take the mirror. It could be worth money.")
    elif answer =="2":
        printDelay("You ignore the mirror and keep walking. It doesn't belong to you.")
    loungeGhost()

def investigate():
    printDelay("You decide to get up from your seat and go see what the problem is.")
    printDelay("You should probably take something from your bag with you.")
    printDelay("Your pockets only have room for two items. You should probably leave something on your chair to save your seat.")
    
    printDelay("What do you take?\n(1) your phone\n(2) your flashlight")
    answer=input()
    while answer != "1" and answer !="2":
        printDelay("Try again. Choose from 1 or 2: ")
        answer = input()
    if answer == "1":
        items.append("phone")
        notItem="flashlight"
    elif answer =="2":
        items.append("flashlight")
        notItem="phone"
    time.sleep(1)
    toPrint=("You put your "+items[0]+" in your pocket and leave the "+notItem+" and get up from your seat.")
    printDelay(toPrint)
    printDelay("Which way should you go? \n(1) Towards the caboose of the train \n(2) the conductor car? ")
    answer = input()
    while answer != "1" and answer !="2":
        printDelay("Try again. Choose from 1 or 2: ")
        answer = input()
    if answer == "1":
        caboose()
    elif answer == "2":
        conductor()

def intro():
    printDelay("What is your name? ")
    name = input()
    printDelay("Welcome aboard, "+name+ ". Go ahead and make yourself comfortable. We reserved an empty car just for you")
    train()
    printDelay("You fell asleep for a minute there.")
    printDelay("You noticed that the lights are flickering. And it's getting pretty late, shouldn't you have arrived by now?")
    printDelay("What do you do?\n(1) Eh, it's probably just running late. Go back to sleep. \n(2) Something must be wrong. Go and investigate: ")
    answer = input()
    while answer != "1" and answer !="2":
        printDelay("Try again. Choose from 1 or 2: ")
        answer = input()
    if answer=="1":
        printDelay("You shrug and close your eyes again. You drift back to sleep.")
        sleepEnd()
    elif answer =="2":
        investigate()
    
#START
printDelay("Welcome to the Haunted Train. You are running late to see your family and this is the only train running tonight.\nKnowing that it's haunted, would you still like to board? \n(1) Yes \n(2) No: ")
answer = input()
while answer != "1" and answer !="2":
    printDelay("Try again. Choose from 1 or 2: ")
    answer = input()
if answer == "1":
    printDelay("Splendid. We'll get your ticket right away.")
    name = input("What is your name? ")
    printDelay("Welcome aboard, "+name+ ". Go ahead and make yourself comfortable. We reserved an empty car just for you")
    train()
    printDelay("You fell asleep for a minute there.")
    printDelay("You noticed that the lights are flickering. And it's getting pretty late, shouldn't you have arrived by now?")
    answer = input("What do you do? \n(1) Eh, it's probably just running late. Go back to sleep.\n(2) Something must be wrong. Go and investigate: ")
    while answer != "1" and answer !="2":
        printDelay("Try again. Choose from 1 or 2: ")
        answer=input()
    if answer=="1":
        sleepEnd()
    elif answer =="2":
        investigate()
elif answer == "2":
    printDelay("Fair enough. Your family will be sad though. Goodbye")