#takes any number of arguments
def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)

def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

#this takes one argument
def print_one(arg1):
    print "arg1: %r" % arg1

#this takes no arguments
def print_none():
    print "No arguments"

print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()