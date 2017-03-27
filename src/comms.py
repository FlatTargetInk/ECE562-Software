#!/usr/bin/env python3
# This script contains the serial communication between the software and the hardware.
# As of now, the running setup is 9600 8N1 (8 bits, no parity, 1 stop bit)

import serial
import queue
import threading

class Connection:
    ser = None # Serial Connection
    inq = None # Incoming queue from serial
    outq = None # Outgoing queue to serial
    term_char = None # Terminating character decided upon between the Hardware and Software interface
    num_chars = 1 # Number of characters in a word

    def __init__(self, port='/dev/ttyUSB0', baud=9600, term_char=None, num_chars = 1):
        self.ser = serial.Serial(port=port, baudrate=baud)
        self.inq = queue.Queue()
        self.outq = queue.Queue()
        self.term_char = term_char
        # Create threads for continuous read and write
        reader = threading.Thread(target=self.__continuous_read,daemon=True)
        reader.start()
        writer = threading.Thread(target=self.__continuous_write,daemon=True)
        writer.start()

    def read(self):
        # Function for reading from the input buffer, which came from the serial connection
        return self.inq.get()

    def write(self, msg):
        # Function for writing to the output buffer, which then outputs through the serial connection
        return self.outq.put(msg)

    def _serial_read(self, num_chars=None, term_char = '\n'):
        # If chars == None, read everything out of the buffer
        outstr = ''
        if num_chars == None:
            charin = 'deadbeef'
            while charin != term_char:
                charin = self.ser.read().decode()
                outstr += charin
            return outstr
        for i in range(num_chars):
            outstr += self.ser.read().decode()
        return outstr

    def _serial_write(self, msg):
        self.ser.write(msg.encode())
        return

    def read_ready(self):
        # Returns True if there is data waiting in the incoming queue or False if not
        return not self.inq.empty()

    def __continuous_read(self):
        while True:
            if self.term_char == None:
                wordin = self._serial_read(num_chars = self.num_chars)
            else:
                wordin = self._serial_read(term_char = self.term_char)
            self.inq.put(wordin)
        return 1

    def __continuous_write(self):
        while True:
            out_msg = self.outq.get()
            if self.term_char != None:
                out_msg += term_char
            self._serial_write(out_msg)
        return 1

def test():
    import sys
    print("This is a test.")
    con = Connection()
    if (len(sys.argv) > 1) and (sys.argv[1] == "-c"):
        print("Enabling continuous read mode")
        while True:
            print(con.read())
        return
    con.write(input("Enter a message to send: "))
    print("Data is in the incoming queue:",con.read_ready())
    print(con.read())
    print("Data is in the incoming queue:",con.read_ready())

if __name__ == "__main__":
    test()
