from textual.app import App
from textual.widgets import Static
from src.weather.get_weather import get_weather
from src.dashboard.image_widget import ImageWidget


class WeatherDashboard(App):
    CSS_PATH = "style.tcss"

    def __init__(self, testkw=False):
        self.testkw = testkw
        self.weather_data = get_weather(testkw=self.testkw)
        super().__init__()

    def compose(self):
        yield Static(f"{self.weather_data["latitude"]}", classes="box", id="two-row")
        yield ImageWidget("images/winter-images/1.jpg", (30, 30))
        yield Static("yeah whatever")
        yield Static("Daily Forecast Box", classes="box", id="two-column")

    def on_mount(self):
        pass
        # self.screen.styles.background = "white"
