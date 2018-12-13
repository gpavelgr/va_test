

def get_weather_for_tomorrow(location:str)->dict:
    from weather import Weather, Unit
    weather = Weather(unit=Unit.CELSIUS)
    lookup = weather.lookup_by_location(location)
    f = lookup.forecast[1]
    return {"high": f.high, "low": f.low, "text": f.text, "date": f.date}



def get_weather_for_tomorrow_mock(location:str)->dict:
    if location == "saint-petersburg":
        return {"high": 10, "low": 7, "text": "Rainy", "date": "14 Dec 2018"}
    else:
        return {"high": -3, "low": -5, "text": "Cloudy", "date": "14 Dec 2018"}

if __name__ == "__main__":
    print(get_weather_for_tomorrow("saint-petersburg"))

