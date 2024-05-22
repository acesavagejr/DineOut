def WP():
    import os
    from core import Core
    os.system("pip install WeatherPlug")
    os.system("clear")
    from WeatherPlug import WeatherPlug

    City = input("Enter a city: ")
    WeatherPlug(City)
    print(WeatherPlug.temp)
    print(WeatherPlug.wind)
    print(WeatherPlug.humidity)
    print(WeatherPlug.pressure)
    print(WeatherPlug.desc)
    print("  ")
    Core()
