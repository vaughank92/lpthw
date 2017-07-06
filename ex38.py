ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there are not 10 things in that list. Let's fix that."

#splits on the space to make a list
stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

#adds more_stuff to stuff until there are 10 things
while len(stuff) != 10:
    next_one = more_stuff.pop()
    print "Adding: ", next_one
    stuff.append(next_one)
    print "There are %d items now." % len(stuff)

print "There we go: ", stuff

print "Let's do some things with stuff."

#stuff at position 1
print stuff[1]
#stuff at position -1 (last spot)
print stuff[-1]
#removes the last item from list
print stuff.pop()
#makes everything a string, joined by a space
print ' '.join(stuff)
#takes items in the 3 and 5 spot and joins with a #
print '#'.join(stuff[3:5])
