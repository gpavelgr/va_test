from weather import Weather, Unit

weather = Weather(unit=Unit.CELSIUS)

lookup = weather.lookup_by_location("saint-petersburg")
condition = lookup.condition

for forecast in lookup.forecast:
    print(forecast.date)
    print(forecast.high, forecast.low)

#print(condition.text)
