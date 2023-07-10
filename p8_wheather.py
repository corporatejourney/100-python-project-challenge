import requests
import json

class WeatherApp:
    """
    A simple weather application that fetches weather information using the OpenWeatherMap API.
    """

    def __init__(self, api_key):
        """
        Initializes the WeatherApp object with the provided API key.

        Args:
            api_key (str): The API key obtained from OpenWeatherMap.
        """
        self.api_key = api_key
        self.base_url = "https://api.openweathermap.org/data/2.5/weather?"

    def get_weather(self, city):
        """
        Fetches weather information for the specified city.

        Args:
            city (str): The name of the city for which weather information is to be fetched.

        Returns:
            dict: A dictionary containing the weather information.
        """
        url = self.base_url + f"q={city}&appid={self.api_key}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()

            weather_info = {
                "city": city,
                "main_weather": data["weather"][0]["main"],
                "description": data["weather"][0]["description"],
                "temperature": data["main"]["temp"],
                "humidity": data["main"]["humidity"]
            }

            return weather_info
        else:
            return None


# Usage example
api_key = "YOUR_API_KEY"  # Replace with your OpenWeatherMap API key

# Create a WeatherApp instance
weather_app = WeatherApp(api_key)

# Prompt the user for a city name
city_name = input("Enter city name: ")

# Get the weather information for the specified city
weather_info = weather_app.get_weather(city_name)

# Display the weather information
if weather_info:
    print(f"Weather in {weather_info['city']}:")
    print(f"Main weather: {weather_info['main_weather']}")
    print(f"Description: {weather_info['description']}")
    print(f"Temperature: {weather_info['temperature']} K")
    print(f"Humidity: {weather_info['humidity']}%")
else:
    print("Error occurred while retrieving weather data.")
