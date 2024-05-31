import requests

def get_weather(api_key,city,lang="tr"):
    url=f"https://api.collectapi.com/weather/getWeather?data.lang={lang}&data.city={city}"
    headers = {
    'content-type': "application/json",
    'authorization': api_key
    }

    a=requests.get(url,headers=headers)
    data=a.json() 
    
    return data.get("result",[])

def display_weather_forecast(weather_data):
    for day_info in weather_data:
        print("Date: ",day_info['date'])
        print(f"Temperature: {day_info['degree']}°C")
        print(f"Status: {day_info['status']}")
        print(f"Description: {day_info['description']}")

api_key="2lQnemPqccKJty5BOlW8TI:2T8iXCjryiVM6nbwZb9a4z"
print()
city=input("Şehir adını girin: ")
weather_data=get_weather(api_key,city)
if weather_data:
    display_weather_forecast(weather_data)
else:
    print("Hata")