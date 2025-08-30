# from django.shortcuts import render

# Create your views here.
import requests
from django.shortcuts import render

import requests
from django.shortcuts import render

def index(request):
    weather_data = None
    if 'city' in request.GET:
        city = request.GET['city']
        api_key = "cc63e13554571fd08c1afd40616b7f9d"  # Replace with your OpenWeatherMap API key
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url).json()

        if response.get("cod") == 200:
            weather_data = {
                "city": response["name"],
                "temperature": response["main"]["temp"],
                "description": response["weather"][0]["description"].title(),
                "icon": response["weather"][0]["icon"],
            }
        else:
            weather_data = {"error": "City not found!"}
    return render(request, 'weather/index.html', {"weather": weather_data})

