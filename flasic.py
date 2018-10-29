from flask import Flask
# from flask_script import Manager
from flask import render_template
from flask_bootstrap import Bootstrap
from flask import url_for
import os
import sys
import json

# reload(sys) 
# sys.setdefaultencoding('utf8')

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', playlists = All, songs = songs)

@app.route('/song/<sid>/')
def song(sid):
    return render_template('index.html', playlists = All, songs = songs, sid = sid)
    pass

@app.route('/playlist/<lid>/')
def playlist(lid):
    return render_template('index.html', playlists = All, songs = songs, lid = lid )
    pass

class Song(object):
    """docstring for Song"""
    def __init__(self, sid):
        super(Song, self).__init__()
        self.sid = sid;
        self.lyric = 'music/lyrics/' + str() + '.txt'

def mpath(sid, r):
    path = 'music/' + str(r) + '/' + str(sid)
    if str(r) == 'audio' :
        path += '.mp3'
    elif str(r) == 'cover' :
        path += '.png'
    elif str(r) == 'lyrics' :
        path += '.txt'
    return path
        

if __name__ == '__main__':

    playlists_file = open("static/music/playlists.json",'r+', encoding = 'utf-8')
    songs_file = open("static/music/songs.json",'r+', encoding = 'utf-8')
    # playlists = json.load(playlists_file)
    All = json.load(playlists_file)
    songs = json.load(songs_file)
    # All = list(playlists.values())
    songs_file.close()
    playlists_file.close()

    app.add_template_global(mpath, 'mpath')
    app.run(debug = True)

