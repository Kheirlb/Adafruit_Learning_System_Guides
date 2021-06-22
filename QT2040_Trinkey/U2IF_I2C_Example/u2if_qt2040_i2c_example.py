"""
CircuitPython U2IF I2C QAT2040 Trinkey Example

Reads the temperature every two seconds from an MCP9808 I2C temperature sensor
connected via STEMMA QT.
"""
import time
import board
import adafruit_mcp9808

i2c = board.I2C()  # uses board.SCL and board.SDA
mcp9808 = adafruit_mcp9808.MCP9808(i2c)

while True:
    temperature_celsius = mcp9808.temperature
    temperature_fahrenheit = temperature_celsius * 9 / 5 + 32
    print("Temperature: {:.2f} C {:.2f} F ".format(temperature_celsius, temperature_fahrenheit))
    time.sleep(2)
