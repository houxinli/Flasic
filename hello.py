from flask import Flask
# from flask_script import Manager
from flask import render_template
from flask_bootstrap import Bootstrap
from flask import url_for
import os
import sys
# reload(sys) 
# sys.setdefaultencoding('utf8')

app = Flask(__name__)


@app.route('/')
def index():
	return render_template('index.html', songs = All, sname = 'Something_Just_Like_This')

@app.route('/Billboard')
def Billboard():
	return render_template('index.html', songs = Billboard, sname = 'Something_Just_Like_This')
	pass

@app.route('/Personal')
def Personal():
	return render_template('index.html', songs = Personal, sname = 'The_theme_of_Sachio')
	pass

@app.route('/song/Billboard/<sname>/')
def bsong(sname):
	return render_template('index.html', songs = Billboard, sname = sname)
	pass

@app.route('/song/Personal/<sname>/')
def psong(sname):
	return render_template('index.html', songs = Personal, sname = sname)
	pass


class Song(object):
	"""docstring for Song"""
	def __init__(self, cat, filename, name):
		super(Song, self).__init__()
		self.filename = filename;
		self.name = name;
		self.cat = cat;
		self.mp3 = 'music/' + str(cat) + '/MP3/' + str(filename) + '.mp3'
		self.cover = 'music/' + str(cat) + '/covers/' + str(filename) + '.png'
		self.shadow = 'music/' + str(cat) + '/covers/shadow/' + str(filename) + '.jpg'
		self.lyric = 'music/' + str(cat) + '/lyrics/' + str(filename) + '.txt'
		

if __name__ == '__main__':

	bpath = 'static/music/Billboard/lyrics/'
	bsongfiles = os.listdir(bpath)
	Billboard = {}
	for songfile in bsongfiles:
		lyricfile = open(bpath + songfile)
		name = lyricfile.readline().strip('\n')
		lyricfile.close()
		filename = os.path.splitext(songfile)[0]
		cursong = Song('Billboard', filename, name)
		Billboard[name] = cursong
		pass

	ppath = 'static/music/Personal/lyrics/'
	psongfiles = os.listdir(ppath)
	Personal = {}
	for songfile in psongfiles:
		lyricfile = open(ppath + songfile ,encoding='gb18030')
		name = lyricfile.readline().strip('\n')
		lyricfile.close()
		filename = os.path.splitext(songfile)[0]
		cursong = Song('Personal', filename, name)
		Personal[name] = cursong
		pass

	All = {**Billboard, **Personal} 

	app.run(debug = True)

