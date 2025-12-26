def give_advice(weather):
    """
    Receives a weather dictionary from get_weather()
    Returns a string with advice based on temperature and condition.
    """
    temp = weather["temperature"]
    condition = weather["condition"].lower()

    if "rain" in condition or "storm" in condition:
        return "⚠️ Advice: Carry an umbrella or stay safe indoors."
    elif temp > 35:
        return "🔥 Advice: Stay hydrated and avoid going out at noon."
    elif temp < 15:
        return "❄️ Advice: Wear warm clothes."
    else:
        return "✅ Advice: Weather looks good today."
