# CIS-CAPSTONE
Weather Data Retrieval
This Python script retrieves weather data for a specified city using the OpenWeatherMap API and stores it in a SQLite database.

Requirements
Python 3.x
requests library
SQLite3
Setup
OpenWeatherMap API Key: Obtain an API key from OpenWeatherMap and set it as an environment variable named API_KEY_CIS_CAPSTONE.
Python Libraries: Install the required Python libraries using pip:
bash
Copy code
pip install requests
SQLite Database: The script creates a SQLite database named weather_data.db in the current directory to store weather data.
Usage
Run the Script: Execute the Python script in your terminal or command prompt:
bash
Copy code
python weather_data_retrieval.py
Input City: Enter the name of the city for which you want to retrieve weather data when prompted.
View Results: The script retrieves weather data for the specified city from the OpenWeatherMap API, displays the weather description and temperature in Fahrenheit, and stores the data in the SQLite database.
Notes
If the city name includes a country, separate it with a comma (e.g., "London, UK").
Weather data is retrieved using the get_weather() function, which queries the OpenWeatherMap API.
Retrieved data is stored in the weather_data.db SQLite database in a table named weather_data.

