import requests
from datetime import datetime
import time
import pandas as pd
from geopy.geocoders import Nominatim
from django.conf import settings

api_key = settings.WEATHER_API_KEY


def cityWeather(location):
    geolocator = Nominatim(user_agent="trendLab")
    location = geolocator.geocode(location)
    lat = location.latitude
    lon = location.longitude
    part = "minutely,hourly"
    url_forecast = f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude={part}&appid={api_key}&units=metric"
    response = requests.get(url_forecast)
    data = response.json()
    return data


def get_city_data(location):
    city_id_url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"
    response = requests.get(city_id_url)
    data = response.json()
    city_id = data['id']
    return city_id


def getForecastData(data):
    daily_length = range(len(data['daily']))
    col_names = ['date', 'Temp', 'Temp_morn', 'Temp_eve', 'Temp_night', 'Temp_max', 'Temp_min', 'humidity', 'main',
                 'description', 'wind_speed', 'sunrise', 'sunset']
    df_forecast = pd.DataFrame(columns=col_names, index=daily_length)
    for ind in daily_length:
        daily = data['daily'][ind]
        dtime = time.localtime(daily['dt'])
        df_forecast.date[ind] = f"{dtime.tm_mday}/{dtime.tm_mon}/{dtime.tm_year}"
        df_forecast.Temp[ind] = daily['temp']['day']
        df_forecast.Temp_morn[ind] = daily['temp']['morn']
        df_forecast.Temp_eve[ind] = daily['temp']['eve']
        df_forecast.Temp_night[ind] = daily['temp']['night']
        df_forecast.Temp_min[ind] = daily['temp']['min']
        df_forecast.Temp_max[ind] = daily['temp']['max']
        df_forecast.humidity[ind] = daily['humidity']
        df_forecast.main[ind] = daily['weather'][0]['main']
        df_forecast.description[ind] = daily['weather'][0]['description']
        df_forecast.wind_speed[ind] = daily['wind_speed']
        df_forecast.sunrise[ind] = time.ctime(daily['sunrise'])
        df_forecast.sunset[ind] = time.ctime(daily['sunset'])
    df_forecast.set_index('date', inplace=True)
    return df_forecast
