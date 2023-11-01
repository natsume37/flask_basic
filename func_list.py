# coding:utf-8
# USER: 冷不丁
# @FILE_NAME: func_list
# @TIME: 2023/11/1 12:51
import requests
import re


def search_of_name(name):
    url = f"https://music.163.com/api/search/get?s={name}&type=1&limit=2"
    res = requests.get(url)
    return res.json()


def clean_json(name):
    songs = []
    res = search_of_name(name)
    for song in res['result']['songs']:
        singer_list = []
        song_id = song['id']
        name = song['name']
        form = song['album']['name']
        # 歌手
        for singer in song['artists']:
            singer_list.append(singer['name'])
        songs.append(
            {
                'song_id': song_id,
                'name': name,
                'form': form,
                'singer_list': singer_list,
            }
        )
    return songs


if __name__ == '__main__':
    # res = clean_json("十年")
    # for i in res:
    #     print(i['song_id'],i['name'])
    search_of_name("十年")