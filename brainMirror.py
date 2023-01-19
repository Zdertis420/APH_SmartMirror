import requests
import bs4

try:
    responseWeather=requests.get('https://yandex.ru/pogoda/')
    
    pageTemper=bs4.BeautifulSoup(responseWeather.content)
    pageWindSpeed = bs4.BeautifulSoup(responseWeather.content)

    responseTime=requests.get('https://time100.ru')
    
    pageTime=bs4.BeautifulSoup(responseTime.content)

    temper=pageTemper.find('span', 'temp__value temp__value_with-unit')
    time=pageTime.find('span', 'time')
    windspeed=pageWindSpeed.find('span', 'wind-speed')


    temper=temper.text
    time=time.text
    windspeed=windspeed.text
except ConnectionError:
    print('Проверьте ваше подключение к интернету')
