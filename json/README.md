This folder contains json files which can be used to configure the weather dashboard. These files are read directly, should not be moved, but can either be added to or edited.

### weather_api_config.json

Contains the Open Meteo weather api link for the python requests package. For "convenience", the longitude and latitude fields are separated out for editing if you move. The weather api link has modified entries like ```[LAT]``` which are replaced by the latitude field. If the link put in the json file has numerical values for latitude and longitude, the separate fields for these values remain unused.

### special_dates.json

The point of this project was to make a simple weather dashboard for my partner with custom images they would like. I wanted to add some customization into it by adding images on important dates like birthdays and anniversaries. 

The ```special_dates.json``` file has dates as keys in the format ```date.strftime("%B %d")``` (Ex: ```"April 08"```). The year is omitted so that recurring dates don't require modifications! The value is then the path to whatever folder has the images for the occassion you want. This can be any folder you choose on your machine, not just the ones provided in ```images/```. However, the dashboard will still choose a random image from the directory. If you want the same image all the time, make sure the path leads to a directory with only one image in it. You can add as many dates as you want!
