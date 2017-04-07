from PySide import QtGui

class MainController(object):

    def __init__(self, model):
        self.model = model

    #### widget event functions ####
    def change_VMAddr0(self, text):
        self.model.VMAddr0 = text
        print('DEBUG: change_VMAddr0 called with arg value:', text)
    def change_VMAddr1(self, text):
        self.model.VMAddr1 = text
        print('DEBUG: change_VMAddr1 called with arg value:', text)
    def change_VMAddr2(self, text):
        self.model.VMAddr2 = text
        print('DEBUG: change_VMAddr2 called with arg value:', text)
    def change_VMAddr3(self, text):
        self.model.VMAddr3 = text
        print('DEBUG: change_VMAddr3 called with arg value:', text)
    def change_VMAddr4(self, text):
        self.model.VMAddr4 = text
        print('DEBUG: change_VMAddr4 called with arg value:', text)
    def change_VMAddr5(self, text):
        self.model.VMAddr5 = text
        print('DEBUG: change_VMAddr5 called with arg value:', text)
    def change_VMAddr6(self, text):
        self.model.VMAddr6 = text
        print('DEBUG: change_VMAddr6 called with arg value:', text)
    def change_VMAddr7(self, text):
        self.model.VMAddr7 = text
        print('DEBUG: change_VMAddr7 called with arg value:', text)
    def change_VMAddr8(self, text):
        self.model.VMAddr8 = text
        print('DEBUG: change_VMAddr8 called with arg value:', text)
    def change_VMAddr9(self, text):
        self.model.VMAddr9 = text
        print('DEBUG: change_VMAddr9 called with arg value:', text)
    def change_VMAddr10(self, text):
        self.model.VMAddr10 = text
        print('DEBUG: change_VMAddr10 called with arg value:', text)
    def change_VMAddr11(self, text):
        self.model.VMAddr11 = text
        print('DEBUG: change_VMAddr11 called with arg value:', text)
    def change_VMAddr12(self, text):
        self.model.VMAddr12 = text
        print('DEBUG: change_VMAddr12 called with arg value:', text)
    def change_VMAddr13(self, text):
        self.model.VMAddr13 = text
        print('DEBUG: change_VMAddr13 called with arg value:', text)
    def change_VMAddr14(self, text):
        self.model.VMAddr14 = text
        print('DEBUG: change_VMAddr14 called with arg value:', text)
    def change_VMAddr15(self, text):
        self.model.VMAddr15 = text
        print('DEBUG: change_VMAddr15 called with arg value:', text)
    def change_PABit0(self, text):
        self.model.PABit0 = text
        print('DEBUG: change_PABit0 called with arg value:', text)
    def change_PABit1(self, text):
        self.model.PABit1 = text
        print('DEBUG: change_PABit1 called with arg value:', text)
    def change_PABit2(self, text):
        self.model.PABit2 = text
        print('DEBUG: change_PABit2 called with arg value:', text)
    def change_PABit3(self, text):
        self.model.PABit3 = text
        print('DEBUG: change_PABit3 called with arg value:', text)
    def change_PABit4(self, text):
        self.model.PABit4 = text
        print('DEBUG: change_PABit4 called with arg value:', text)
    def change_PABit5(self, text):
        self.model.PABit5 = text
        print('DEBUG: change_PABit5 called with arg value:', text)
    def change_PABit6(self, text):
        self.model.PABit6 = text
        print('DEBUG: change_PABit6 called with arg value:', text)
    def change_PABit7(self, text):
        self.model.PABit7 = text
        print('DEBUG: change_PABit7 called with arg value:', text)
    def change_PABit8(self, text):
        self.model.PABit8 = text
        print('DEBUG: change_PABit8 called with arg value:', text)
    def change_PABit9(self, text):
        self.model.PABit9 = text
        print('DEBUG: change_PABit9 called with arg value:', text)
    def change_PABit10(self, text):
        self.model.PABit10 = text
        print('DEBUG: change_PABit10 called with arg value:', text)
    def change_PABit11(self, text):
        self.model.PABit11 = text
        print('DEBUG: change_PABit11 called with arg value:', text)
    def change_PABit12(self, text):
        self.model.PABit12 = text
        print('DEBUG: change_PABit12 called with arg value:', text)
    def change_PABit13(self, text):
        self.model.PABit13 = text
        print('DEBUG: change_PABit13 called with arg value:', text)
    def change_PABit14(self, text):
        self.model.PABit14 = text
        print('DEBUG: change_PABit14 called with arg value:', text)
    def change_PABit15(self, text):
        self.model.PABit15 = text
        print('DEBUG: change_PABit15 called with arg value:', text)
    def change_PMAddr0(self, text):
        self.model.PMAddr0 = text
        print('DEBUG: change_PMAddr0 called with arg value:', text)
    def change_PMAddr1(self, text):
        self.model.PMAddr1 = text
        print('DEBUG: change_PMAddr1 called with arg value:', text)
    def change_PMAddr2(self, text):
        self.model.PMAddr2 = text
        print('DEBUG: change_PMAddr2 called with arg value:', text)
    def change_PMAddr3(self, text):
        self.model.PMAddr3 = text
        print('DEBUG: change_PMAddr3 called with arg value:', text)
    def change_Connect(self, checked):
        self.model.Connect = checked
        print('DEBUG: change_Connect called with arg value:', checked)
    def change_Disconnect(self, checked):
        self.model.Disconnect = checked
        print('DEBUG: change_Disconnect called with arg value:', checked)
