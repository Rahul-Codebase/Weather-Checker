import requests

def get_weather(city):
    # Using wttr.in to get weather info for the city
    url = f'https://wttr.in/{city}?format=%C+%t+%w+%p'
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text.strip()  # Remove extra whitespace
        else:
            return "Sorry, could not fetch weather data at this time."
    except Exception as e:
        return f"An error occurred: {e}"

def main():
    city = input("Enter the city name: ")
    weather_info = get_weather(city)
    print(f"Weather info for {city}: {weather_info}")

if __name__ == "__main__":
    main()
