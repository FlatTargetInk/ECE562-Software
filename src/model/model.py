from PySide import QtGui

class Page:
    virtAddr = None # Address in virtual memory
    data = [] # Data within memory

    # Constructor
    def __init__(self, page_size, p_virtAddr):
        self.data = [0 for x in range(page_size)]
        self.virtAddr = p_virtAddr

class Model(object):
    def __init__(self, num_pages, num_frames, page_size):
        self._update_funcs = []
        self.config_section = 'settings'
        self.config_options = (
            ('VMAddr0', 'get'),
            ('VMAddr1', 'get'),
            ('VMAddr2', 'get'),
            ('VMAddr3', 'get'),
            ('VMAddr4', 'get'),
            ('VMAddr5', 'get'),
            ('VMAddr6', 'get'),
            ('VMAddr7', 'get'),
            ('VMAddr8', 'get'),
            ('VMAddr9', 'get'),
            ('VMAddr10', 'get'),
            ('VMAddr11', 'get'),
            ('VMAddr12', 'get'),
            ('VMAddr13', 'get'),
            ('VMAddr14', 'get'),
            ('VMAddr15', 'get'),
            ('PABit0', 'get'),
            ('PABit1', 'get'),
            ('PABit2', 'get'),
            ('PABit3', 'get'),
            ('PABit4', 'get'),
            ('PABit5', 'get'),
            ('PABit6', 'get'),
            ('PABit7', 'get'),
            ('PABit8', 'get'),
            ('PABit9', 'get'),
            ('PABit10', 'get'),
            ('PABit11', 'get'),
            ('PABit12', 'get'),
            ('PABit13', 'get'),
            ('PABit14', 'get'),
            ('PABit15', 'get'),
            ('PMAddr0', 'get'),
            ('PMAddr1', 'get'),
            ('PMAddr2', 'get'),
            ('PMAddr3', 'get'),
            ('Connect', 'getboolean'),
            ('Disconnect', 'getboolean'),
        )

        #### create Qt models for compatible widget types ####

        #### model variables ####
        self.VMAddr0 = None
        self.VMAddr1 = None
        self.VMAddr2 = None
        self.VMAddr3 = None
        self.VMAddr4 = None
        self.VMAddr5 = None
        self.VMAddr6 = None
        self.VMAddr7 = None
        self.VMAddr8 = None
        self.VMAddr9 = None
        self.VMAddr10 = None
        self.VMAddr11 = None
        self.VMAddr12 = None
        self.VMAddr13 = None
        self.VMAddr14 = None
        self.VMAddr15 = None
        self.PABit0 = None
        self.PABit1 = None
        self.PABit2 = None
        self.PABit3 = None
        self.PABit4 = None
        self.PABit5 = None
        self.PABit6 = None
        self.PABit7 = None
        self.PABit8 = None
        self.PABit9 = None
        self.PABit10 = None
        self.PABit11 = None
        self.PABit12 = None
        self.PABit13 = None
        self.PABit14 = None
        self.PABit15 = None
        self.PMAddr0 = None
        self.PMAddr1 = None
        self.PMAddr2 = None
        self.PMAddr3 = None
        self.Connect = None
        self.Disconnect = None

    def subscribe_update_func(self, func):
        if func not in self._update_funcs:
            self._update_funcs.append(func)

    def unsubscribe_update_func(self, func):
        if func in self._update_funcs:
            self._update_funcs.remove(func)

    def announce_update(self):
        for func in self._update_funcs:
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
        self.physicalMem[framenum] = self.virtualMem[pagenum]
        # Update page table
        self.validbit[pagenum] = True
        # Update variables
        self.pageIn = pagenum

    # Remove page from physical memory
    def _pageout(self, pagenum, framenum):
        # Remove page from physical memory
        self.physicalMem[framenum] = 0
        # Update page table

    # Parse input
    def parsein(self, msg):
        # TODO Determine messages, create parsing techniques for messages
        msg_type = msg[1] & 0xE0
        if msg_type == 128:
            # Valid Read
            phy_addr = msg[1] & 0x0F
            vm_addr = msg[0] & 0xFC
        elif msg_type == 64:
            # Page Fault
            phy_addr = msg[1] & 0x0F
            frame_num = phy_addr & 0x0C
            vm_out = msg[0] & 0xF0
            vm_in = msg[0] & 0x0F
            self._pageout(vm_out, frame_num)
            self._pagein(vm_in, frame_num)
        else:
            return -1
        return 0
