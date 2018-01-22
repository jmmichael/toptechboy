from time import sleep  # Library will let us put in delays
import RPi.GPIO as GPIO # Import the RPi Library for GPIO pin control
GPIO.setmode(GPIO.BOARD)# We want to use the physical pin number scheme
button1=16              # Give intuitive names to our pins
button2=12
LED1=22
LED2=18
GPIO.setup(button1,GPIO.IN,pull_up_down=GPIO.PUD_UP)  # Button 1 is an input, and activate pullup resisrot
GPIO.setup(button2,GPIO.IN,pull_up_down=GPIO.PUD_UP)  # Button 2 is an input, and activate pullup resistor
GPIO.setup(LED1,GPIO.OUT) # LED1 will be an output pin
GPIO.setup(LED2,GPIO.OUT) # LED2 will be an output pin
pwm1=GPIO.PWM(LED1,1000)  # We need to activate PWM on LED1 so we can dim, use 1000 Hz 
pwm2=GPIO.PWM(LED2,1000)  # We need to activate PWM on LED2 so we can dim, use 1000 Hz
pwm1.start(0)              # Start PWM at 0% duty cycle (off)             
pwm2.start(0)              # Start PWM at 0% duty cycle (off)
bright=1                   # Set initial brightness to 1%
try:
    while True:                  # Loop Forever
		if GPIO.input(button1)==0:             #If left button is pressed
			print "Button 1 was Pressed"   # Notify User
			bright=bright/2.               # Set brightness to half
			pwm1.ChangeDutyCycle(bright)   # Apply new brightness
			pwm2.ChangeDutyCycle(bright)   # Apply new brightness
			sleep(.25)                     # Briefly Pause
			print "New Brightness is: ",bright # Notify User of Brightness
		if GPIO.input(button2)==0:             # If button 2 is pressed
			print "Button 2 was Pressed"   # Notify User
			bright=bright*2                # Double Brightness
			if bright>100:                 # Keep Brightness at or below 100%
				bright=100
				print "You are at Full Bright"
			pwm1.ChangeDutyCycle(bright)  # Apply new brightness
			pwm2.ChangeDutyCycle(bright)  # Apply new brightness
			sleep(.25)                    # Pause
			print "New Brightness is: ",bright #Notify User of Brightness
except KeyboardInterrupt:
    GPIO.cleanup()
