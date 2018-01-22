from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
button1=16
button2=12
GPIO.setup(button1,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(button2,GPIO.IN,pull_up_down=GPIO.PUD_UP)
while True:
        if GPIO.input(button1)==0:
                print "Button 1 Pressed"
                sleep(.1)
        if  GPIO.input(button2)==0:
                sleep(.1)
                print "Button 2 Pressed"
