from picamera import PiCamera
from time import sleep
from subprocess import call
from pathlib import Path
import sched, time
import sys
import platform
import requests
import json
from settings import *
import ip
from datetime import datetime

camera = PiCamera()

now = datetime.now()

day = str(now.day).zfill(2)
month = str(now.month).zfill(2)
year = str(now.year).zfill(4)

yearmonthday = '{}{}{}'.format(str(year), str(month), str(day))

## Handle the folder that will store the individual pictures
folder_location = ''
if len(sys.argv) == 0:
    if platform.system() = 'Windows':
        folder_location_root_windows = 'C:/PERSO/raspberry/day/'
        if not os.path.isdir(folder_location_root_windows):
            folder_location = '/day/{}/'.format(yearmonthday)'
        else:
            folder_location = os.path.join(folder_location_root_windows, '{}/'.format(yearmonthday))
    if platform.system() = 'Linux':
        folder_location_root_linux = '/home/pi/software/day/'
        if not os.path.isdir(folder_location_root_linux):
            folder_location = '/day/{}/'.format(yearmonthday)'
        else:
            folder_location = os.path.join(folder_location_root_linux, '{}/'.format(yearmonthday))
else:
    folder_location = sys.argv[1] + '/day/{}/'.format(yearmonthday)'

Path(folder_location).mkdir(parents=True, exist_ok=True)

myip = ip.getIP()
mylocation = location.getLocalCoordinates(myip)
sunriseSunsetTimes = sun.getSunriseTime(myLocation)
sunriseTime = sunriseSunsetTimes['civil_twilight_begin']
sunsetTime = sunriseSunsetTimes.['civil_twilight_end']

now_utc = datetime.utcnow()

if now_utc > sunriseTime and now_utc > sunsetTime:
    camera.start_preview()

    s = sched.scheduler(time.time, time.sleep)
    def take_picture(sc):
        now = datetime.now()
        hour = str(now.hour).zfill(2)
        minute = str(now.minute).zfill(2)
        second = str(now.second).zfill(2)
        hourminutesecond = '{}{}{}'.format(str(hour), str(minute), str(second))
        camera.capture(folder_location + hourminutesecond + '.jpg')
        s.enter(15, 1, take_picture, (sc,))

    s.enter(15, 1, take_picture, (s,))
    s.run()
    camera.stop_preview()
