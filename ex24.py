print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation 
\n\twhere there is none.
"""

print "------------" 
print poem
print "------------"


five = 10 - 2 + 3 - 6
print "This should be five: %s" % five

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates
    
    
start_point = 1000
beanss, jarss, cratess = secret_formula(start_point)
# The above renders the function secret_formula to 3 variables

print "With a starting point of: %d " % start_point
print "We'd have %d beans, %d jars, and %d crates." % (beanss, jarss, cratess)
# The last print calls the function 3 times and the 3 variables get the
# return value since the return in the function had 3 variables!

start_point = start_point / 10

print "We can also do that this way: "
print "We'd have %d beans, %d jars and %d crates." % secret_formula(start_point)
# Alternative way of running it by having merely the function in format value.
