import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve, urlopen, Request


def get_data(title, series, season):
    dict = {'острые козырьки': 'ostrye-kozyrki-na-anglijskom',
            'очень странные дела': 'ochen-strannye-dela-na-anglijskom'
            }
    link = f'http://lelang.su/english/{dict[title]}-{season}-sezon-{series}-seriya/'
    headers = {
        'accept': '* / *',
        'user - agent': 'Mozilla / 5.0 (Windows NT 10.0 ;Win64 ;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 108.0.0.0 Safari / 537.36'
    }
    req = requests.get(link, headers=headers).text
    bs = BeautifulSoup(req, 'lxml')
    videos = bs.find_all(class_='video')
    lst = [video.iframe['src'] for video in videos]
    # num = lst[0].split('/')[4]


    r = requests.get(lst[0], headers=headers).text
    soup = BeautifulSoup(r, 'lxml')
    # link = soup.video['src']




    # urlretrieve(link, 'video.mp4')
    #
    # req = Request(link)
    # req.add_header('user - agent', 'Mozilla / 5.0 (Windows NT 10.0 ;Win64 ;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 108.0.0.0 Safari / 537.36')
    # file_name = 'video1.mp4'
    # rsp = urlopen(link)
    # with open(file_name, 'wb') as f:
    #     f.write(rsp.read())

    return r

print(get_data('острые козырьки', 1, 1))