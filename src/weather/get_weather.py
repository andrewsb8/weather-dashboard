from requests import get

def get_weather():
    """
    Retrieve weather data from open-meteo API: https://open-meteo.com/

    """
    return get('https://api.open-meteo.com/v1/forecast?latitude=39.92026&longitude=-75.15935&daily=weather_code,temperature_2m_max,temperature_2m_min,sunrise,sunset,uv_index_max,precipitation_probability_max,precipitation_sum,precipitation_hours&current=temperature_2m,relative_humidity_2m,apparent_temperature,is_day,wind_speed_10m,wind_direction_10m,precipitation,rain,snowfall,weather_code,cloud_cover&timezone=America%2FNew_York&wind_speed_unit=mph&temperature_unit=fahrenheit&precipitation_unit=inch')
