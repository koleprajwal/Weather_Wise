import smtplib
from email.message import EmailMessage

EMAIL_ADDRESS = "Enter Email ID From Which You Want To Send Alerts"
EMAIL_PASSWORD = "Enter Email Password or App Password Here"  

def send_email_alert(weather):
    """
    Sends an email alert if extreme weather is detected.
    """
    city = weather['city']
    temp = weather['temperature']
    condition = weather['condition']

    alerts = []
    if temp > 35:
        alerts.append("High temperature! Stay hydrated.")
    if temp < 10:
        alerts.append("Very cold! Wear warm clothes.")
    if "rain" in condition.lower() or "storm" in condition.lower():
        alerts.append("Rain/storm detected! Carry umbrella/safety precautions.")

    if not alerts:
        return

    subject = f"WeatherWise Alert for {city}"
    body = f"City: {city}\nTemperature: {temp}°C\nCondition: {condition}\n\n" + "\n".join(alerts)

    msg = EmailMessage()
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = 'Eneter Recipient Email ID Here'
    msg.set_content(body)

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)
        print("📧 Alert email sent!")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")
