import sys
from PyQt5 import QtWidgets
from model.model import Model
from ctrls.controller import MainController
from views.MainView import MainView

class App(QtWidgets.QApplication):
    def __init__(self):
        self.model = Model()
        self.main_ctrl = MainController(self.model)
        self.main_view = MainView(self.model, self.main_ctrl)
        self.main_view.show()

if __name__ == '__main__':
    app = App()
    sys.exit(app.exec_())
