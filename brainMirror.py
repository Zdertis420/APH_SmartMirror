import requests
import bs4

try:
    responseWeather=requests.get('https://yandex.ru/pogoda/')
    pageWeather=bs4.BeautifulSoup(responseWeather.content)
    responseTime=requests.get('https://time100.ru')
    pageTime=bs4.BeautifulSoup(responseTime.content)

    wether=pageWeather.find('span', 'temp__value temp__value_with-unit')
    time=pageTime.find('span', 'time')

    wether=wether.text
    time=time.text
except ConnectionError:
    print('Проверьте ваше подключение к интернету')
#print(wether)
