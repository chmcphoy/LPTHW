cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available." # 100
print "There are only", drivers, "drivers available." # 30
print "There will be", cars_not_driven, "empty cars today." # 100 - 30 = 70 
print "We can transport", carpool_capacity, "people today" # 30 * 4.0 = 120.0
print "We have", passengers, "passengers to carpool today" # 90
print "We need to put about", average_passengers_per_car, "passengers per car" # 3

#Dont forget to use the , sign prior to/after the variable to minimize syntax errors
