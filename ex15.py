from sys import argv

script, filename = argv

#opens the file
txt = open(filename)

print "Here's your file %r:" % filename
#Reads the file
print txt.read()

txt.close();

print "Type the filename again:"
#gets the file name
file_again = raw_input("> ")

#opens the file
txt_again = open(file_again)

#reads the file again
print txt_again.read()

txt_again.close()
