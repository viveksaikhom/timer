import time
import TI.GPIO as GPIO

SER = 37
SRCLK = 38
RCLK = 40

GPIO.setmode(GPIO.BOARD)
GPIO.setup(SER, GPIO.OUT)
GPIO.setup(SRCLK, GPIO.OUT)
GPIO.setup(RCLK, GPIO.OUT)

try:
    while True:
        print("Toggling pins...")
        GPIO.output(SER, GPIO.HIGH)
        GPIO.output(SRCLK, GPIO.HIGH)
        GPIO.output(RCLK, GPIO.HIGH)
        time.sleep(0.5)

        GPIO.output(SER, GPIO.LOW)
        GPIO.output(SRCLK, GPIO.LOW)
        GPIO.output(RCLK, GPIO.LOW)
        time.sleep(0.5)

finally:
    GPIO.cleanup()
