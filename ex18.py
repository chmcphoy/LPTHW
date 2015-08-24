def print_tre(arg1, arg2, arg3):
    print "arg1: %r, arg2: %r, arg3: %r" % (arg1, arg2, arg3)

# This one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# That args* is actually pointless. We can just do this:
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)
    
# Example of one argument
def print_one(arg1):
    print "arg1: %r" % arg1
    
# No arguments
def print_none():
    print "Nothing here."
    
# Assign values to arguments.    
print_tre("Three","Two", "Ett")
print_two("Chuma","Mcphoy")
print_two_again("Chuma","Mcphoy")
print_one("Mezzi")
print_none()
