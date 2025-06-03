from textual.app import App
from textual.widgets import Static, Header
from textual.containers import Grid, Container, Horizontal
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
                yield Static(f"Last Updated: {self.weather_obj.weather["current"]["time"].split("T")[0]} {self.weather_obj.weather["current"]["time"].split("T")[1]}")
                yield Static(f"Temperature / Feels Like: {self.weather_obj.weather["current"]["temperature_2m"]} {self.weather_obj.weather["current_units"]["temperature_2m"]} / {self.weather_obj.weather["current"]["apparent_temperature"]} {self.weather_obj.weather["current_units"]["temperature_2m"]}")
                yield Static(f"Humidity: {self.weather_obj.weather["current"]["relative_humidity_2m"]} {self.weather_obj.weather["current_units"]["relative_humidity_2m"]}")
                yield Static(f"Wind Speed: {self.weather_obj.weather["current"]["wind_speed_10m"]} {self.weather_obj.weather["current_units"]["wind_speed_10m"]}")
                yield Static(f"Cloud Cover: {self.weather_obj.weather["current"]["cloud_cover"]} {self.weather_obj.weather["current_units"]["cloud_cover"]}")
                yield Static(f"Precipitation: {self.weather_obj.weather["current"]["precipitation"]} {self.weather_obj.weather["current_units"]["precipitation"]}")
                yield Static(f"Rain: {self.weather_obj.weather["current"]["rain"]} {self.weather_obj.weather["current_units"]["rain"]}")
                yield Static(f"Snowfall: {self.weather_obj.weather["current"]["snowfall"]} {self.weather_obj.weather["current_units"]["snowfall"]}")

            # Image Container
            with Container(classes="box-two-row"):
                yield ImageWidget("images/winter-images/1.jpg", (30, 30))

            # Forecast Container
            with Container(classes="box-two-col"):
                yield Static("Seven Day Forecast", classes="center-text")
                with Horizontal():
                    yield Static(f'first one')
                    # below doesn't show up
                    yield Static(f'second one')
                    yield Static(f'third one')


    def on_mount(self):
        pass
