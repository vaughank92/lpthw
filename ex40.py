#Class example
class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

#lyrics are given as a list
happy_bday = Song(["Happy birthday to you",
                    "I don't want to get sued",
                    "So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
                        "With pockets full of shells"])

#lyrics stored in a varaible and then passed to instantiation
one_two = ["One two three four",
            "Tell me that you love me more"]

song = Song(one_two)

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

song.sing_me_a_song()
