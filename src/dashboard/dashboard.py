import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
    QGridLayout,
    QGroupBox,
)
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPixmap
from src.dashboard.image_widget import ImageWidget
from src.weather.weather import Weather


class WeatherDashboard(QWidget):
    def __init__(self, config):
        super().__init__()
        self.config = config
        self.init_dashboard()
        if self.config.args.update:
            self.set_timer(self.config.args.time)

        if self.config.args.screenshot:
            # takes screenshot after second of delay
            QTimer.singleShot(1000, self.take_screenshot_and_exit)

    def init_dashboard(self):
        self.weather_obj = Weather(testkw=self.config.args.test)
        if self.config.args.size is not None:
            self.set_window_size(self.config.args.size)
        else:
            self.set_fullscreen()
        self.init_ui()

    def init_ui(self):
        w = self.weather_obj.weather
        wi = self.weather_obj.weather_imgs

        self.setWindowTitle("Weather Dashboard")
        main_layout = QGridLayout()
        # left, top, right, bottom
        main_layout.setContentsMargins(50, 50, 50, 20)

        # --- Current Weather Container ---
        current_weather_box = QGroupBox("Current Weather")
        current_weather_layout = QVBoxLayout()
        current_weather_layout.addWidget(
            QLabel(
                f"Last Updated: {w['current']['time'].split('T')[0]} {w['current']['time'].split('T')[1]}"
            )
        )
        current_weather_layout.addWidget(
            ImageWidget(
                wi["current"], svg=True, size=(60, 60)
            ).svgmap
        )
        current_weather_layout.addWidget(
            QLabel(
                f"Temperature / Feels Like: {w['current']['temperature_2m']} {w['current_units']['temperature_2m']} / "
                f"{w['current']['apparent_temperature']} {w['current_units']['temperature_2m']}"
            )
        )
        current_weather_layout.addWidget(
            QLabel(
                f"Humidity: {w['current']['relative_humidity_2m']} {w['current_units']['relative_humidity_2m']}"
            )
        )
        current_weather_layout.addWidget(
            QLabel(f"Max UV Index: {w['daily']['uv_index_max'][0]}")
        )
        current_weather_layout.addWidget(
            QLabel(
                f"Cloud Cover: {w['current']['cloud_cover']} {w['current_units']['cloud_cover']}"
            )
        )
        current_weather_layout.addWidget(
            QLabel(
                f"Wind Speed: {w['current']['wind_speed_10m']} {w['current_units']['wind_speed_10m']}"
            )
        )
        current_weather_layout.addWidget(
            QLabel(
                f"Total Precipitation: {w['current']['precipitation']} {w['current_units']['precipitation']}"
            )
        )
        current_weather_layout.addWidget(
            QLabel(f"Rain: {w['current']['rain']} {w['current_units']['rain']}")
        )
        current_weather_layout.addWidget(
            QLabel(
                f"Snowfall: {w['current']['snowfall']} {w['current_units']['snowfall']}"
            )
        )
        current_weather_layout.addWidget(
            QLabel(f"Sunrise: {w['daily']['sunrise'][0].split('T')[1]}")
        )
        current_weather_layout.addWidget(
            QLabel(f"Sunset: {w['daily']['sunset'][0].split('T')[1]}")
        )

        current_weather_box.setLayout(current_weather_layout)

        # --- Image Container ---
        image_box = QGroupBox("Weather Image")
        image_layout = QVBoxLayout()
        image_layout.addWidget(
            ImageWidget(wi["w_img"], svg=False, size=(200, 200))
        )
        image_box.setLayout(image_layout)

        # --- Forecast Container ---
        forecast_box = QGroupBox("Two Day Forecast")
        forecast_layout = QHBoxLayout()
        labels = ["Today", "Tomorrow"]
        for i in range(2):
            day_layout = QVBoxLayout()
            day_layout.addWidget(QLabel(labels[i]))
            day_layout.addWidget(QLabel(f"{w['daily']['time'][i]}"))
            day_layout.addWidget(
                ImageWidget(
                    wi["daily"][i], svg=True, size=(60, 60)
                ).svgmap
            )
            day_layout.addWidget(
                QLabel(
                    f"H/L: {w['daily']['temperature_2m_max'][i]}/{w['daily']['temperature_2m_min'][i]}"
                )
            )
            day_layout.addWidget(QLabel(f"Max UV: {w['daily']['uv_index_max'][i]}"))
            day_layout.addWidget(
                QLabel(
                    f"Precip %: {w['daily']['precipitation_probability_max'][i]}{w['daily_units']['precipitation_probability_max']}"
                )
            )
            day_layout.addWidget(
                QLabel(
                    f"Sunup: {w['daily']['sunrise'][i].split('T')[1]}"
                )
            )
            forecast_col = QWidget()
            forecast_col.setLayout(day_layout)
            forecast_layout.addWidget(forecast_col)
        forecast_box.setLayout(forecast_layout)

        # --- Add to main layout ---
        main_layout.addWidget(current_weather_box, 0, 0, 2, 1)
        main_layout.addWidget(image_box, 0, 1)
        main_layout.addWidget(forecast_box, 1, 1, 1, 1)

        self.setLayout(main_layout)

    def set_window_size(self, size):
        self.setFixedWidth(int(size[0]))  # height
        self.setFixedHeight(int(size[1]))  # height

    def set_fullscreen(self):
        app = QApplication.instance()
        screen = app.primaryScreen()
        geometry = screen.availableGeometry()
        self.setGeometry(geometry)

    def set_timer(self, time):
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.init_dashboard)
        self.timer.start(time)

    def take_screenshot_and_exit(self):
        pixmap = self.grab()
        pixmap.save(self.config.args.path)
        QApplication.instance().quit()
