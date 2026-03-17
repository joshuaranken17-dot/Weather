# app.py

from flask import Flask, render_template
from weather import get_weather
import schedule
import threading
import time

app = Flask(__name__)

# Store latest weather
weather_report = get_weather()

# Function to update weather daily
def update_weather():
    global weather_report
    weather_report = get_weather()
    print("Weather updated:", weather_report)

# Background scheduler
def run_scheduler():
    schedule.every().day.at("07:00").do(update_weather)
    while True:
        schedule.run_pending()
        time.sleep(60)

# Start scheduler in background
threading.Thread(target=run_scheduler, daemon=True).start()

@app.route("/")
def home():
    return render_template("index.html", weather=weather_report)

if __name__ == "__main__":
    app.run(debug=True)