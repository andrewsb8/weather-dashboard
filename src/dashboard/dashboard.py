import sys
import datetime
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
from src.dashboard.text_widget import TextWidget


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
        main_layout.setContentsMargins(50, 30, 50, 10)
        font_size = 24
        font_type = "Sans Serif"

        # --- Current Weather Container ---
        current_weather_box = QGroupBox()
        current_weather_box.setAlignment(Qt.AlignHCenter)
        current_weather_layout = QHBoxLayout()
        curr_weath_col_one = QVBoxLayout()

        date = datetime.datetime.strptime(
            w["current"]["time"].split("T")[0], "%Y-%m-%d"
        )
        normal_date = date.strftime("%B %d %Y")
        curr_weath_col_one.addWidget(
            TextWidget(
                text=f"{normal_date} at {w['current']['time'].split('T')[1]}",
                font=font_type,
                size=font_size,
            ),
            alignment=Qt.AlignCenter,
        )
        curr_weath_col_one.addWidget(
            ImageWidget(wi["current"], svg=True, size=(150, 150)).svgmap,
            alignment=Qt.AlignCenter,
        )
        curr_weath_col_one.addWidget(
            TextWidget(
                text=f"Temp / Feels: {w['current']['temperature_2m']} {w['current_units']['temperature_2m']} / "
                f"{w['current']['apparent_temperature']} {w['current_units']['temperature_2m']}",
                font=font_type,
                size=font_size,
            ),
            alignment=Qt.AlignCenter,
        )
        current_weather_layout.addLayout(curr_weath_col_one)

        curr_weath_col_two = QVBoxLayout()
        curr_weath_col_two.addWidget(
            TextWidget(
                text=f"Humidity: {w['current']['relative_humidity_2m']} {w['current_units']['relative_humidity_2m']}",
                font=font_type,
                size=font_size,
            ),
            alignment=Qt.AlignCenter,
        )
        curr_weath_col_two.addWidget(
            TextWidget(
                text=f"Max UV Index: {w['daily']['uv_index_max'][0]}",
                font=font_type,
                size=font_size,
            ),
            alignment=Qt.AlignCenter,
        )
        curr_weath_col_two.addWidget(
            TextWidget(
                text=f"Cloud Cover: {w['current']['cloud_cover']} {w['current_units']['cloud_cover']}",
                font=font_type,
                size=font_size,
            ),
            alignment=Qt.AlignCenter,
        )
        curr_weath_col_two.addWidget(
            TextWidget(
                text=f"Tot Precip: {w['current']['precipitation']} {w['current_units']['precipitation']}",
                font=font_type,
                size=font_size,
            ),
            alignment=Qt.AlignCenter,
        )
        current_weather_layout.addLayout(curr_weath_col_two)
        current_weather_box.setLayout(current_weather_layout)

        # --- Image Container ---
        image_box = QGroupBox()
        image_box.setAlignment(Qt.AlignHCenter)
        image_layout = QVBoxLayout()
        image_layout.addWidget(ImageWidget(wi["w_img"], svg=False, size=(400, 400)))
        image_box.setLayout(image_layout)

        # --- Forecast Container ---
        forecast_box = QGroupBox()
        forecast_box.setAlignment(Qt.AlignHCenter)
        forecast_layout = QHBoxLayout()
        labels = ["Today", "Tomorrow"]
        for i in range(2):
            day_layout = QVBoxLayout()
            day_layout.addWidget(
                TextWidget(text=labels[i], font=font_type, size=font_size),
                alignment=Qt.AlignCenter,
            )
            day_layout.addWidget(
                ImageWidget(wi["daily"][i], svg=True, size=(100, 100)).svgmap,
                alignment=Qt.AlignCenter,
            )
            day_layout.addWidget(
                TextWidget(
                    text=f"H/L: {w['daily']['temperature_2m_max'][i]}/{w['daily']['temperature_2m_min'][i]}",
                    font=font_type,
                    size=font_size,
                ),
                alignment=Qt.AlignCenter,
            )
            day_layout.addWidget(
                TextWidget(
                    text=f"Max UV: {w['daily']['uv_index_max'][i]}",
                    font=font_type,
                    size=font_size,
                ),
                alignment=Qt.AlignCenter,
            )
            day_layout.addWidget(
                TextWidget(
                    text=f"Precip %: {w['daily']['precipitation_probability_max'][i]}{w['daily_units']['precipitation_probability_max']}",
                    font=font_type,
                    size=font_size,
                ),
                alignment=Qt.AlignCenter,
            )
            forecast_col = QWidget()
            forecast_col.setLayout(day_layout)
            forecast_layout.addWidget(forecast_col)
        forecast_box.setLayout(forecast_layout)

        # --- Add to main layout ---
        main_layout.addWidget(current_weather_box, 0, 0, 1, 2)
        main_layout.addWidget(image_box, 1, 0)
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
