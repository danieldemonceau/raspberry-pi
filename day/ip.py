import requests

def getIP():
    return requests.get('https://api.ipify.org').text