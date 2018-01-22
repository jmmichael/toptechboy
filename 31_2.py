from time import sleep  # Library will let us put in delays
import RPi.GPIO as GPIO # Import the RPi Library for GPIO pin control
GPIO.setmode(GPIO.BOARD)# We want to use the physical pin number scheme
button1=36              # was 16Give intuitive names to our pins
button2=38              #was 12
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
bright1=1                   # Set initial brightness to 1%
bright2=49
try:
    while True:                  # Loop Forever
		if GPIO.input(button1)==0:             #If left button is pressed
			print "Button 1 was Pressed"   # Notify User
			bright1=bright1/1.1               # Set brightness to half
			bright2=bright2*1.1
			pwm1.ChangeDutyCycle(bright1)   # Apply new brightness
			pwm2.ChangeDutyCycle(bright2)   # Apply new brightnesshalf
			pwm1.ChangeDutyCycle(bright1)   # Apply new brightness
			pwm2.ChangeDutyCycle(bright2)   # Apply new brightness
			sleep(.25)                     # Briefly Pause
			print "New Brightness1 is: ",bright1 # Notify User of Brightness
			print "New Brightness2 is: ",bright2
		if GPIO.input(button2)==0:             # If button 2 is pressed
			print "Button 2 was Pressed"   # Notify User
			bright=bright1*1.1                # Double Brightness
			bright=bright2/1.1 
			if bright>100:                 # Keep Brightness at or below 100%
				bright=100
				print "You are at Full Bright"
			pwm1.ChangeDutyCycle(bright1)  # Apply new brightness
			pwm2.ChangeDutyCycle(bright2)  # Apply new brightness
			sleep(.25)                    # Pause
			print "New Brightness1 is: ",bright1 #Notify User of Brightness			
			print "New Brightness2 is: ",bright2 #Notify User of Brightness
except KeyboardInterrupt:
    GPIO.cleanup()
