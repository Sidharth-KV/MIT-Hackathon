import requests
import Location
# Your API Key from IQAir
API_KEY = "28ee0285-e57c-47bd-bc0e-74a3ebb3a638"

# Location
lat, long, city, state, country = Location.locationCoordinates()

if(country == "IN"):
    country = "India"
else if(country != "IN"):
    print("Not supported")

print(lat, long, city, state, country)

# IQAir API URL
url = f"https://api.airvisual.com/v2/city?city={city}&state={state}&country={country}&key={API_KEY}"

# Fetch Data
response = requests.get(url)
def ret_AQI():
    if response.status_code == 200:
        data = response.json()
        
        # Extract AQI Data
        if "data" in data and "current" in data["data"]:
            aqi = data["data"]["current"]["pollution"]["aqius"]  # AQI in US standard
            return aqi
            print(aqi)
        else:
            print("No AQI data found.")
    else:
        print(f"Error {response.status_code}: {response.text}")
print(ret_AQI())