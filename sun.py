import requests

def getSunriseSunsetTimes(myLocation):
    sunrisesunset_API_url = 'https://api.sunrise-sunset.org/json'
    params = dict(
        lat = myLocation['latitude'],
        lng = myLocation['latitude']
    )
    sunriseSunsetTimes = requests.get(url=sunrisesunset_API_url, params=params).json()
    return {"civil_twilight_begin": datetime.strptime(sunriseSunsetTimes['results']['civil_twilight_begin'], '%I:%M:%S %p'), "civil_twilight_end": datetime.strptime(sunriseSunsetTimes['results']['civil_twilight_end'], '%I:%M:%S %p')}