#!/usr/bin/python
import httplib, urllib
import json
deviceId = "DpwJPYEJ"
deviceKey = "1mOUe8ZVclT0CimZ"
def post_to_mcs(payload):  
    headers = {"Content-type": "application/json", "deviceKey": deviceKey}
    not_connected = 1
    while (not_connected):
        try:
            conn = httplib.HTTPConnection("api.mediatek.com:80")
            conn.connect()
            not_connected = 0
        except (httplib.HTTPException, socket.error) as ex:
            print "Error: %s" % ex
            time.sleep(10)  # sleep 10 seconds
	conn.request("POST", "/mcs/v2/devices/" + deviceId + "/datapoints", 
json.dumps(payload), headers) 
	response = conn.getresponse() 
	print( response.status, response.reason, json.dumps(payload), time.strftime("%c")) 
	data = response.read() 
	conn.close() 

import time, RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)GPIO.setup(14, GPIO.IN, pull_up_down = GPIO.PUD_UP)
while True:
	sw = GPIO.input(14)
	payload = {"datapoints":[{"dataChnId":"sw1","values":{"value":sw}}]}
	if(sw == 0):
		print('button released')
   	else:
		print('Button prassed')
