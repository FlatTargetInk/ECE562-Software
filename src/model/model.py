from PySide import QtGui

class Model(object):

    #### properties for value of Qt model contents ####

    def __init__(self):
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
