import sys
from src.config.config import Config
from PyQt5.QtWidgets import QApplication
from src.dashboard.dashboard import WeatherDashboard


if __name__ == "__main__":
    config = Config()

    app = QApplication(sys.argv)
    dashboard = WeatherDashboard(config=config)
    dashboard.show()
    sys.exit(app.exec_())
