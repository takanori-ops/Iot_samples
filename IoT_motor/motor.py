import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
gp_out = 2
GPIO.setup(gp_out,GPIO.OUT)

motor = GPIO.PWM(gp_out,50)
motor.start(1.0)

try:	
	for i in range(2,13):
		print("start {}".format(i))
		motor.ChangeDutyCycle(i)
		time.sleep(1)
except:
	print("failed")
finally:
	GPIO.cleanup()
