class Song(object):

	def __init__(self, lyrics):
		self.lyrics = lyrics

	def sing_me_a_song(self):
		for line in self.lyrics:
			print line

	def word_count(self):
		words = []
		for line in self.lyrics:
			words.append(len(line.split()))
		print "Number of words:", sum(words)

happy_bday = Song(["Happy birthday to you",
	"I don't want to get sued",
	"So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
	"With pockets full of shells"])

merry_christmas = Song(["This would be a Christmas song",
	"But it's the wrong time of year"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

merry_christmas.sing_me_a_song()

easter_lyrics = ["This is an Easter song",
	"Here is another line",
	"and this is where it ends"]

easter_song = Song(easter_lyrics)
easter_song.sing_me_a_song()

easter_song.word_count()

print dir(Song)