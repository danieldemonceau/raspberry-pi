from picamera import PiCamera
from time import sleep
from subprocess import call
from pathlib import Path
import datetime
import sched, time

camera = PiCamera()

now = datetime.datetime.now()

day = str(now.day).zfill(2)
month = str(now.month).zfill(2)
year = str(now.year).zfill(4)

yearmonthday = '{}{}{}'.format(str(year), str(month), str(day))

path = '/home/pi/software/day/{}/'.format(yearmonthday)

Path(path).mkdir(parents=True, exist_ok=True)

camera.start_preview()

s = sched.scheduler(time.time, time.sleep)
def take_picture(sc):
    now = datetime.datetime.now()
    hour = str(now.hour).zfill(2)
    minute = str(now.minute).zfill(2)
    second = str(now.second).zfill(2)
    hourminutesecond = '{}{}{}'.format(str(hour), str(minute), str(second))
    camera.capture(path + hourminutesecond + '.jpg')
    s.enter(15, 1, take_picture, (sc,))

s.enter(15, 1, take_picture, (s,))
s.run()
camera.stop_preview()
