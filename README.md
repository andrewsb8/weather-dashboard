# Weather Dashboard

This project is a small weather dashboard made using python and the following tools:

- PyQt5 for GUI
- Open Meteo for weather API: https://open-meteo.com/

# General Usage

To see available options, use: ```python weather-dashboard.py -h```

You can set various settings such as update frequency and screen size. You can also take a screenshot of the dashboard instead of continuously updating a desktop application window (will be relevant below).

# Adding Images

In ```images/``` there are directories to add custom weather-specific images and examples for each category are provided. The application will pick one of the images based on weather conditions and the season at each update.

# Setup on Raspberry Pi Zero 2 W and E-Ink Screen

## Hardware Setup

I followed this tutorial mostly, but wanted to make the software myself: https://www.youtube.com/watch?v=65sda565l9Y.

The hardware:
- Raspberry Pi Zero 2 W
- 7.3" Inky Impression E-ink Display
- Ikea RÖDALM Frame

## Software Setup

The setup here for an e-ink screen is a little unexpected. Since the display cannot display a live desktop, I cannot use the interval update feature of PyQt. Instead, I take a screenshot of the application after rendering and display that image. The screen is updated using another script which is executed by crontab for desired interval updates. I do hourly to be nice to the weather API provider.

- Setup Raspberry Pi
- Follow instructions to set up E-ink display (see installing software): https://learn.pimoroni.com/article/getting-started-with-inky-impression
- Clone repo
- make directory ```weather-dashboard-img```
- make directory ```inky_scripts``` which should contain the following scripts:

```update_inky_screen.py```:

```
from inky.auto import auto
from PIL import Image
import time

inky = auto()

img = Image.open("/home/weather-pi/weather-dashboard-img/weather-dashboard.png")
img = img.resize((800,480))
inky.set_image(img)
inky.show()
```

```inky_script.sh```

```
#!/bin/bash

cd
cd /home/weather-pi/weather-dashboard
# ensure pyqt can run in headless env
export QT_QPA_PLATFORM=offscreen
# make dashboard
python weather-dashboard.py --screenshot -p /home/weather-pi/weather-dashboard-img/weather-dashboard.png -s 1280 768


cd /home/weather-pi/inky_script/
source ~/.virtualenvs/pimoroni/bin/activate
python update_inky_screen.py
```

Then add the following line to crontab to run update hourly:

```0 * * * * bash /home/weather-pi/inky_script/inky_script.sh```

You may have to run the following command to get the dashboard python script to run without an external (not e-ink) display connected to the pi:

```export QT_QPA_PLATFORM=offscreen```
