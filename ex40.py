# from pg. 141 - 142

class Song(object):
    
    def __init__(self, lyrics):
        # self is necessary to acces the attribute
        self.lyrics = lyrics
   
    # always write self within the perenthises of methods within a class 
    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

# This creates an instance of the Song Class with a list of 3 strings.           
happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So i'll stop right there."])
                  
hmm = Song(["I don't want to get sued x2"])                 
                   
bulls_on_parade = Song(["They rally around the family",
                        "with pockets FULL of shells"])
                        
happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

hmm.sing_me_a_song()
