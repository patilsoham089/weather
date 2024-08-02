from django.shortcuts import render
from .api import get_weather

def weather_view(request):
    weather_data = None
    error_message = None

    if 'city' in request.GET:
        city = request.GET['city'].strip()  # Strip any extra whitespace
        
        if city:  # Ensure the city is not empty
            try:
                weather_data = get_weather(city)
            except Exception as e:
                error_message = str(e)

    return render(request, 'weather.html', {'weather_data': weather_data, 'error_message': error_message})
