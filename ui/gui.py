import tkinter as tk
from tkinter import ttk, messagebox
from core.fetch_weather import get_weather
from core.advisor import give_advice
from core.alert import send_email_alert
from core.forecast import get_forecast

ICON_MAP = {
    "clear": "☀️",
    "cloud": "☁️",
    "rain": "🌧️",
    "storm": "⛈️",
    "snow": "❄️",
    "mist": "🌫️",
}

def weather_icon(condition):
    cond = condition.lower()
    for key, icon in ICON_MAP.items():
        if key in cond:
            return icon
    return "🌈"

def bg_color(temp):
    if temp < 10:
        return "#b3e5fc"   # cool blue
    elif temp > 35:
        return "#ffcc80"   # warm orange
    else:
        return "#c8e6c9"   # mild green

def run_gui():
    def show_weather():
        city = city_entry.get().strip()
        if not city:
            messagebox.showwarning("Warning", "Enter a city name!")
            return

        weather = get_weather(city)
        if not weather:
            messagebox.showerror("Error", "City not found or API error.")
            return

        temp = weather["temperature"]
        cond = weather["condition"]
        icon = weather_icon(cond)

        root.configure(bg=bg_color(temp))
        result_label.config(
            text=f"{icon}  {weather['city']}\n🌡️ {temp}°C | 💧 {weather['humidity']}%\n{cond.title()}",
            bg=bg_color(temp),
        )

        # Forecast
        forecast = get_forecast(city)
        for widget in forecast_frame.winfo_children():
            widget.destroy()

        if forecast:
            for day in forecast:
                icon_f = weather_icon(day["condition"])
                ttk.Label(
                    forecast_frame,
                    text=f"{day['date']}  {icon_f}  {day['temp']}°C  {day['condition']}",
                    font=("Segoe UI", 10),
                ).pack(anchor="w", pady=1)
        else:
            ttk.Label(forecast_frame, text="Forecast unavailable.").pack()

        # Advice + email
        advice = give_advice(weather)
        advice_label.config(text=f"✅ {advice}", bg=bg_color(temp))
        send_email_alert(weather)

    root = tk.Tk()
    root.title("WeatherWise: Smart Weather Advisor")
    root.geometry("430x550")
    root.resizable(False, False)
    root.configure(bg="#e0f7fa")

    ttk.Label(root, text="🌦️ WeatherWise", font=("Segoe UI", 18, "bold")).pack(pady=10)
    ttk.Label(root, text="Enter city:").pack(pady=5)

    city_entry = ttk.Entry(root, font=("Segoe UI", 12), width=25)
    city_entry.pack(pady=5)

    ttk.Button(root, text="Get Weather", command=show_weather).pack(pady=8)

    result_label = tk.Label(root, text="", font=("Segoe UI", 12), bg="#e0f7fa", justify="center")
    result_label.pack(pady=10)

    advice_label = tk.Label(root, text="", font=("Segoe UI", 11), bg="#e0f7fa")
    advice_label.pack(pady=5)

    ttk.Label(root, text="5-Day Forecast:", font=("Segoe UI", 12, "bold")).pack(pady=5)
    forecast_canvas = tk.Canvas(root, height=180, width=400)
    forecast_frame = ttk.Frame(forecast_canvas)
    scroll_y = ttk.Scrollbar(root, orient="vertical", command=forecast_canvas.yview)
    forecast_canvas.configure(yscrollcommand=scroll_y.set)
    forecast_canvas.create_window((0, 0), window=forecast_frame, anchor="nw")
    forecast_canvas.pack(pady=5)
    scroll_y.pack(side="right", fill="y")

    forecast_frame.bind("<Configure>", lambda e: forecast_canvas.configure(scrollregion=forecast_canvas.bbox("all")))

    root.mainloop()
