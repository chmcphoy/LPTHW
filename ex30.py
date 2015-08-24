people = 30
cars = 40
buses = 15


if cars > people:
    print "We should tak the cars."
elif cars < people:
    print "We should not take the cars"
else:
    print "We can't decide."
    
if buses > cars:
    print "That's to many buses."
elif buses < cars:
    print "Maybe we could take the buses."
else:
    print "we still can't decide."
    
if people > buses:
    print "Alright let's just take the buses."
else:
    print "Fine, lets stay home then."
 
# Created my own.   
if cars > people and not(buses < cars):
    print "one."
elif cars < people and not(buses > cars):
    print "two."
else:
    print "three."
