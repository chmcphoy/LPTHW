from sys import argv 

script, filename = argv

txt = open(filename)
# open is a command that reads our text file
# (As long as you type in the filename in the 
# command line when you run the script.)

print "Here's your file %r" % filename
print txt.read()
# 'txt' is the variable/object, .(dot) is the
# object operator. 'read' is the command

# And this does it all over from with the script
print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()

txt.close()
txt_again.close()
