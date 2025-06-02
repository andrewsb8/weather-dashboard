from textual.app import App
from textual.widgets import Static

class WeatherDashboard(App):
    def compose(self):
        yield Static("Hello, Textual!")

if __name__ == "__main__":
    app = WeatherDashboard()
    app.run()
