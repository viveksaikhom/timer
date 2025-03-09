import time
import TI.GPIO as GPIO

SER = 37
SRCLK = 38
RCLK = 40


GPIO.setmode(GPIO.BOARD)
GPIO.setup(SER, GPIO.OUT)
GPIO.setup(SRCLK, GPIO.OUT)
GPIO.setup(RCLK, GPIO.OUT)


SEGMENTS = {
    '0': 0b00111111, '1': 0b00000110, '2': 0b01011011, '3': 0b01001111,
    '4': 0b01100110, '5': 0b01101101, '6': 0b01111101, '7': 0b00000111,
    '8': 0b01111111, '9': 0b01101111, '-': 0b01000000, ' ': 0b00000000,
}


def shift_out(byte):
    GPIO.output(RCLK, GPIO.LOW)
    for i in range(8):
        GPIO.output(SRCLK, GPIO.LOW)
        GPIO.output(SER, (byte >> (7 - i)) & 1)
        GPIO.output(SRCLK, GPIO.HIGH)
    GPIO.output(RCLK, GPIO.HIGH)


def display_number(num):
    num_str = str(num).zfill(2)
    shift_out(SEGMENTS[num_str[1]])
    shift_out(SEGMENTS[num_str[0]])


def countdown_timer(minutes):
    seconds = minutes * 60
    while seconds >= 0:
        display_number(seconds)
        time.sleep(1)
        seconds -= 1
    display_number(0)


countdown_timer(2)

GPIO.cleanup()
