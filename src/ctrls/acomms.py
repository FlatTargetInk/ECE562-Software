from time import sleep


class Connection:
    index = -1
    bits = [
            (0b10000100).to_bytes(1,byteorder='big'),
            (0b00000000).to_bytes(1,byteorder='big'),
            (0b10000101).to_bytes(1,byteorder='big'),
            (0b00000100).to_bytes(1,byteorder='big'),
            (0b10000110).to_bytes(1,byteorder='big'),
            (0b00001000).to_bytes(1,byteorder='big'),
            (0b10000111).to_bytes(1,byteorder='big'),
            (0b00001100).to_bytes(1,byteorder='big'),
            (0b01000000).to_bytes(1,byteorder='big'),
            (0b01000001).to_bytes(1,byteorder='big'),
            (0b10000001).to_bytes(1,byteorder='big'),
            (0b00010000).to_bytes(1,byteorder='big'),
            (0b10000010).to_bytes(1,byteorder='big'),
            (0b00010100).to_bytes(1,byteorder='big'),
            (0b01001000).to_bytes(1,byteorder='big'),
            (0b10001100).to_bytes(1,byteorder='big'),
            (0b10001001).to_bytes(1,byteorder='big'),
            (0b11000100).to_bytes(1,byteorder='big'),
            (0b10001010).to_bytes(1,byteorder='big'),
            (0b11001000).to_bytes(1,byteorder='big'),
            (0b10001011).to_bytes(1,byteorder='big'),
            (0b11001100).to_bytes(1,byteorder='big'),
            (0b01001100).to_bytes(1,byteorder='big'),
            (0b11101101).to_bytes(1,byteorder='big'),
            (0b10001101).to_bytes(1,byteorder='big'),
            (0b11010100).to_bytes(1,byteorder='big'),
            (0b10001110).to_bytes(1,byteorder='big'),
            (0b11011000).to_bytes(1,byteorder='big'),
            (0b10001111).to_bytes(1,byteorder='big'),
            (0b11011100).to_bytes(1,byteorder='big'),
            (0b01000100).to_bytes(1,byteorder='big'),
            (0b00001111).to_bytes(1,byteorder='big'),
            (0b10000101).to_bytes(1,byteorder='big'),
            (0b11110100).to_bytes(1,byteorder='big'),
            (0b10000110).to_bytes(1,byteorder='big'),
            (0b11111000).to_bytes(1,byteorder='big'),
            (0b10000111).to_bytes(1,byteorder='big'),
            (0b11111100).to_bytes(1,byteorder='big')
            ]

    def __init__(self, port='/dev/ttyUSB0', baud=9600, term_char=None, num_char=1):
        # lol
        self.something = "something"

    def read(self):
        sleep(1)
        self.index += 1
        if self.index < len(self.bits):
            return self.bits[self.index]
        sleep(9001)
