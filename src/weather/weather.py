from os import listdir
from requests import get
from json import load
import sys


class Weather(object):
    def __init__(self, testkw=False):
        self.weather = self.get_weather_json(testkw=testkw)
        self.get_images()

    def get_weather_json(self, testkw=False):
        """
        Retrieve weather data from open-meteo API: https://open-meteo.com/

        """
        if testkw:
            with open("tests/test_files/example1.json") as file:
                trial = load(file)
            return trial
        else:
            return get(
                "https://api.open-meteo.com/v1/forecast?latitude=39.92026&longitude=-75.15935&daily=weather_code,temperature_2m_max,temperature_2m_min,sunrise,sunset,uv_index_max,precipitation_probability_max,precipitation_sum,precipitation_hours&current=temperature_2m,relative_humidity_2m,apparent_temperature,is_day,wind_speed_10m,wind_direction_10m,precipitation,rain,snowfall,weather_code,cloud_cover&timezone=America%2FNew_York&wind_speed_unit=mph&temperature_unit=fahrenheit&precipitation_unit=inch"
            ).json()

    def get_images(self):
        self.weather_imgs = {}
        self.weather_imgs["current"] = self.get_current_weather_img_path(path="./images/weather-icons/")
        self.weather_imgs["daily"] = self.get_forecast_img_paths(path="./images/weather-icons/")
        self.weather_imgs["w_img"] = self.get_weather_img_path(path="./images/winter-images/")

    def get_current_weather_img_path(self, path):
        if self.weather["current"]["precipitation"] > 20.0:
            return path + "wi-rain.svg"
        else:
            return path + "wi-day-sunny.svg"

    def get_forecast_img_paths(self, path):
        img_list = []
        for i in range(2):
            if self.weather["daily"]["precipitation_sum"][i] > 20.0:
                img_list.append(path + "wi-rain.svg")
            else:
                img_list.append(path + "wi-day-sunny.svg")
        return img_list

    def get_weather_img_path(self, path):
        return path + "1.jpg"
