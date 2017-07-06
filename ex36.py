from sys import exit


def start_room():
    print "You've been kidnapped and you're trying to escape."
    print "You stand in a round, stone room with 4 doors"
    print "Which door do you take? N, S, E, W"

    choice = raw_input("> ")

    mainKeyFound = False

    if "N" == choice.upper():
        north_hall()
    elif "S" == choice.upper():
        south_hall()
    elif "E" == choice.upper():
        east_room()
    elif "W" == choice.upper():
        west_room()
    else:
        print "No decision made, the guards have found you."
        print "Queen insists 'off with the head!'"

def west_room():
    print "You enter the West Room."
    print "Looking around you find the only way out to be the old wooden stairs."
    print "They are splintered into pieces, only the landing platform above remains."
    print "To go back to the starting room: S"

    choice = raw_input("> ")

    if "S" == choice.upper():
        start_room()
    else:
        print "Too slow, the guards have found you!"
        print "You are dragged to the dungeon to rot.  Good luck."

def north_hall():
    print "You enter the North Hall."
    print "Debris liters the hallway."
    print "At the end of the cold stone hallway is a closed door."
    print "Go to the door: G"
    print "Look around the debris: L"
    print "Go back to the starting room: S"

    firstKey = False

    choice = raw_input("> ")

    if "G" == choice.upper() and firstKey == False:
        print "The door is locked.  Do something quick before you're caught!"
    elif "L" == choice.upper() and firstKey == False:
        print "You hurriedly look through the debris, finding an old rusty key."
        firstKey = True


def start():
    start_room()


start()
