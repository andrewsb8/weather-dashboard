import sys

from PyQt5.QtWidgets import QApplication

from src.config.config import Config
from src.dashboard.dashboard import WeatherDashboard

if __name__ == "__main__":
    config = Config()

    try:
        app = QApplication(sys.argv)
        dashboard = WeatherDashboard(config=config)
        dashboard.show()
        config.log.info("-- Dashboard Generation Successful --")
        sys.exit(app.exec_())
    except Exception:
        config.log.exception("FATAL ERROR. SEE STACK TRACE BELOW:")
