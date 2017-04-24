from PySide import QtGui
from ctrls.comms import Connection
import threading

class MainController(object):
    def __init__(self, model, port):
        self.model = model
        self.port = port
        self.serial = None

    def change_VMAddr0(self, text):
        self.model.VMAddr0 = text
        self.model.announce_update()
    def change_VMAddr1(self, text):self.model.VMAddr1 = text
    def change_VMAddr2(self, text):self.model.VMAddr2 = text
    def change_VMAddr3(self, text):self.model.VMAddr3 = text
    def change_VMAddr4(self, text):self.model.VMAddr4 = text
    def change_VMAddr5(self, text):self.model.VMAddr5 = text
    def change_VMAddr6(self, text):self.model.VMAddr6 = text
    def change_VMAddr7(self, text):self.model.VMAddr7 = text
    def change_VMAddr8(self, text):self.model.VMAddr8 = text
    def change_VMAddr9(self, text):self.model.VMAddr9 = text
    def change_VMAddr10(self, text):self.model.VMAddr10 = text
    def change_VMAddr11(self, text):self.model.VMAddr11 = text
    def change_VMAddr12(self, text):self.model.VMAddr12 = text
    def change_VMAddr13(self, text):self.model.VMAddr13 = text
    def change_VMAddr14(self, text):self.model.VMAddr14 = text
    def change_VMAddr15(self, text):self.model.VMAddr15 = text
    def change_PABit0(self, text):self.model.PABit0 = text
    def change_PABit1(self, text):self.model.PABit1 = text
    def change_PABit2(self, text):self.model.PABit2 = text
    def change_PABit3(self, text):self.model.PABit3 = text
    def change_PABit4(self, text):self.model.PABit4 = text
    def change_PABit5(self, text):self.model.PABit5 = text
    def change_PABit6(self, text):self.model.PABit6 = text
    def change_PABit7(self, text):self.model.PABit7 = text
    def change_PABit8(self, text):self.model.PABit8 = text
    def change_PABit9(self, text):self.model.PABit9 = text
    def change_PABit10(self, text):self.model.PABit10 = text
    def change_PABit11(self, text):self.model.PABit11 = text
    def change_PABit12(self, text):self.model.PABit12 = text
    def change_PABit13(self, text):self.model.PABit13 = text
    def change_PABit14(self, text):self.model.PABit14 = text
    def change_PABit15(self, text):self.model.PABit15 = text
    def change_PMAddr0(self, text):self.model.PMAddr0 = text
    def change_PMAddr1(self, text):self.model.PMAddr1 = text
    def change_PMAddr2(self, text):self.model.PMAddr2 = text
    def change_PMAddr3(self, text):self.model.PMAddr3 = text

    def Connect(self):
        if self.serial:
            # Send a ready message
            self.serial.write('x1x2x3')
            serial.read()
        self.serial = Connection(self.port)
        reading = threading.Thread(target=self.reader,daemon=True)
        reading.start()


    # def Disconnect(self):
        # self.serial.close()

    def reader(self):
        inchar = [0,0]
        while True:
            inchar[0] = self.serial.read()
            inchar[1] = self.serial.read()
            self.model.parsein(inchar)

