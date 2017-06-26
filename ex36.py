from sys import exit


def start_room():
    print "You've been kidnapped and you're trying to escape."
    print "You stand in a round, stone room with 4 doors"
    print "Which door do you take? N, S, E, W"

    choice = raw_input("> ")

    if "N" in choice:
        north_room()
    elif "S" in choice:
        south_room()
    elif "E" in choice:
        east_room()
    elif "W" in choice:
        west_room()
    else:
        print "No decision made, the guards have found you."
        print "Queen insists 'off with the head!'"
