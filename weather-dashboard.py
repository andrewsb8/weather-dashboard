import sys
from PyQt5.QtWidgets import QApplication
from src.dashboard.dashboard import WeatherDashboard


if __name__ == "__main__":
    testkw = False
    if len(sys.argv) > 2:
        print("Too many arguments. Exiting.")
        exit(1)
    elif len(sys.argv) == 2 and sys.argv[-1] == "test":
        testkw = True

    app = QApplication(sys.argv)
    dashboard = WeatherDashboard()
    dashboard.show()
    sys.exit(app.exec_())
