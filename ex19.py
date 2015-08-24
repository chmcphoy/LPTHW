def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"
    
    
print "We can just give the function numbers (value) directly:"
cheese_and_crackers(50, 49)


print "OR, we can use variables from our script:"
amount_of_cheese =  33
amount_of_crackers = 43

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print "We can even do math inside too:"
cheese_and_crackers(22 + 999, 31 + 97)


print "And we can combine variables and math:"
cheese_and_crackers(amount_of_cheese + 77, amount_of_crackers - 20)
