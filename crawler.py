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

count = 0

def getPlaylist(lid = '2256615030'):
    playlist_url = 'http://music.163.com/playlist?id=' + str(lid)

    soup = BeautifulSoup(session.get(playlist_url, headers = headers).content, 'lxml')
    musics = soup.select('#song-list-pre-cache a')
    lname = soup.find('h2').get_text()
    # print(lname)
    playlist = {}
    playlist['lid'] = str(lid)
    playlist['lname'] = lname
    sids = []
    for music in musics:
        sid = music['href'].strip("/song?id=")
        sids.append(sid)
        # snames.append( music.get_text() )
    playlist['sids'] = sids

    return playlist

# def downloadSong(sid, file_path):

def getSong(sid):
    global count
    song = {}
    song['sid'] = sid
    try:
        url = 'http://music.163.com/song/media/outer/url?id=' + str(sid)
        urllib.request.urlretrieve(url, 'static/music/audio/' + str(sid) + '.mp3')

        # handle cover & info
        url = 'http://music.163.com/song?id=' + str(sid)
        soup = BeautifulSoup(session.get(url, headers = headers).content, 'lxml')
        sname = soup.select('em.f-ff2')[0].get_text()
        artists = []
        artist_elements = soup.select("p.des span a")
        for element in artist_elements:
            aid = element['href'].strip("/artist?id=")
            aname = element.get_text()
            artists.append({"aid":aid , "aname": aname})
        album_element = soup.select("p.des > a")[0]
        alid = album_element['href'].strip("/album?id=")
        alname = album_element.get_text()
        album = {"alid": alid, "alname": alname}
        # download cover
        img_element = soup.select('.cvrwrap img')[0]
        url = img_element['src'].replace('130', '150')
        urllib.request.urlretrieve(url, 'static/music/cover/' + str(sid) + ".png" )
        
        # handle lyrics
        url = 'http://music.163.com/api/song/lyric?id=' + str(sid) + '&lv=1&tv=-1&kv=1'
        response = requests.get(url, headers = headers)
        text = response.text
        lyrics_json = json.loads(text)
        # print(json.dumps(lyrics_json, indent = 4, ensure_ascii=False))
        lyrics_file = open('static/music/lyrics/' + str(sid) + '.txt', 'w+', encoding='utf-8' )
        lyrics_file.write(sname + '\nArtists:')
        for artist in artists:
            lyrics_file.write(artist['aname'] + '/ ')
        lyrics_file.write('\nAlbum:' + str(alname) + '\n\n')
        try:
            lyrics = lyrics_json['lrc']['lyric']
            lines = re.findall( r'\[.*\](.*)', lyrics )
            for line in lines:
                lyrics_file.write(line.strip() + '\n' )
        except :
            lyrics_file.write('No lyrics\n')
        finally:
            lyrics_file.close()

        # handle song object
        song['sname'] = sname
        song['artists'] = artists
        song['album'] = album
        count += 1
        print("No.",str(count) , ": " , sname, "...100%")
        return song

    except RequestException as e:
        if hasattr(e, 'reason' ):
            print("Error, reason:", e.reason)
        else:
            print("Oops, unexpected request error")
    except Exception as e:
        print("unexpected error")

def init():
    if not os.path.exists("static"):
        os.mkdir('static')
    if not os.path.exists('static/music'):
        os.mkdir('static/music')

    if os.path.exists("static/music/playlists.json"):
        os.remove("static/music/playlists.json")
        pass
    else:
        playlists_file = open("static/music/playlists.json",'w+', encoding = 'utf-8')
        playlists_file.write('{}')
        playlists_file.close()
    if os.path.exists("static/music/songs.json"):
        os.remove("static/music/songs.json")
        pass
    else:
        songs_file = open("static/music/songs.json",'w+', encoding = 'utf-8')
        songs_file.write('{}')
        songs_file.close()
    if not os.path.exists('static/music/audio'):
        os.mkdir('static/music/audio')
    if not os.path.exists('static/music/cover'):
        os.mkdir('static/music/cover')
    if not os.path.exists('static/music/lyrics'):
        os.mkdir('static/music/lyrics')
    pass

if __name__ == '__main__':
    session = requests.session()

    init()
    playlists_file = open("static/music/playlists.json",'r+', encoding = 'utf-8')
    songs_file = open("static/music/songs.json",'r+', encoding = 'utf-8')
    playlists = json.load(playlists_file)
    songs = json.load(songs_file)
    songs_file.close()
    playlists_file.close()

    lids = ['993510552', '540425046', '503865635', '409336560']
    # lids = ['503865635', '409336560'] # 在此处控制需要的歌单列表
    for lid in lids:
        if lid in playlists:
            pass
        else :
            playlist = getPlaylist(lid)
            playlists[lid] = playlist
            for sid in playlist['sids']:
                if sid in songs:
                    pass
                else:
                    try:
                        song = getSong(sid)
                    except Exception as e:
                        raise e
                    songs[sid] = song

    # print(songs)
    # print(playlists)
    playlists_file = open("static/music/playlists.json",'w+', encoding = 'utf-8')
    songs_file = open("static/music/songs.json",'w+', encoding = 'utf-8')
    json.dump(songs, songs_file, indent = 4, ensure_ascii = False, sort_keys = True)
    json.dump(playlists, playlists_file, indent = 4, ensure_ascii = False, sort_keys = True)
    songs_file.close()
    playlists_file.close()
    print("下载完成! 本次共下载：", count, "首歌曲")


