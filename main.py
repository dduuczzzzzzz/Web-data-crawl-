from bs4 import BeautifulSoup
import requests
import time

def nettruyen():
    headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"}
    html_text = requests.get('http://www.nettruyengo.com/', headers = headers).text
    soup = BeautifulSoup(html_text, 'lxml')
    comics = soup.find_all('div', class_ = 'item')
    for index, comic in enumerate(comics):
        name = comic.find('div', class_ = 'title')
        more_info = comic.find('div', class_ = 'box_text')
        time = comic.find('i', class_ = 'time')
        info = comic.find('div', class_ = 'message_main')
        if name != None :
            print(f'Manga name: {name.text.strip()}')
        if more_info!=None:
            print(f'More info about this: {more_info.text.strip()}')
        if time!= None:
            print(f'New update: {time.text.strip()}')
        if(info!=None):
            print(info.text.strip())
        print('')

if __name__ == '__main__' :
    while True:
        nettruyen()
        time_wait = 3
        print(f'Waiting for {time_wait} minutes')
        time.sleep(time_wait*60)
