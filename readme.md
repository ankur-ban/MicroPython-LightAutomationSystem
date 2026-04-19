# Light Automation System

This project contains a simple MicroPython script that sequentially toggles three separate lights, creating a continuous running light automation effect. It is a great foundational script for testing GPIO outputs and hardware loops on microcontrollers like the ESP32 or ESP32-S3.

## Hardware Requirements

To set up this circuit, you will need:
* A MicroPython-compatible microcontroller (e.g., ESP32 series)
* 3x LEDs (or compatible relays if driving larger lights)
* 3x Current-limiting resistors (e.g., 220Ω or 330Ω)
* Breadboard and jumper wires

## Pin Configuration

The components should be wired to the following GPIO pins on your board:

| Component | GPIO Pin | Mode |
| :--- | :--- | :--- |
| Light 1 | `Pin 2` | Output |
| Light 2 | `Pin 4` | Output |
| Light 3 | `Pin 16` | Output |

*(Note: Ensure the grounds of your components are tied back to the common GND on your microcontroller).*

## The Code

Here is the core logic that drives the automation loop:

```python
# light automation system
from machine import Pin
from time import sleep

led1 = Pin(2, Pin.OUT)
led2 = Pin(4, Pin.OUT)
led3 = Pin(16, Pin.OUT)

while True:
    led1.on()
    sleep(1)
    led1.off()
    
    led2.on()
    sleep(1)
    led2.off()
    
    led3.on()
    sleep(1)
    led3.off()