import requests
from datetime import datetime

API_KEY = "da181b43da1a6eeac7e34727ce599d51"


def get_weather_description(place, target_date):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"

    response = requests.get(url)

    if response.status_code != 200:
        print(
            f"Error: Unable to fetch data for {place}. Status code: {response.status_code}")
        return None

    data = response.json()

    if "list" in data:
        for entry in data["list"]:
            forecast_date = datetime.fromtimestamp(entry["dt"])
            if forecast_date.date() == target_date.date():
                weather_description = entry["weather"][0]["main"]
                return weather_description

    return "No weather data available for the specified date."


if __name__ == "__main__":
    place = "Tokyo"
    target_date = datetime(2024, 10, 22)
    weather_description = get_weather_description(place, target_date)
    print(
        f"The weather in {place} on {target_date.date()} is: {weather_description}")
