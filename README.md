# WeatherWise - Smart Weather Advisor

## Features
- Fetches live weather data for any city.
- Gives actionable advice based on temperature and condition.
- Sends email alerts for extreme weather.
- GUI interface with Tkinter for easy use.

## Setup
1. Install Python 3.10+.
2. Install requests: pip install requests
3. Replace YOUR_OPENWEATHERMAP_API_KEY and email credentials in core/alert.py and core/fetch_weather.py
4. Run GUI: python main.py

## Notes
- Email alerts require a dedicated Gmail + App Password.
- CLI mode is optional and can be activated by commenting out run_gui().
