import re
import json
import urllib.request
import requests
from bs4 import BeautifulSoup
import os,sys


headers = { 
        'Referer':'http://music.163.com/',
        'Host':'music.163.com',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0 Iceweasel/38.3.0', 
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8' 
}


def getPlaylist(lid = '2256615030'):
    playlist_url = 'http://music.163.com/playlist?id=' + str(lid)

    soup = BeautifulSoup(session.get(playlist_url, headers = headers).content, 'lxml')
    musics = soup.select('#song-list-pre-cache a')
    lname = soup.find('h2').get_text()
    # print(lname)
    playlist = {}
    playlist['lid'] = str(lid)
    playlist['name'] = lname
    sids = []
    for music in musics:
    	sid = music['href'].strip("/song?id=")
    	sids.append(sid)
    	# snames.append( music.get_text() )
    playlist['sids'] = sids

    return playlist

def downloadSong(sid, file_path):
    url = 'http://music.163.com/song/media/outer/url?id=' + str(sid)
    urllib.request.urlretrieve(url, file_path + '/' + str(sid) + '.mp3')

if __name__ == '__main__':
    # lid = input('input the playlist id:')
    playlists_file = open("static/playlists.json", encoding = 'utf-8')
    print("file", playlists_file)
    playlists = json.loads(playlists_file)
    lids = ['2256615030']
    file_path = 'music'
    # song_names, song_ids = getPlaylist(lid)
    session = requests.session()
    for lid in lids:
    	if playlists.has_key(lid):
    		pass
    	else :
    		playlist = getPlaylist(lid)
    		playlists['lid'] = playlist
    		for sid in playlist['sids']:
    			downloadSong(sid, file_path)


    # for i in range(len(song_names)):
    #     get_song(song_ids[i], i + 1, 'songs')
    #     get_cover_img(song_ids[i], i + 1, 'imgs')
    #     get_lyric(song_ids[i], song_names[i], i + 1, 'lyrics')
    #     print('progress: %d/%d' % (i + 1, len(song_names)))


    # print(filenames)
    # print(filenames[0]- '.mp3')
    print('All done!'[:-2])
    url = 'http://music.163.com/song/media/outer/url?id=569214321.mp3'
    url = ' http://music.163.com/api/song/detail/?id=569214321&ids=%5B569214321%5D'
    # url = 'http://music.163.com/api/song/lyric?os=pc&id=569214321&lv=-1&kv=-1&tv=-1'
    try:
    	soup = (session.get(url, headers = headers).content , 'lxml' )
    	r = session.get(url, headers = headers)
    	print(r.status_code)
    	detail = json.loads(r.text)
    	print( type(detail) )
    	print( json.dumps(detail, sort_keys=True, indent=4, separators=(',', ': ') ) )
    	# urllib.request.urlretrieve(url, 'GALWAYGIRL.mp3')
    	print("success")
    	print(soup.prettify() )
    	print("ii")
    except Exception as e:
    	if hasattr(e, 'reason'):
    		print("error, reason:", e.reason)

