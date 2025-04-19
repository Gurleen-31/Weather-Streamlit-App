import requests

def get_city_data(city_name):
    api_url = f"1f3f37d20eeae508e68697020648277f"  # Replace with the correct API URL
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an error for bad HTTP status codes
        city_data = response.json()
        return city_data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data for {city_name}: {e}")
        return None

city_name = input("Enter a city name: ")
city_data = get_city_data(city_name)

if city_data:
    print(f"City found: {city_data}")
else:
    print("City not found or API error.")
