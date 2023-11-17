import requests
import sys
import sqlite3

#API key and base URL
API_KEY = "7cc83b9244dad40033542988850119a3"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city):
    request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
    response = requests.get(request_url)

    if response.status_code == 200:
        data = response.json()
        weather = data['weather'][0]['description']
        temperature = round(data["main"]["temp"] * 9/5 - 459.67, 2)  # Convert from Kelvin to Fahrenheit
        return weather, temperature
    else:
        return None, None

conn = sqlite3.connect("weather_data.db")
cursor = conn.cursor()


cursor.execute("""
    CREATE TABLE IF NOT EXISTS weather_data (
        city TEXT,
        weather TEXT,
        temperature REAL
    )
""")
conn.commit()


city = input("Enter a city name: ")

weather, temperature = get_weather(city)

if weather is not None and temperature is not None:
    # Insert data
    cursor.execute("INSERT INTO weather_data (city, weather, temperature) VALUES (?, ?, ?)", (city, weather, temperature))
    conn.commit()

    print("Weather:", weather)
    print("Temperature:", temperature, "Fahrenheit")

else:
    print("An error occurred.")

# Closing the database connection
conn.close()
