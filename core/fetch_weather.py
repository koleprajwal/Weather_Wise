import requests

API_KEY = "Enter Your OpenWeatherMap API Key Here"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city_name):
    """
    Fetch current weather data for a given city.
    Returns a dictionary with temperature, humidity, and condition.
    """
    params = {
        "q": city_name,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if data.get("cod") != 200:
            return {"error": f"City not found or invalid response: {data.get('message')}"}

        main = data["main"]
        weather_desc = data["weather"][0]["description"]

        return {
            "city": data["name"],
            "temperature": main["temp"],
            "humidity": main["humidity"],
            "condition": weather_desc
        }

    except requests.exceptions.RequestException as e:
        return {"error": f"Network error: {e}"}
