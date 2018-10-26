import os,sys

class Song(object):
	"""docstring for Song"""
	def __init__(self, cat, filename, name):
		super(Song, self).__init__()
		self.name = name;
		self.filename = filename;
		self.cat = cat;
		self.mp3 = 'static/music/' + str(cat) + '/MP3/' + str(filename) + '.mp3'
		self.cover = 'static/music/' + str(cat) + '/covers/' + str(filename) + '.png'
		self.lyric = 'static/music/' + str(cat) + '/lyrics/' + str(filename) + '.txt'

def category(cname):
	if cname == 'Billboard':
		return songs

	pass


if __name__ == '__main__':
	billboard = 'static/music/Personal/lyrics/'
	songfiles = os.listdir(billboard)
	songs = {}
	# print(songs[0]- '.mp3')
	for songfile in songfiles:
		lyricfile = open(billboard + songfile)
		name = lyricfile.readline().strip('\n')
		# print(name)
		lyricfile.close()
		songname = os.path.splitext(songfile)[0]
		cursong = Song('Billboard', songname, name)
		# print(cursong.name)
		songs[songname] = cursong
		# print(cursong.cover)
	# print('sad' + songs['101_Issues'].mp3)

	print(list(category('Billboard').values())[0].name )



