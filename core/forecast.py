# core/forecast.py
import requests
import datetime

API_KEY = "Enter Your OpenWeatherMap API Key Here"

def get_forecast(city):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric"
    r = requests.get(url)
    data = r.json()

    if data.get("cod") != "200":
        return None

    forecast_data = []
    for item in data["list"]:
        time_txt = item["dt_txt"]
        if "12:00:00" in time_txt:
            date = datetime.datetime.strptime(time_txt, "%Y-%m-%d %H:%M:%S").date()
            temp = item["main"]["temp"]
            cond = item["weather"][0]["description"].title()
            forecast_data.append({"date": date, "temp": temp, "condition": cond})

    return forecast_data[:5]
