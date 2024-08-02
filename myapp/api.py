import requests

def get_weather(city):
    API_KEY = '8223c74832cc2f6df12c07eb034e0390'  # Replace with your actual API key
    url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }
    response = requests.get(url, params=params)
    
    if response.status_code != 200:
        raise Exception(f"API Error: {response.json().get('message', 'Unknown error')}")
    
    return response.json()
