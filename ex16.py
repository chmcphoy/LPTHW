from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("? ")

print "Opening the file..."
target = open(filename, "w")

print "Truncating the file. Goodbye!"
target.truncate()
# Truncate is a function to empty/clear the file.

print "Now I'm going to ask you for three lines."

line1 = raw_input("line1: ")
line2 = raw_input("line2: ")
line3 = raw_input("line3: ")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
# The 'write' function puts whatever is in
# The parameter into the file(object).

print "And finally, we close it."
target.close()
