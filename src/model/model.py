from PySide import QtGui

class Page:
    virtAddr = None # Address in virtual memory
    data = [] # Data within memory

    # Constructor
    def __init__(self, page_size, p_virtAddr):
        self.data = [0 for x in range(page_size)]
        self.virtAddr = p_virtAddr

class Model(object):
    def __init__(self):
        self._update_funcs = []
        self.config_section = 'settings'

        #### model variables ####
        self.VMAddr0 = "1"
        self.VMAddr1 = "None"
        self.VMAddr2 = "None"
        self.VMAddr3 = "None"
        self.VMAddr4 = "0"
        self.VMAddr5 = "None"
        self.VMAddr6 = "None"
        self.VMAddr7 = "None"
        self.VMAddr8 = "2"
        self.VMAddr9 = "None"
        self.VMAddr10 = "None"
        self.VMAddr11 = "None"
        self.VMAddr12 = "None"
        self.VMAddr13 = "None"
        self.VMAddr14 = "3"
        self.VMAddr15 = "None"
        self.PABit0 = "1"
        self.PABit1 = "0"
        self.PABit2 = "0"
        self.PABit3 = "0"
        self.PABit4 = "1"
        self.PABit5 = "0"
        self.PABit6 = "0"
        self.PABit7 = "0"
        self.PABit8 = "1"
        self.PABit9 = "0"
        self.PABit10 = "0"
        self.PABit11 = "0"
        self.PABit12 = "0"
        self.PABit13 = "0"
        self.PABit14 = "1"
        self.PABit15 = "0"
        self.PMAddr0 = "4"
        self.PMAddr1 = "0"
        self.PMAddr2 = "8"
        self.PMAddr3 = "14"
        self.Connect = True
        self.Disconnect = False
        self.curPHAddr = "None"
        self.curVMAddr = "None"

        self.announce_update()

    def subscribe_update_func(self, func):
        if func not in self._update_funcs:
            self._update_funcs.append(func)

    def unsubscribe_update_func(self, func):
        if func in self._update_funcs:
            self._update_funcs.remove(func)

    def announce_update(self):
        for func in self._update_funcs:
            #print(func)
            func()
    
    def __setVMAddr(self,index,val):
        if index == 0:
            self.VMAddr0 = val
        elif index == 1:
            self.VMAddr1 = val
        elif index == 2:
            self.VMAddr2 = val
        elif index == 3:
            self.VMAddr3 = val
        elif index == 4:
            self.VMAddr4 = val
        elif index == 5:
            self.VMAddr5 = val
        elif index == 6:
            self.VMAddr6 = val
        elif index == 7:
            self.VMAddr7 = val
        elif index == 8:
            self.VMAddr8 = val
        elif index == 9:
            self.VMAddr9 = val
        elif index == 10:
            self.VMAddr10 = val
        elif index == 11:
            self.VMAddr11 = val
        elif index == 12:
            self.VMAddr12 = val
        elif index == 13:
            self.VMAddr13 = val
        elif index == 14:
            self.VMAddr14 = val
        elif index == 15:
            self.VMAddr15 = val
        else:
            return -1

    def __getVMAddr(self,index):
        if index == 0:
            return self.VMAddr0
        if index == 1:
            return self.VMAddr1
        if index == 2:
            return self.VMAddr2
        if index == 3:
            return self.VMAddr3
        if index == 4:
            return self.VMAddr4
        if index == 5:
            return self.VMAddr5
        if index == 6:
            return self.VMAddr6
        if index == 7:
            return self.VMAddr7
        if index == 8:
            return self.VMAddr8
        if index == 9:
            return self.VMAddr9
        if index == 10:
            return self.VMAddr10
        if index == 11:
            return self.VMAddr11
        if index == 12:
            return self.VMAddr12
        if index == 13:
            return self.VMAddr13
        if index == 14:
            return self.VMAddr14
        if index == 15:
            return self.VMAddr15
        return -1

    def __setPMAddr(self,index,val):
        if index == 0:
            self.PMAddr0 = val
        elif index == 1:
            self.PMAddr1 = val
        elif index == 2:
            self.PMAddr2 = val
        elif index == 3:
            self.PMAddr3 = val
        else:
            return -1

    def __setPABit(self,index,val):
        if index == 0:
            self.PABit0 = val
        elif index == 1:
            self.PABit1 = val
        elif index == 2:
            self.PABit2 = val
        elif index == 3:
            self.PABit3 = val
        elif index == 4:
            self.PABit4 = val
        elif index == 5:
            self.PABit5 = val
        elif index == 6:
            self.PABit6 = val
        elif index == 7:
            self.PABit7 = val
        elif index == 8:
            self.PABit8 = val
        elif index == 9:
            self.PABit9 = val
        elif index == 10:
            self.PABit10 = val
        elif index == 11:
            self.PABit11 = val
        elif index == 12:
            self.PABit12 = val
        elif index == 13:
            self.PABit13 = val
        elif index == 14:
            self.PABit14 = val
        elif index == 15:
            self.PABit15 = val
        else:
            return -1

    # Load page from virtual memory to physical memory
    def _pagein(self, pagenum, framenum):
        # Place page into physical memory
        self.__setPMAddr(framenum,str(pagenum))
        # Update page table
        self.__setVMAddr(pagenum,str(framenum))
        self.__setPABit(pagenum,"1")

    # Remove page from physical memory
    def _pageout(self, pagenum, framenum):
        # Remove page from physical memory
        self.__setPMAddr(framenum,"None")
        # Update page table
        self.__setPABit(pagenum,"0")

    # Parse input
    def parsein(self, msg):
        #print(str(msg))
        msg[0] = int.from_bytes(msg[0],byteorder='big')
        msg[1] = int.from_bytes(msg[1],byteorder='big')
        msg_type = (msg[0] & 0xF0) >> 4
        phy_addr = msg[0] & 0x0F
        frame_num = (phy_addr & 0x0C) >> 2
        if msg_type == (1 << 3):
            # Valid Read
            #print('Valid Read')
            vm_addr = (msg[1] & 0xFC) >> 2
            self.curPHAddr = str(phy_addr)
            self.curVMAddr = str(vm_addr)
        elif msg_type == (1 << 2):
            # Page Fault
            #print('Page Fault')
            vm_out = (msg[1] & 0xF0) >> 4
            vm_in = msg[1] & 0x0F
            ofst = phy_addr & 0x03
            vm_addr = (vm_in << 2) | (ofst)
            #print('Page out:', vm_out, 'Page in:', vm_in, 'Frame num:', frame_num)
            self._pageout(vm_out, frame_num)
            self._pagein(vm_in, frame_num)
            self.curPHAddr = str(phy_addr)
            self.curVMAddr = str(vm_addr)
        else:
            #print("Rx'd", msg)
            return -1
        self.announce_update()
        return 0
