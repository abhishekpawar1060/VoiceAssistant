import requests

key = "e1b1a8131b5bcf37ac92f8ee389c0036"
api_address = "http://api.openweathermap.org/data/2.5/weather?q=Aurangabad&appid="+key

json_data = requests.get(api_address).json()

def temp():
    temprature = round(json_data["main"]["temp"]-273,2)
    return temprature

def des():
    description = json_data["weather"][0]["description"]
    return description

# print(temp())
# print(des())