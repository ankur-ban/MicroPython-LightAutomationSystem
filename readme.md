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
