# Example code for communicating with Serial

# Need 'pyserial' installed
import serial

ser = serial.Serial('/dev/ttyUSB0') # Open serial port

# Write a string
ser.write("Hello World!".encode())

# Read a eight bytes (changable)
msg = ser.read(8)
