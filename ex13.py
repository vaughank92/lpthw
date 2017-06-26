from sys import argv

# script, first, second, third = argv
#
# print "The script is called:", script
# print "Your first variable is:", first
# print "Your second variable is:", second
# print "Your third variable is:", third

script, firstInput = argv

rawInput = raw_input("%r is a variable, name another " % firstInput);
print rawInput;
