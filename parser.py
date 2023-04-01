import requests
from datetime import datetime

s_city = "Moscow,RU"
city_id = 524901
appid = "36864f4aec2acf7d8abf1d0afa33df75"


def getWeather():
    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                           params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
        data = res.json()
        print(data)

        temp = data['main']['temp']
        feelsLike = data['main']['feels_like']
        windSpeed = data['wind']['speed']
        conditions = data['weather'][0]['description']

    except Exception as e:
        print("Exception (weather):", e)
        pass

    return (temp, feelsLike, windSpeed, conditions)


def getTime():
    time = datetime.now().strftime('%H:%M:%S')
    return time
