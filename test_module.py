import time
import TI.GPIO as GPIO

SER = 37
SRCLK = 38
RCLK = 40

GPIO.setmode(GPIO.BOARD)
GPIO.setup(SER, GPIO.OUT)
GPIO.setup(SRCLK, GPIO.OUT)
GPIO.setup(RCLK, GPIO.OUT)


def shift_out(byte):
    """ Shift out 8-bit data to the 74HC595 shift register """
    GPIO.output(RCLK, GPIO.LOW)
    for i in range(8):
        GPIO.output(SRCLK, GPIO.LOW)
        GPIO.output(SER, (byte >> (7 - i)) & 1)
        GPIO.output(SRCLK, GPIO.HIGH)
    GPIO.output(RCLK, GPIO.HIGH)


def test_all_segments():
    shift_out(0b11111111)
    time.sleep(5)
    shift_out(0b00000000)

try:
    test_all_segments()
finally:
    GPIO.cleanup()
