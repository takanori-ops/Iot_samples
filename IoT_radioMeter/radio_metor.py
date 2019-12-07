import time
import RPi.GPIO as GPIO


def reading(sensor):
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BOARD)
	
	TRIG = 11
	ECHO = 13
	
	if sensor == 0:
		GPIO.setup(TRIG,GPIO.OUT)
		GPIO.setup(ECHO,GPIO.IN)
		GPIO.output(TRIG,GPIO.LOW)
		
		time.sleep(0.3)
		
		GPIO.output(TRIG,True)
		time.sleep(0.00001)
		GPIO.output(TRIG,False)
		
		while GPIO.input(ECHO) == 0:
			signaloff = time.time()
	
		while GPIO.input(ECHO) == 1:
			signalon= time.time()
		
		timepassed = signalon - signaloff
		distance = timepassed * 17000
		
		GPIO.cleanup()
		return distance
		
	else:
		print("incorrect ")

while True:
	dist = reading(0)
	if dist < 100:
		print(dist)
	else:
		break
		
		
