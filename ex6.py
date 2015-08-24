x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s" % (binary, do_not)

print x # We don't need " marks over x since its assigned value already contains them.  
print y # Same here.

print "I said %r." % x # the %r is a formatted variable meaning its linked to the variable (x) after the " mark.
print "I also said: %s" % y # Same here.

hilarious = False 
joke_evaluation = "Isn't that joke so funny?! %r" 

print joke_evaluation % hilarious 

w = "This is the left side of..."
e = "a string with a right side."

print w + e # Simply adds the 2 sentences together.
