import requests

api_key = "3f74d0913594e78ed558deb43849ed2a"

print("Welcome to the Weather App!")

user_input = input("Enter a city name: ")

url = f"http://api.openweathermap.org/data/2.5/weather?q={user_input}&units=metric&appid={api_key}"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    city = data["name"]
    country = data["sys"]["country"]
    temperature = data["main"]["temp"] 
    weather_description = data["weather"][0]["description"]

    print(f"City: {city}, Country: {country}")
    print(f"Temperature: {temperature}°C")
    print(f"Weather: {weather_description.capitalize()}")
else:
    print("City not found. Please check the name and try again.")