the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

#first kind of for-loop goes through a list
for number in the_count:
    print "This is count %d" % number

#same as above
for fruit in fruits:
    print "A fruit of type: %s" % fruit

#mixed list
#%r is used since we don't know what's in it
for i in change:
    print "I got %r" % i

#building a list
#first create empty
elements = []

#range function to do 0 to 5 counts
#exclusive ending
for i in range(0, 6):
    print "Adding %d to the list." % i
    elements.append(i)

#print out created list
for i in elements:
    print "Element was: %d" % i

newList = range(0,8)

for i in newList:
    print "element: %d" % i

print newList
