from __future__ import print_function
import requests
import json
from picamera import PiCamera
from time import sleep
import os

def load_binary(file):
    with open(file, 'rb') as file:
        return file.read()

def main():

    addr = 'http://192.168.1.22:5000'
    test_url = addr + '/faces'

    # prepare headers for http request
    content_type = 'image/jpeg'
    headers = {'content-type': content_type}



    camera = PiCamera()
    camera.start_preview()

    numPics = 0
    while numPics < 10:
        sleep(2)
        picLocation = '/home/pi/pics/image%s.jpg' % numPics
        camera.capture(picLocation)
        img = load_binary(picLocation)
        # encode image as jpeg
        # send http request with image and receive response
        response = requests.post(test_url, data=img, headers=headers)
        os.remove(picLocation)
        numPics += 1
    camera.stop_preview()

if __name__ == '__main__':
    main()