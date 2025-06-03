from textual.app import App
from textual.widgets import Static, Header
from textual.containers import Grid, Container, Horizontal, Vertical
from src.weather.weather import Weather
from src.dashboard.image_widget import ImageWidget


class WeatherDashboard(App):
    CSS_PATH = "style.tcss"

    def __init__(self, testkw=False):
        self.testkw = testkw
        self.weather_obj = Weather(testkw=self.testkw)
        super().__init__()

    def compose(self):
        yield Header("Custom")
        with Grid(id="app-grid"):
            # Current Weather Container
            with Container(classes="box-two-row"):
                yield Static("Current Weather", classes="center-text")
                yield Static(f"Last Updated: {self.weather_obj.weather["current"]["time"].split("T")[0]} {self.weather_obj.weather["current"]["time"].split("T")[1]}", classes="center-text")
                yield Static("")

                yield Static("Temperature Information", classes="center-text")
                yield Static(f"Temperature / Feels Like: {self.weather_obj.weather["current"]["temperature_2m"]} {self.weather_obj.weather["current_units"]["temperature_2m"]} / {self.weather_obj.weather["current"]["apparent_temperature"]} {self.weather_obj.weather["current_units"]["temperature_2m"]}")
                yield Static(f"Humidity: {self.weather_obj.weather["current"]["relative_humidity_2m"]} {self.weather_obj.weather["current_units"]["relative_humidity_2m"]}")
                yield Static(f"Max UV Index: {self.weather_obj.weather["daily"]["uv_index_max"][0]}")
                yield Static(f"Cloud Cover: {self.weather_obj.weather["current"]["cloud_cover"]} {self.weather_obj.weather["current_units"]["cloud_cover"]}")
                yield Static(f"Wind Speed: {self.weather_obj.weather["current"]["wind_speed_10m"]} {self.weather_obj.weather["current_units"]["wind_speed_10m"]}")
                yield Static("")

                yield Static("Precipitation Information", classes="center-text")
                yield Static(f"Total Precipitation: {self.weather_obj.weather["current"]["precipitation"]} {self.weather_obj.weather["current_units"]["precipitation"]}")
                yield Static(f"Rain: {self.weather_obj.weather["current"]["rain"]} {self.weather_obj.weather["current_units"]["rain"]}")
                yield Static(f"Snowfall: {self.weather_obj.weather["current"]["snowfall"]} {self.weather_obj.weather["current_units"]["snowfall"]}")
                yield Static("")

                yield Static("Daylight Information", classes="center-text")
                yield Static(f"Sunrise: {self.weather_obj.weather["daily"]["sunrise"][0].split("T")[1]}")
                yield Static(f"Sunset: {self.weather_obj.weather["daily"]["sunset"][0].split("T")[1]}")

            # Image Container
            with Container(classes="box-two-row"):
                yield ImageWidget("images/winter-images/1.jpg", (30, 30))

            # Forecast Container
            with Container(classes="box-two-col"):
                yield Static("Seven Day Forecast", classes="center-text")
                with Horizontal():
                    for i in range(7):
                        with Vertical(classes="horizontal-box"):
                            yield Static(f'{self.weather_obj.weather["daily"]["time"][i]}', classes="center-text")
                            yield Static(f'H/L: {self.weather_obj.weather["daily"]["temperature_2m_max"][i]}/{self.weather_obj.weather["daily"]["temperature_2m_min"][i]}', classes="center-text")
                            yield Static(f"Max UV: {self.weather_obj.weather["daily"]["uv_index_max"][i]}", classes="center-text")
                            yield Static(f'Precip %: {self.weather_obj.weather["daily"]["precipitation_probability_max"][i]}{self.weather_obj.weather["daily_units"]["precipitation_probability_max"]}', classes="center-text")
                            yield Static(f"Sunup/down: {self.weather_obj.weather["daily"]["sunrise"][i].split("T")[1]}/{self.weather_obj.weather["daily"]["sunset"][i].split("T")[1]}", classes="center-text")

    def on_mount(self):
        pass
