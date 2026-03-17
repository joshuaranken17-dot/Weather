# weather.py

from meteostat import Point, Daily
from datetime import datetime, timedelta

def get_weather():
    location = Point(53.4808, -2.2426)

    # Use yesterday to guarantee data exists
    end = datetime.today()
    start = end - timedelta(days=2)

    data = Daily(location, start, end).fetch()

    # Check if data exists
    if data.empty:
        return {
            "date": "N/A",
            "tavg": "N/A",
            "tmin": "N/A",
            "tmax": "N/A",
            "prcp": "N/A"
        }

    # Get the most recent row safely
    latest = data.iloc[-1]

    def safe(val, unit):
        return f"{val:.1f} {unit}" if val is not None else "N/A"

    return {
        "date": latest.name.strftime("%Y-%m-%d"),
        "tavg": safe(latest.get("tavg"), "°C"),
        "tmin": safe(latest.get("tmin"), "°C"),
        "tmax": safe(latest.get("tmax"), "°C"),
        "prcp": safe(latest.get("prcp"), "mm")
    }