from textual.app import App
from textual.widgets import Static
from textual.containers import Grid, Container
from src.weather.weather import Weather
from src.dashboard.image_widget import ImageWidget


class WeatherDashboard(App):
    CSS_PATH = "style.tcss"

    def __init__(self, testkw=False):
        self.testkw = testkw
        self.weather_obj = Weather(testkw=self.testkw)
        super().__init__()

    def compose(self):
        with Grid(id="app-grid"):
            # Current Weather Container
            with Container(classes="box-two-row"):
                yield Static(f"{self.weather_obj.weather["latitude"]}")

            # Image Container
            with Container(classes="box-two-row"):
                yield ImageWidget("images/winter-images/1.jpg", (30, 30))

            # Forecast Container
            with Container(classes="box-two-col"):
                yield Static("Daily Forecast Box")

    def on_mount(self):
        pass
