tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat


print '''
Testing\nout
anime\fkawai
wow\byareyrare
darkness\bneosphere
bebe\rlightnessphere
wind\vdragon
'''
# This was for testing various escape sequences on pg.39


print "%rI am the center of the multiland!" % '\t'
print "%sI am the center of the multiland!" % '\t' 
# See the difference %r and %s has in the shell? %r prints it exactly as you write it here
# So generally, %s is a better format when using escape sequences such as \t.
