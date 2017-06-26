
def whileLoop(ending, increment = 1):
    i = 0
    numbers = []

    while i < ending:
        print "At the top i is %d" % i
        numbers.append(i)

        i += increment
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

    print "The numbers: "

    for num in numbers:
        print num
    print "~~~~~~~~~~~~~~~End While~~~~~~~~~~~~~~~~~~~"

def forLoop(ending, increment = 1):
    i = 0
    numbers = []

    #range(start, end, step)
    for num in range(i, ending, increment):
        print "num is %d" % num
        numbers.append(num)
        print "num does not need to increment until it loops again"

    print "Numbers: ", numbers
    print "~~~~~~~~~~~~~~~End For~~~~~~~~~~~~~~~~~~~"


whileLoop(3)
forLoop(3)
whileLoop(10, 2)
forLoop(10, 2)
