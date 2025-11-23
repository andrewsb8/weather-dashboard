import datetime
import os
import sys
from json import load
from random import randint

from requests import get


class Weather(object):
    def __init__(self, testkw=False):
        self.weather = self.get_weather_json(testkw=testkw)
        self.weather["normal_date"] = self.get_normal_date()
        self.weather_code_dict = self.get_weather_code_dict()
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

    def get_normal_date(self):
        date = datetime.datetime.strptime(
            self.weather["current"]["time"].split("T")[0], "%Y-%m-%d"
        )
        return date.strftime("%B %d %Y")

    def get_weather_code_dict(self):
        # weather codes as defined here:
        # https://open-meteo.com/en/docs/dwd-api
        return {
            0: {
                "img": "wi-day-sunny.svg",
                "desc": "Clear sky",
            },
            1: {
                "img": "wi-day-sunny.svg",
                "desc": "Mainly clear",
            },
            2: {
                "img": "wi-day-cloudy.svg",
                "desc": "Partly Cloudy",
            },
            3: {
                "img": "wi-cloudy.svg",
                "desc": "Overcast",
            },
            45: {
                "img": "wi-cloudy.svg",
                "desc": "Fog",
            },
            48: {
                "img": "wi-cloudy.svg",
                "desc": "Depositing Rime Fog",
            },
            51: {
                "img": "wi-rain.svg",
                "desc": "Light Drizzle",
            },
            53: {
                "img": "wi-rain.svg",
                "desc": "Moderate Drizzle",
            },
            55: {
                "img": "wi-rain.svg",
                "desc": "Intense Drizzle",
            },
            56: {
                "img": "wi-rain.svg",
                "desc": "Light Freezing Drizzle",
            },
            57: {
                "img": "wi-rain.svg",
                "desc": "Intense Freezing Drizzle",
            },
            61: {
                "img": "wi-rain.svg",
                "desc": "Slight Rain",
            },
            63: {
                "img": "wi-rain.svg",
                "desc": "Moderate Rain",
            },
            65: {
                "img": "wi-rain.svg",
                "desc": "Heavy Rain",
            },
            66: {
                "img": "wi-rain.svg",
                "desc": "Light Freezing Rain",
            },
            67: {
                "img": "wi-rain.svg",
                "desc": "Heavy Freezing Rain",
            },
            71: {
                "img": "wi-snow.svg",
                "desc": "Slight Snow",
            },
            73: {
                "img": "wi-snow.svg",
                "desc": "Moderate Snow",
            },
            75: {
                "img": "wi-snow.svg",
                "desc": "Heavy Snow",
            },
            77: {
                "img": "wi-snow.svg",
                "desc": "Snow Grains",
            },
            80: {
                "img": "wi-rain.svg",
                "desc": "Slight Rain Showers",
            },
            81: {
                "img": "wi-rain.svg",
                "desc": "Moderate Rain Showers",
            },
            82: {
                "img": "wi-rain.svg",
                "desc": "Violent Rain Showers",
            },
            85: {
                "img": "wi-snow.svg",
                "desc": "Slight Snow Showers",
            },
            86: {
                "img": "wi-snow.svg",
                "desc": "Moderate Snow Showers",
            },
            95: {
                "img": "wi-rain.svg",
                "desc": "Slight Thunderstorm",
            },
            96: {
                "img": "wi-rain.svg",
                "desc": "Moderate Thunderstorm",
            },
            99: {"img": "wi-rain.svg", "desc": "Thunderstorm with Hail"},
        }

    def get_images(self):
        self.weather_imgs = {}
        self.weather_imgs["current"] = self.get_current_weather_img_path(
            path="./images/weather-icons/"
        )
        self.weather_imgs["daily"] = self.get_forecast_img_paths(
            path="./images/weather-icons/"
        )
        self.weather_imgs["w_img"] = self.get_dress_img_path(path="./images/")

    def get_current_weather_img_path(self, path):
        if self.weather["current"]["weather_code"] in self.weather_code_dict:
            code = self.weather["current"]["weather_code"]
            return path + self.weather_code_dict[code]["img"]
        else:
            return path + "wi-day-sunny.svg"

    def get_forecast_img_paths(self, path):
        img_list = []
        for i in range(2):
            if self.weather["daily"]["weather_code"][i] in self.weather_code_dict:
                code = self.weather["daily"]["weather_code"][i]
                img_list.append(path + self.weather_code_dict[code]["img"])
            else:
                img_list.append(path + "wi-day-sunny.svg")
        return img_list

    def get_dress_img_path(self, path):
        if self.weather["daily"]["temperature_2m_max"][0] >= 95:
            path = path + "really-hot-images/"
        elif (
            self.weather["daily"]["temperature_2m_max"][0] >= 85
            and self.weather["daily"]["temperature_2m_max"][0] < 95
        ):
            path = path + "hot-images/"
        elif (
            self.weather["daily"]["temperature_2m_max"][0] < 85
            and self.weather["daily"]["temperature_2m_max"][0] >= 65
        ):
            if (
                self.weather["normal_date"].split()[0] == "March"
                or self.weather["normal_date"].split()[0] == "April"
                or self.weather["normal_date"].split()[0] == "May"
            ):
                path = path + "mid-spring-images/"
            elif (
                self.weather["normal_date"].split()[0] == "September"
                or self.weather["normal_date"].split()[0] == "October"
                or self.weather["normal_date"].split()[0] == "November"
            ):
                path = path + "mid-fall-images/"
            else:
                path = path + "cool-images/"
        elif (
            self.weather["daily"]["temperature_2m_max"][0] < 65
            and self.weather["daily"]["temperature_2m_max"][0] >= 50
        ):
            path = path + "cool-images/"
        elif (
            self.weather["daily"]["temperature_2m_max"][0] < 50
            and self.weather["daily"]["temperature_2m_max"][0] > 32
        ):
            path = path + "cold-images/"
        elif self.weather["daily"]["temperature_2m_max"][0] <= 32:
            path = path + "really-cold-images/"

        files = os.listdir(path)
        # if no files or path added
        if path == "./images/" or len(files) == 0:
            return path + "confused-image/1.jpg"
        else:
            while True:
                rand = randint(0, len(files) - 1)
                file = os.path.join(path, files[rand])
                if os.path.isfile(file):
                    return file
