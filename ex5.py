myname = 'Chuma Mc Phoy' 
myage = 20
myheight = 175 # centimeters
myweight = 65 # kg
myeyes = 'Brown'
myhair = 'Black'
myteeth = 'White'


print "Let's talk about %r." % myname
print "He's %r centimeters tall." % myheight
print "He weighs %r kg" % myweight
print "He's got %r eyes and %r hair." % (myeyes, myhair)
print "His teeth are usually %r, depending on the coffee" % myteeth

# this line is tricky, try to get it exactly right
print "if I add %r, %r and %r i get %r." % (myage, myheight, myweight, myage + myheight + myweight)

