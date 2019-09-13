import serial
import time
from urllib.request import urlopen
import json
import nexmo
​
arduino = serial.Serial('/dev/cu.usbmodem141401')
time.sleep(2)
​
print("Enter 1 to turn ON LED and 0 to turn OFF LED")
​
while 1:

    datafromUser = input()
​
    if datafromUser == '1':
        arduino.write(b'1')
        response = urlopen('http://ipinfo.io/json')
        data = json.load(response)
        location = data["loc"]
        client = nexmo.Client(key='29cc211c', secret='U5W7sdHU8GqYK9M7')
        client.send_message({
            'from': 'Nexmo',
            'to': '256759678174',
            'text': f'https://www.google.com/maps/place/{location}'
        })
        print("LED  turned ON")
    elif datafromUser == '0':
        arduino.write(b'0')
        print("LED turned OFF")
