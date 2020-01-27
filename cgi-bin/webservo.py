#!/usr/bin/env python

import cgi
import cgitb    #display CGI error on browser
import time
import RPi.GPIO as GPIO


print('Content-type: text/html; charset=UTF-8\r\n')
print('<link href="../css/style.css" rel="stylesheet" type="text/css">')
print('Web SERVO')

print('<form action="" method="post">')
print('<input type="number" name="num" min="-90" max="90">')
print('<input type="submit" name="sub" value="soushin">')
print('</form>')

form = cgi.FieldStorage()
value = form.getvalue("sub")

bottom = 2.5
middle = 7.2
top = 12.0

def setservo(dig):
    angle = (top - bottom) * (90 + dig) / 180 + bottom
    servo.ChangeDutyCycle(angle)
    time.sleep(1.0)

if value == "soushin":
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(2, GPIO.OUT)
    servo = GPIO.PWM(2, 50)
    servo.start(0.0)
    setservo(int(form.getvalue("num")))
