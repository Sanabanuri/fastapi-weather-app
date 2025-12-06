from fastapi import FastAPI
import requests

api_key = 'f4b18b49daf6014cde248ed790441a28'
#city = "karachi"

app = FastAPI()

@app.get("/weather/{city}")
def get_weather(city:str):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)
    data = response.json()

    return {
         "city": data["name"],
         "Temprature": data["main"]["temp"],
         "Weather": data["weather"][0]["description"]
         }

