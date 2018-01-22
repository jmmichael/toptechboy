#based on toptechboy 31
from time import sleep  # Library will let us put in delays
import RPi.GPIO as GPIO # Import the RPi Library for GPIO pin control
GPIO.setmode(GPIO.BOARD)# We want to use the physical pin number scheme
button1=36              # was 16Give intuitive names to our pins
button2=38              #was 12
motor1=22
motor2=18
GPIO.setup(button1,GPIO.IN,pull_up_down=GPIO.PUD_UP)  # Button 1 is an input, and activate pullup resisrot
GPIO.setup(button2,GPIO.IN,pull_up_down=GPIO.PUD_UP)  # Button 2 is an input, and activate pullup resistor
GPIO.setup(motor1,GPIO.OUT) # motor1 will be an output pin
GPIO.setup(motor2,GPIO.OUT) # motor2 will be an output pin
pwm1=GPIO.PWM(motor1,1000)  # We need to activate PWM on motor1 so we can dim, use 1000 Hz 
pwm2=GPIO.PWM(motor2,1000)  # We need to activate PWM on motor2 so we can dim, use 1000 Hz
pwm1.start(0)              # Start PWM at 0% duty cycle (off)             
pwm2.start(0)              # Start PWM at 0% duty cycle (off)
speed1=1                   # Set initial brightness to 1%
speed2=49
try:
    while True:                  # Loop Forever
		if GPIO.input(button1)==0:             #If left button is pressed
			print "Button 1 was Pressed"   # Notify User
			speed1=speed1/1.1               # Set brightness to half
			pwm1.ChangeDutyCycle(speed1)   # Apply new speed
			sleep(.25)                     # Briefly Pause
			print "New speed1 is: ",speed # Notify User of speed
		if GPIO.input(button2)==0:             # If button 2 is pressed
			print "Button 2 was Pressed"   # Notify User
			speed=speed2/1.1 
			if speed>100:                 # Keep speed at or below 100%
				speed=100
				print "You are at Full speed"
			pwm2.ChangeDutyCycle(speed2)  # Apply new speed
			sleep(.25)                    # Pause
			print "New speedness1 is: ",speed1 #Notify User of speed
except KeyboardInterrupt:
    GPIO.cleanup()
