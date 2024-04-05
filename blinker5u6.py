import gpiod as GPIO
import time
from guizero import App, Text, PushButton, ButtonGroup
import sys

red = 17
green = 18
blue = 22

def switch_on():
    if clicked.value== "red":
        print("ON")
        output1.set_value(1)
        led1_text.append(clicked.value + " LED!! ")

    if clicked.value== "green":
        print("ON")
        output2.set_value(1)
        led1_text.append(clicked.value + " LED!! ")

    if clicked.value== "blue":
        print("ON")
        output3.set_value(1)
        led1_text.append(clicked.value + " LED!! ")

def switch_off():
    print("OFF")
    output1.set_value(0)
    output2.set_value(0)
    output3.set_value(0)
    led2_text.append(clicked.value + " LED!! ")

def close_gui():
    sys.exit()
    output1.set_value(0)
    output2.set_value(0)
    output3.set_value(0)
    GPIO.cleanup()

def blink_led():
    try:
        while True:

            output.set_value(1)
            time.sleep(0.25)
            output.set_value(0)
            time.sleep(0.25)
    finally:
        output.release()


app = App(title="LED GUI")
Text(app, text = "3 LED's")
clicked = ButtonGroup(app, options=["red", "green", "blue"], horizontal=True)
Text(app, text = "switch them ON or OFF")

chip = GPIO.Chip('gpiochip4')
output1 = chip.get_line(red)
output1.request(consumer="LED", type=GPIO.LINE_REQ_DIR_OUT)
output2 = chip.get_line(green)
output2.request(consumer="LED", type=GPIO.LINE_REQ_DIR_OUT)
output3 = chip.get_line(blue)
output3.request(consumer="LED", type=GPIO.LINE_REQ_DIR_OUT)

btn1 = PushButton(app, command=switch_on, text="LED ON", width=20, height=5)
btn2 = PushButton(app, command=switch_off, text="LED OFF", width=20, height=5)
btn3 = PushButton(app, command=close_gui, text="CLOSE", width=20, height=5)
#btn4 = PushButton(app, command=blink_led, text="Blink LED", width=20, height=5)

led1_text = Text(app, text = "You have switched on a ")
led2_text = Text(app, text = "OFF goes.. .")

app.display()
