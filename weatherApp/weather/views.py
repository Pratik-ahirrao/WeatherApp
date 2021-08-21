from django.shortcuts import render
import requests


# Create your views here.

def home(req):

    city = req.GET.get('city', "Bhusawal")

    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=9988780e24bfb7d925eeeb76f36be422'
    data = requests.get(url).json()
    payload = {
        'city': data['name'],
        'weather': data['weather'][0]['main'],
        'icon': data['weather'][0]['icon'],
        'kelvin_temperature': data['main']['temp'],
        'celcius_temperature': int(data['main']['temp'] - 273),
        'pressure': data['main']['pressure'],
        'humidity': data['main']['humidity'],
        'country': data['sys']['country'],
        'description': data['weather'][0]['description']
    }
    context = {'data': payload}
    print(context)
    return render(req, 'home.html', context)
