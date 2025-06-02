from textual.app import App
from textual.widgets import Static
from src.weather.get_weather import get_weather


class WeatherDashboard(App):
    def compose(self):
        weather_data = get_weather().json()
        yield Static("Hello, Textual!")
        yield Static(f"{weather_data["latitude"]}")


if __name__ == "__main__":
    app = WeatherDashboard()
    app.run()
