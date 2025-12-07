from fastapi import FastAPI
import requests


pi_key='f4b18b49daf6014cde248ed790441a28'
city = "karachi"

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
data = requests.get(url)

if data.status_code == 200:
    test = data.json()
    print(test)

else:
    print("no")

