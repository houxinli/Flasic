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


def get_playlist_songs(playlist_id = '626907603'):
    playlist_url = 'http://music.163.com/playlist?id=' + str(playlist_id)

    sess = requests.session()
    resp = BeautifulSoup(sess.get(playlist_url, headers = headers).content, 'lxml')
    musics = resp.find('ul', {'class': 'f-hide'})

    song_names = []
    song_ids = []
    for music in musics.find_all('a'):
        song_names.append(music.text)
        song_ids.append(music['href'][music['href'].index('=') + 1:])
        # print('{}: {}'.format(music.text, music['href'][music['href'].index('=') + 1:]))

    return song_names, song_ids

def get_song(song_id, index, file_path):
    url = 'http://music.163.com/song/media/outer/url?id=' + str(song_id)
    urllib.request.urlretrieve(url, file_path + '/' + str(index) + '.mp3')

def get_cover_img(song_id, index, file_path):
    url = 'http://music.163.com/song?id=' + str(song_id)
    sess = requests.session()
    content = BeautifulSoup(sess.get(url, headers = headers).content, 'lxml')
    imgs = content.find_all('img')
    img_urls = [img.get('src') for img in imgs]
    # print(img_urls)

    if len(img_urls) != 0:
        urllib.request.urlretrieve(img_urls[0], file_path + '/' + str(index) + '.jpg')


def get_lyric(song_id, song_name, index, file_path):
    url = 'http://music.163.com/api/song/lyric?id=' + str(song_id) + '&lv=1&kv=1&tv=-1'
    lyric = requests.get(url)
    lyric = lyric.text
    lyric = json.loads(lyric)

    f = open(file_path + '/' + str(index) + '.txt', 'w')
    f.writelines(song_name + '\n')
    try:
        l = lyric['lrc']['lyric']
        pattern = re.compile(r'\[.*\]')
        l = re.sub(pattern, '', l)
        l = l.strip()
        f.writelines(l)
        f.close()
        return l
    except:
        f.writelines('No lyric for this song')
        f.close()
        return ''

if __name__ == '__main__':
    # playlist_id = input('input the playlist id:')
    # playlist_id = '626907603'
    # song_names, song_ids = get_playlist_songs(playlist_id)

    # for i in range(len(song_names)):
    #     get_song(song_ids[i], i + 1, 'songs')
    #     get_cover_img(song_ids[i], i + 1, 'imgs')
    #     get_lyric(song_ids[i], song_names[i], i + 1, 'lyrics')
    #     print('progress: %d/%d' % (i + 1, len(song_names)))

    billboard = 'Billboard/MP3/'
    filenames = os.listdir(billboard)
    a = os.path.splitext(filenames[0])
    # print(filenames)
    # print(filenames[0]- '.mp3')
    print(a[0])
    print('All done!')