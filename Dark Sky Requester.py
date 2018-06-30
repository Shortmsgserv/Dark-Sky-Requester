from forecastiopy import *
from geopy.geocoders import Nominatim

import config
import certifi
import ssl
import geopy.geocoders
ctx = ssl.create_default_context(cafile=certifi.where())
geopy.geocoders.options.default_ssl_context = ctx
geolocator = Nominatim()
geolocator.scheme = 'http'
apikey = config.apikey

userEnteredLocation = input('Please enter a location: ')
location = geolocator.geocode(userEnteredLocation)
print(location.address)
print ("Nominatim's Coordinates: ", location.latitude, location.longitude)

returnedLocation = [location.latitude, location.longitude]
fio = ForecastIO.ForecastIO(apikey, units = ForecastIO.ForecastIO.UNITS_SI, lang = ForecastIO.ForecastIO.LANG_ENGLISH, latitude = returnedLocation[0], longitude = returnedLocation[1])
print("Dark Sky's Data: ")
print('latitude', fio.latitude, 'Longitude', fio.longitude)
print('Timezone', fio.timezone, 'Offset', fio.offset)
print(fio.get_url())
print(location.address)

currently = FIOCurrently.FIOCurrently(fio)
print("The Temperature in ", userEnteredLocation, "is", currently.temperature)
userEnteredTimeframe = input("What timeframe do you want to know, minutely, hourly, daily: ")
#userEnteredTimeframe = str.lower(userEnteredTimeframe)

minutely = FIOMinutely.FIOMinutely(fio)
hourly = FIOHourly.FIOHourly(fio)
daily = FIODaily.FIODaily(fio)

if userEnteredTimeframe == "minutely":
	print(minutely.summary)
if userEnteredTimeframe == "hourly":
	print(hourly.summary)
if userEnteredTimeframe == "daily":
	print(daily.summary)
else:
	print("I'm not sure what you typed.")
	

