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

def setservo(dig):
    angle = (12.0 - 2.5) * (90 + dig) / 180 + 2.5
    servo.ChangeDutyCycle(angle)
    time.sleep(1.0)


def main():
    form = cgi.FieldStorage()
    value = form.getvalue("sub")

    if value == "soushin":
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(2, GPIO.OUT)
        servo = GPIO.PWM(2, 50)
        servo.start(0.0)
        setservo(int(form.getvalue("num")))

if __name__ == "__main__":
    main()
