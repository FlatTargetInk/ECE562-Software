#!/usr/bin/python
import sys
from PySide import QtGui
from model.model import Model
from ctrls.controller import MainController
from views.MainView import MainView

class App(QtGui.QApplication):
    def __init__(self, sys_argv, port):
        super(App, self).__init__(sys_argv)
        self.model = Model(16, 4, 2)
        self.main_controller = MainController(self.model, port)
        self.main_view = MainView(self.model, self.main_controller)
        self.main_view.show()

if __name__ == '__main__':
    app = App(sys.argv, '/dev/ttyUSB0')
    sys.exit(app.exec_())
