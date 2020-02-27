import requests
import settings

def getLocalCoordinates(myip):
    ipstack_url = 'http://api.ipstack.com/{}'.format(myip)
    params = dict(
        access_key = settings.ipstack_API_KEY,
        format = 1,
        fields = 'latitude,longitude'
    )
    coordinates = requests.get(url=ipstack_url, params=params).json()
    return {"longitude": coordinates['longitude'], "latitude": coordinates['latitude']}