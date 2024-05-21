import os
os.system("pip install WeatherPlug")
import WeatherPlug

City = input("Enter a city: ")
WeatherPlug(City)

print(WeatherPlug.temp)
print(WeatherPlug.wind)
