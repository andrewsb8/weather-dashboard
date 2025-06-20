import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QGridLayout, QGroupBox
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from src.dashboard.image_widget import ImageWidget
from src.weather.weather import Weather

class WeatherDashboard(QWidget):
    def __init__(self, testkw=False):
        super().__init__()
        self.testkw = testkw
        self.weather_obj = Weather(testkw=self.testkw)
        self.init_ui()
        app = QApplication.instance()
        screen = app.primaryScreen()
        geometry = screen.availableGeometry()
        self.setGeometry(geometry)

    def init_ui(self):
        self.setWindowTitle("Weather Dashboard")
        main_layout = QGridLayout()

        # --- Current Weather Container ---
        current_weather_box = QGroupBox("Current Weather")
        current_layout = QVBoxLayout()
        w = self.weather_obj.weather

        current_layout.addWidget(QLabel(
            f"Last Updated: {w['current']['time'].split('T')[0]} {w['current']['time'].split('T')[1]}"
        ))
        current_layout.addWidget(QLabel(
            f"Temperature / Feels Like: {w['current']['temperature_2m']} {w['current_units']['temperature_2m']} / "
            f"{w['current']['apparent_temperature']} {w['current_units']['temperature_2m']}"
        ))
        current_layout.addWidget(QLabel(
            f"Humidity: {w['current']['relative_humidity_2m']} {w['current_units']['relative_humidity_2m']}"
        ))
        current_layout.addWidget(QLabel(
            f"Max UV Index: {w['daily']['uv_index_max'][0]}"
        ))
        current_layout.addWidget(QLabel(
            f"Cloud Cover: {w['current']['cloud_cover']} {w['current_units']['cloud_cover']}"
        ))
        current_layout.addWidget(QLabel(
            f"Wind Speed: {w['current']['wind_speed_10m']} {w['current_units']['wind_speed_10m']}"
        ))
        current_layout.addWidget(QLabel(
            f"Total Precipitation: {w['current']['precipitation']} {w['current_units']['precipitation']}"
        ))
        current_layout.addWidget(QLabel(
            f"Rain: {w['current']['rain']} {w['current_units']['rain']}"
        ))
        current_layout.addWidget(QLabel(
            f"Snowfall: {w['current']['snowfall']} {w['current_units']['snowfall']}"
        ))
        current_layout.addWidget(QLabel(
            f"Sunrise: {w['daily']['sunrise'][0].split('T')[1]}"
        ))
        current_layout.addWidget(QLabel(
            f"Sunset: {w['daily']['sunset'][0].split('T')[1]}"
        ))
        current_weather_box.setLayout(current_layout)

        # --- Image Container ---
        image_box = QGroupBox("Weather Image")
        image_layout = QVBoxLayout()
        image_layout.addWidget(ImageWidget("images/winter-images/1.jpg", size=(120, 120)))
        image_box.setLayout(image_layout)

        # --- Forecast Container ---
        forecast_box = QGroupBox("Five Day Forecast")
        forecast_layout = QHBoxLayout()
        for i in range(5):
            day_layout = QVBoxLayout()
            day_layout.addWidget(QLabel(f"{w['daily']['time'][i]}"))
            day_layout.addWidget(ImageWidget("images/weather-icons/icons8-sun-20.png", size=(20, 20)))
            day_layout.addWidget(QLabel(
                f"H/L: {w['daily']['temperature_2m_max'][i]}/{w['daily']['temperature_2m_min'][i]}"
            ))
            day_layout.addWidget(QLabel(
                f"Max UV: {w['daily']['uv_index_max'][i]}"
            ))
            day_layout.addWidget(QLabel(
                f"Precip %: {w['daily']['precipitation_probability_max'][i]}{w['daily_units']['precipitation_probability_max']}"
            ))
            day_layout.addWidget(QLabel(
                f"Sunup/down: {w['daily']['sunrise'][i].split('T')[1]}/{w['daily']['sunset'][i].split('T')[1]}"
            ))
            forecast_col = QWidget()
            forecast_col.setLayout(day_layout)
            forecast_layout.addWidget(forecast_col)
        forecast_box.setLayout(forecast_layout)

        # --- Add to main layout ---
        main_layout.addWidget(current_weather_box, 0, 0)
        main_layout.addWidget(image_box, 0, 1)
        main_layout.addWidget(forecast_box, 1, 0, 1, 2)

        self.setLayout(main_layout)
