# 10. Weather Forecast (Requires 'requests')

def get_weather(city):
    import requests
    api_key = "d0a678fbc52a6ccd3656db0696979a80"  # Replace with your actual OpenWeatherMap API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(f"Weather in {city}: {data['weather'][0]['description']}, {data['main']['temp']}°C")
    else:
        print("City not found!")

city = input("Enter city name for weather forecast: ")
get_weather(city)
