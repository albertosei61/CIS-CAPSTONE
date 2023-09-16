import requests 


API_KEY = "7cc83b9244dad40033542988850119a3"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temperature = round(data["main"]["temp"] * 9/5 - 457.87, 2)

    print("Weather:", weather)
    print("Temperature:", temperature, "Fahrenheit")

    
else:
    print("An error occured.")