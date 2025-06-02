from textual.app import App
from textual.widgets import Static
from src.weather.get_weather import get_weather
from src.image_widget.image_widget import ImageWidget

class WeatherDashboard(App):
    def __init__(self, testkw=False):
        self.testkw = testkw
        super().__init__()

    def compose(self):
        weather_data = get_weather(testkw=self.testkw)
        yield Static("Hello, Textual!")
        yield Static(f"{weather_data["latitude"]}")
        yield ImageWidget("path/to/your/image.png")
