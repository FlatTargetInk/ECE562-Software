from PySide import QtGui
from views.visualizer import Ui_Dialog

class MainView(QtGui.QMainWindow):

    #### properties for widget value ####
    @property
    def VMAddr0(self):
        return self.ui.lineEdit_VMAddr0.text()
    @VMAddr0.setter
    def VMAddr0(self, value):
        self.ui.lineEdit_VMAddr0.setText(value)
    @property
    def VMAddr1(self):
        return self.ui.lineEdit_VMAddr1.text()
    @VMAddr1.setter
    def VMAddr1(self, value):
        self.ui.lineEdit_VMAddr1.setText(value)
    @property
    def VMAddr2(self):
        return self.ui.lineEdit_VMAddr2.text()
    @VMAddr2.setter
    def VMAddr2(self, value):
        self.ui.lineEdit_VMAddr2.setText(value)
    @property
    def VMAddr3(self):
        return self.ui.lineEdit_VMAddr3.text()
    @VMAddr3.setter
    def VMAddr3(self, value):
        self.ui.lineEdit_VMAddr3.setText(value)
    @property
    def VMAddr4(self):
        return self.ui.lineEdit_VMAddr4.text()
    @VMAddr4.setter
    def VMAddr4(self, value):
        self.ui.lineEdit_VMAddr4.setText(value)
    @property
    def VMAddr5(self):
        return self.ui.lineEdit_VMAddr5.text()
    @VMAddr5.setter
    def VMAddr5(self, value):
        self.ui.lineEdit_VMAddr5.setText(value)
    @property
    def VMAddr6(self):
        return self.ui.lineEdit_VMAddr6.text()
    @VMAddr6.setter
    def VMAddr6(self, value):
        self.ui.lineEdit_VMAddr6.setText(value)
    @property
    def VMAddr7(self):
        return self.ui.lineEdit_VMAddr7.text()
    @VMAddr7.setter
    def VMAddr7(self, value):
        self.ui.lineEdit_VMAddr7.setText(value)
    @property
    def VMAddr8(self):
        return self.ui.lineEdit_VMAddr8.text()
    @VMAddr8.setter
    def VMAddr8(self, value):
        self.ui.lineEdit_VMAddr8.setText(value)
    @property
    def VMAddr9(self):
        return self.ui.lineEdit_VMAddr9.text()
    @VMAddr9.setter
    def VMAddr9(self, value):
        self.ui.lineEdit_VMAddr9.setText(value)
    @property
    def VMAddr10(self):
        return self.ui.lineEdit_VMAddr10.text()
    @VMAddr10.setter
    def VMAddr10(self, value):
        self.ui.lineEdit_VMAddr10.setText(value)
    @property
    def VMAddr11(self):
        return self.ui.lineEdit_VMAddr11.text()
    @VMAddr11.setter
    def VMAddr11(self, value):
        self.ui.lineEdit_VMAddr11.setText(value)
    @property
    def VMAddr12(self):
        return self.ui.lineEdit_VMAddr12.text()
    @VMAddr12.setter
    def VMAddr12(self, value):
        self.ui.lineEdit_VMAddr12.setText(value)
    @property
    def VMAddr13(self):
        return self.ui.lineEdit_VMAddr13.text()
    @VMAddr13.setter
    def VMAddr13(self, value):
        self.ui.lineEdit_VMAddr13.setText(value)
    @property
    def VMAddr14(self):
        return self.ui.lineEdit_VMAddr14.text()
    @VMAddr14.setter
    def VMAddr14(self, value):
        self.ui.lineEdit_VMAddr14.setText(value)
    @property
    def VMAddr15(self):
        return self.ui.lineEdit_VMAddr15.text()
    @VMAddr15.setter
    def VMAddr15(self, value):
        self.ui.lineEdit_VMAddr15.setText(value)
    @property
    def PABit0(self):
        return self.ui.lineEdit_PABit0.text()
    @PABit0.setter
    def PABit0(self, value):
        self.ui.lineEdit_PABit0.setText(value)
    @property
    def PABit1(self):
        return self.ui.lineEdit_PABit1.text()
    @PABit1.setter
    def PABit1(self, value):
        self.ui.lineEdit_PABit1.setText(value)
    @property
    def PABit2(self):
        return self.ui.lineEdit_PABit2.text()
    @PABit2.setter
    def PABit2(self, value):
        self.ui.lineEdit_PABit2.setText(value)
    @property
    def PABit3(self):
        return self.ui.lineEdit_PABit3.text()
    @PABit3.setter
    def PABit3(self, value):
        self.ui.lineEdit_PABit3.setText(value)
    @property
    def PABit4(self):
        return self.ui.lineEdit_PABit4.text()
    @PABit4.setter
    def PABit4(self, value):
        self.ui.lineEdit_PABit4.setText(value)
    @property
    def PABit5(self):
        return self.ui.lineEdit_PABit5.text()
    @PABit5.setter
    def PABit5(self, value):
        self.ui.lineEdit_PABit5.setText(value)
    @property
    def PABit6(self):
        return self.ui.lineEdit_PABit6.text()
    @PABit6.setter
    def PABit6(self, value):
        self.ui.lineEdit_PABit6.setText(value)
    @property
    def PABit7(self):
        return self.ui.lineEdit_PABit7.text()
    @PABit7.setter
    def PABit7(self, value):
        self.ui.lineEdit_PABit7.setText(value)
    @property
    def PABit8(self):
        return self.ui.lineEdit_PABit8.text()
    @PABit8.setter
    def PABit8(self, value):
        self.ui.lineEdit_PABit8.setText(value)
    @property
    def PABit9(self):
        return self.ui.lineEdit_PABit9.text()
    @PABit9.setter
    def PABit9(self, value):
        self.ui.lineEdit_PABit9.setText(value)
    @property
    def PABit10(self):
        return self.ui.lineEdit_PABit10.text()
    @PABit10.setter
    def PABit10(self, value):
        self.ui.lineEdit_PABit10.setText(value)
    @property
    def PABit11(self):
        return self.ui.lineEdit_PABit11.text()
    @PABit11.setter
    def PABit11(self, value):
        self.ui.lineEdit_PABit11.setText(value)
    @property
    def PABit12(self):
        return self.ui.lineEdit_PABit12.text()
    @PABit12.setter
    def PABit12(self, value):
        self.ui.lineEdit_PABit12.setText(value)
    @property
    def PABit13(self):
        return self.ui.lineEdit_PABit13.text()
    @PABit13.setter
    def PABit13(self, value):
        self.ui.lineEdit_PABit13.setText(value)
    @property
    def PABit14(self):
        return self.ui.lineEdit_PABit14.text()
    @PABit14.setter
    def PABit14(self, value):
        self.ui.lineEdit_PABit14.setText(value)
    @property
    def PABit15(self):
        return self.ui.lineEdit_PABit15.text()
    @PABit15.setter
    def PABit15(self, value):
        self.ui.lineEdit_PABit15.setText(value)
    @property
    def PMAddr0(self):
        return self.ui.lineEdit_PMAddr0.text()
    @PMAddr0.setter
    def PMAddr0(self, value):
        self.ui.lineEdit_PMAddr0.setText(value)
    @property
    def PMAddr1(self):
        return self.ui.lineEdit_PMAddr1.text()
    @PMAddr1.setter
    def PMAddr1(self, value):
        self.ui.lineEdit_PMAddr1.setText(value)
    @property
    def PMAddr2(self):
        return self.ui.lineEdit_PMAddr2.text()
    @PMAddr2.setter
    def PMAddr2(self, value):
        self.ui.lineEdit_PMAddr2.setText(value)
    @property
    def PMAddr3(self):
        return self.ui.lineEdit_PMAddr3.text()
    @PMAddr3.setter
    def PMAddr3(self, value):
        self.ui.lineEdit_PMAddr3.setText(value)
    @property
    def Connect(self):
        return self.ui.pushButton_Connect.isChecked()
    @Connect.setter
    def Connect(self, value):
        self.ui.pushButton_Connect.setChecked(value)
    @property
    def Disconnect(self):
        return self.ui.pushButton_Disconnect.isChecked()
    @Disconnect.setter
    def Disconnect(self, value):
        self.ui.pushButton_Disconnect.setChecked(value)

    #### properties for widget enabled state ####
    @property
    def VMAddr0_enabled(self):
        return self.ui.lineEdit_VMAddr0.isEnabled()
    @VMAddr0_enabled.setter
    def VMAddr0_enabled(self, value):
        self.ui.lineEdit_VMAddr0.setEnabled(value)
    @property
    def VMAddr1_enabled(self):
        return self.ui.lineEdit_VMAddr1.isEnabled()
    @VMAddr1_enabled.setter
    def VMAddr1_enabled(self, value):
        self.ui.lineEdit_VMAddr1.setEnabled(value)
    @property
    def VMAddr2_enabled(self):
        return self.ui.lineEdit_VMAddr2.isEnabled()
    @VMAddr2_enabled.setter
    def VMAddr2_enabled(self, value):
        self.ui.lineEdit_VMAddr2.setEnabled(value)
    @property
    def VMAddr3_enabled(self):
        return self.ui.lineEdit_VMAddr3.isEnabled()
    @VMAddr3_enabled.setter
    def VMAddr3_enabled(self, value):
        self.ui.lineEdit_VMAddr3.setEnabled(value)
    @property
    def VMAddr4_enabled(self):
        return self.ui.lineEdit_VMAddr4.isEnabled()
    @VMAddr4_enabled.setter
    def VMAddr4_enabled(self, value):
        self.ui.lineEdit_VMAddr4.setEnabled(value)
    @property
    def VMAddr5_enabled(self):
        return self.ui.lineEdit_VMAddr5.isEnabled()
    @VMAddr5_enabled.setter
    def VMAddr5_enabled(self, value):
        self.ui.lineEdit_VMAddr5.setEnabled(value)
    @property
    def VMAddr6_enabled(self):
        return self.ui.lineEdit_VMAddr6.isEnabled()
    @VMAddr6_enabled.setter
    def VMAddr6_enabled(self, value):
        self.ui.lineEdit_VMAddr6.setEnabled(value)
    @property
    def VMAddr7_enabled(self):
        return self.ui.lineEdit_VMAddr7.isEnabled()
    @VMAddr7_enabled.setter
    def VMAddr7_enabled(self, value):
        self.ui.lineEdit_VMAddr7.setEnabled(value)
    @property
    def VMAddr8_enabled(self):
        return self.ui.lineEdit_VMAddr8.isEnabled()
    @VMAddr8_enabled.setter
    def VMAddr8_enabled(self, value):
        self.ui.lineEdit_VMAddr8.setEnabled(value)
    @property
    def VMAddr9_enabled(self):
        return self.ui.lineEdit_VMAddr9.isEnabled()
    @VMAddr9_enabled.setter
    def VMAddr9_enabled(self, value):
        self.ui.lineEdit_VMAddr9.setEnabled(value)
    @property
    def VMAddr10_enabled(self):
        return self.ui.lineEdit_VMAddr10.isEnabled()
    @VMAddr10_enabled.setter
    def VMAddr10_enabled(self, value):
        self.ui.lineEdit_VMAddr10.setEnabled(value)
    @property
    def VMAddr11_enabled(self):
        return self.ui.lineEdit_VMAddr11.isEnabled()
    @VMAddr11_enabled.setter
    def VMAddr11_enabled(self, value):
        self.ui.lineEdit_VMAddr11.setEnabled(value)
    @property
    def VMAddr12_enabled(self):
        return self.ui.lineEdit_VMAddr12.isEnabled()
    @VMAddr12_enabled.setter
    def VMAddr12_enabled(self, value):
        self.ui.lineEdit_VMAddr12.setEnabled(value)
    @property
    def VMAddr13_enabled(self):
        return self.ui.lineEdit_VMAddr13.isEnabled()
    @VMAddr13_enabled.setter
    def VMAddr13_enabled(self, value):
        self.ui.lineEdit_VMAddr13.setEnabled(value)
    @property
    def VMAddr14_enabled(self):
        return self.ui.lineEdit_VMAddr14.isEnabled()
    @VMAddr14_enabled.setter
    def VMAddr14_enabled(self, value):
        self.ui.lineEdit_VMAddr14.setEnabled(value)
    @property
    def VMAddr15_enabled(self):
        return self.ui.lineEdit_VMAddr15.isEnabled()
    @VMAddr15_enabled.setter
    def VMAddr15_enabled(self, value):
        self.ui.lineEdit_VMAddr15.setEnabled(value)
    @property
    def PABit0_enabled(self):
        return self.ui.lineEdit_PABit0.isEnabled()
    @PABit0_enabled.setter
    def PABit0_enabled(self, value):
        self.ui.lineEdit_PABit0.setEnabled(value)
    @property
    def PABit1_enabled(self):
        return self.ui.lineEdit_PABit1.isEnabled()
    @PABit1_enabled.setter
    def PABit1_enabled(self, value):
        self.ui.lineEdit_PABit1.setEnabled(value)
    @property
    def PABit2_enabled(self):
        return self.ui.lineEdit_PABit2.isEnabled()
    @PABit2_enabled.setter
    def PABit2_enabled(self, value):
        self.ui.lineEdit_PABit2.setEnabled(value)
    @property
    def PABit3_enabled(self):
        return self.ui.lineEdit_PABit3.isEnabled()
    @PABit3_enabled.setter
    def PABit3_enabled(self, value):
        self.ui.lineEdit_PABit3.setEnabled(value)
    @property
    def PABit4_enabled(self):
        return self.ui.lineEdit_PABit4.isEnabled()
    @PABit4_enabled.setter
    def PABit4_enabled(self, value):
        self.ui.lineEdit_PABit4.setEnabled(value)
    @property
    def PABit5_enabled(self):
        return self.ui.lineEdit_PABit5.isEnabled()
    @PABit5_enabled.setter
    def PABit5_enabled(self, value):
        self.ui.lineEdit_PABit5.setEnabled(value)
    @property
    def PABit6_enabled(self):
        return self.ui.lineEdit_PABit6.isEnabled()
    @PABit6_enabled.setter
    def PABit6_enabled(self, value):
        self.ui.lineEdit_PABit6.setEnabled(value)
    @property
    def PABit7_enabled(self):
        return self.ui.lineEdit_PABit7.isEnabled()
    @PABit7_enabled.setter
    def PABit7_enabled(self, value):
        self.ui.lineEdit_PABit7.setEnabled(value)
    @property
    def PABit8_enabled(self):
        return self.ui.lineEdit_PABit8.isEnabled()
    @PABit8_enabled.setter
    def PABit8_enabled(self, value):
        self.ui.lineEdit_PABit8.setEnabled(value)
    @property
    def PABit9_enabled(self):
        return self.ui.lineEdit_PABit9.isEnabled()
    @PABit9_enabled.setter
    def PABit9_enabled(self, value):
        self.ui.lineEdit_PABit9.setEnabled(value)
    @property
    def PABit10_enabled(self):
        return self.ui.lineEdit_PABit10.isEnabled()
    @PABit10_enabled.setter
    def PABit10_enabled(self, value):
        self.ui.lineEdit_PABit10.setEnabled(value)
    @property
    def PABit11_enabled(self):
        return self.ui.lineEdit_PABit11.isEnabled()
    @PABit11_enabled.setter
    def PABit11_enabled(self, value):
        self.ui.lineEdit_PABit11.setEnabled(value)
    @property
    def PABit12_enabled(self):
        return self.ui.lineEdit_PABit12.isEnabled()
    @PABit12_enabled.setter
    def PABit12_enabled(self, value):
        self.ui.lineEdit_PABit12.setEnabled(value)
    @property
    def PABit13_enabled(self):
        return self.ui.lineEdit_PABit13.isEnabled()
    @PABit13_enabled.setter
    def PABit13_enabled(self, value):
        self.ui.lineEdit_PABit13.setEnabled(value)
    @property
    def PABit14_enabled(self):
        return self.ui.lineEdit_PABit14.isEnabled()
    @PABit14_enabled.setter
    def PABit14_enabled(self, value):
        self.ui.lineEdit_PABit14.setEnabled(value)
    @property
    def PABit15_enabled(self):
        return self.ui.lineEdit_PABit15.isEnabled()
    @PABit15_enabled.setter
    def PABit15_enabled(self, value):
        self.ui.lineEdit_PABit15.setEnabled(value)
    @property
    def PMAddr0_enabled(self):
        return self.ui.lineEdit_PMAddr0.isEnabled()
    @PMAddr0_enabled.setter
    def PMAddr0_enabled(self, value):
        self.ui.lineEdit_PMAddr0.setEnabled(value)
    @property
    def PMAddr1_enabled(self):
        return self.ui.lineEdit_PMAddr1.isEnabled()
    @PMAddr1_enabled.setter
    def PMAddr1_enabled(self, value):
        self.ui.lineEdit_PMAddr1.setEnabled(value)
    @property
    def PMAddr2_enabled(self):
        return self.ui.lineEdit_PMAddr2.isEnabled()
    @PMAddr2_enabled.setter
    def PMAddr2_enabled(self, value):
        self.ui.lineEdit_PMAddr2.setEnabled(value)
    @property
    def PMAddr3_enabled(self):
        return self.ui.lineEdit_PMAddr3.isEnabled()
    @PMAddr3_enabled.setter
    def PMAddr3_enabled(self, value):
        self.ui.lineEdit_PMAddr3.setEnabled(value)
    @property
    def Connect_enabled(self):
        return self.ui.pushButton_Connect.isEnabled()
    @Connect_enabled.setter
    def Connect_enabled(self, value):
        self.ui.pushButton_Connect.setEnabled(value)
    @property
    def Disconnect_enabled(self):
        return self.ui.pushButton_Disconnect.isEnabled()
    @Disconnect_enabled.setter
    def Disconnect_enabled(self, value):
        self.ui.pushButton_Disconnect.setEnabled(value)

    def __init__(self, model, main_ctrl):
        self.model = model
        self.main_ctrl = main_ctrl
        super(MainView, self).__init__()
        self.build_ui()
        # register func with model for model update announcements
        self.model.subscribe_update_func(self.update_ui_from_model)

    def build_ui(self):
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        #### set Qt model for compatible widget types ####

        #### connect widget signals to event functions ####
        self.ui.lineEdit_VMAddr0.textEdited.connect(self.on_VMAddr0)
        self.ui.lineEdit_VMAddr1.textEdited.connect(self.on_VMAddr1)
        self.ui.lineEdit_VMAddr2.textEdited.connect(self.on_VMAddr2)
        self.ui.lineEdit_VMAddr3.textEdited.connect(self.on_VMAddr3)
        self.ui.lineEdit_VMAddr4.textEdited.connect(self.on_VMAddr4)
        self.ui.lineEdit_VMAddr5.textEdited.connect(self.on_VMAddr5)
        self.ui.lineEdit_VMAddr6.textEdited.connect(self.on_VMAddr6)
        self.ui.lineEdit_VMAddr7.textEdited.connect(self.on_VMAddr7)
        self.ui.lineEdit_VMAddr8.textEdited.connect(self.on_VMAddr8)
        self.ui.lineEdit_VMAddr9.textEdited.connect(self.on_VMAddr9)
        self.ui.lineEdit_VMAddr10.textEdited.connect(self.on_VMAddr10)
        self.ui.lineEdit_VMAddr11.textEdited.connect(self.on_VMAddr11)
        self.ui.lineEdit_VMAddr12.textEdited.connect(self.on_VMAddr12)
        self.ui.lineEdit_VMAddr13.textEdited.connect(self.on_VMAddr13)
        self.ui.lineEdit_VMAddr14.textEdited.connect(self.on_VMAddr14)
        self.ui.lineEdit_VMAddr15.textEdited.connect(self.on_VMAddr15)
        self.ui.lineEdit_PABit0.textEdited.connect(self.on_PABit0)
        self.ui.lineEdit_PABit1.textEdited.connect(self.on_PABit1)
        self.ui.lineEdit_PABit2.textEdited.connect(self.on_PABit2)
        self.ui.lineEdit_PABit3.textEdited.connect(self.on_PABit3)
        self.ui.lineEdit_PABit4.textEdited.connect(self.on_PABit4)
        self.ui.lineEdit_PABit5.textEdited.connect(self.on_PABit5)
        self.ui.lineEdit_PABit6.textEdited.connect(self.on_PABit6)
        self.ui.lineEdit_PABit7.textEdited.connect(self.on_PABit7)
        self.ui.lineEdit_PABit8.textEdited.connect(self.on_PABit8)
        self.ui.lineEdit_PABit9.textEdited.connect(self.on_PABit9)
        self.ui.lineEdit_PABit10.textEdited.connect(self.on_PABit10)
        self.ui.lineEdit_PABit11.textEdited.connect(self.on_PABit11)
        self.ui.lineEdit_PABit12.textEdited.connect(self.on_PABit12)
        self.ui.lineEdit_PABit13.textEdited.connect(self.on_PABit13)
        self.ui.lineEdit_PABit14.textEdited.connect(self.on_PABit14)
        self.ui.lineEdit_PABit15.textEdited.connect(self.on_PABit15)
        self.ui.lineEdit_PMAddr0.textEdited.connect(self.on_PMAddr0)
        self.ui.lineEdit_PMAddr1.textEdited.connect(self.on_PMAddr1)
        self.ui.lineEdit_PMAddr2.textEdited.connect(self.on_PMAddr2)
        self.ui.lineEdit_PMAddr3.textEdited.connect(self.on_PMAddr3)
        self.ui.pushButton_Connect.clicked.connect(self.on_Connect)
        self.ui.pushButton_Disconnect.clicked.connect(self.on_Disconnect)

    def update_ui_from_model(self):
        print('DEBUG: update_ui_from_model called')
        #### update widget values from model ####
        self.VMAddr0 = self.model.VMAddr0
        self.VMAddr1 = self.model.VMAddr1
        self.VMAddr2 = self.model.VMAddr2
        self.VMAddr3 = self.model.VMAddr3
        self.VMAddr4 = self.model.VMAddr4
        self.VMAddr5 = self.model.VMAddr5
        self.VMAddr6 = self.model.VMAddr6
        self.VMAddr7 = self.model.VMAddr7
        self.VMAddr8 = self.model.VMAddr8
        self.VMAddr9 = self.model.VMAddr9
        self.VMAddr10 = self.model.VMAddr10
        self.VMAddr11 = self.model.VMAddr11
        self.VMAddr12 = self.model.VMAddr12
        self.VMAddr13 = self.model.VMAddr13
        self.VMAddr14 = self.model.VMAddr14
        self.VMAddr15 = self.model.VMAddr15
        self.PABit0 = self.model.PABit0
        self.PABit1 = self.model.PABit1
        self.PABit2 = self.model.PABit2
        self.PABit3 = self.model.PABit3
        self.PABit4 = self.model.PABit4
        self.PABit5 = self.model.PABit5
        self.PABit6 = self.model.PABit6
        self.PABit7 = self.model.PABit7
        self.PABit8 = self.model.PABit8
        self.PABit9 = self.model.PABit9
        self.PABit10 = self.model.PABit10
        self.PABit11 = self.model.PABit11
        self.PABit12 = self.model.PABit12
        self.PABit13 = self.model.PABit13
        self.PABit14 = self.model.PABit14
        self.PABit15 = self.model.PABit15
        self.PMAddr0 = self.model.PMAddr0
        self.PMAddr1 = self.model.PMAddr1
        self.PMAddr2 = self.model.PMAddr2
        self.PMAddr3 = self.model.PMAddr3
        self.Connect = self.model.Connect
        self.Disconnect = self.model.Disconnect

    #### widget signal event functions ####
    def on_VMAddr0(self, text): self.main_ctrl.change_VMAddr0(text)
    def on_VMAddr1(self, text): self.main_ctrl.change_VMAddr1(text)
    def on_VMAddr2(self, text): self.main_ctrl.change_VMAddr2(text)
    def on_VMAddr3(self, text): self.main_ctrl.change_VMAddr3(text)
    def on_VMAddr4(self, text): self.main_ctrl.change_VMAddr4(text)
    def on_VMAddr5(self, text): self.main_ctrl.change_VMAddr5(text)
    def on_VMAddr6(self, text): self.main_ctrl.change_VMAddr6(text)
    def on_VMAddr7(self, text): self.main_ctrl.change_VMAddr7(text)
    def on_VMAddr8(self, text): self.main_ctrl.change_VMAddr8(text)
    def on_VMAddr9(self, text): self.main_ctrl.change_VMAddr9(text)
    def on_VMAddr10(self, text): self.main_ctrl.change_VMAddr10(text)
    def on_VMAddr11(self, text): self.main_ctrl.change_VMAddr11(text)
    def on_VMAddr12(self, text): self.main_ctrl.change_VMAddr12(text)
    def on_VMAddr13(self, text): self.main_ctrl.change_VMAddr13(text)
    def on_VMAddr14(self, text): self.main_ctrl.change_VMAddr14(text)
    def on_VMAddr15(self, text): self.main_ctrl.change_VMAddr15(text)
    def on_PABit0(self, text): self.main_ctrl.change_PABit0(text)
    def on_PABit1(self, text): self.main_ctrl.change_PABit1(text)
    def on_PABit2(self, text): self.main_ctrl.change_PABit2(text)
    def on_PABit3(self, text): self.main_ctrl.change_PABit3(text)
    def on_PABit4(self, text): self.main_ctrl.change_PABit4(text)
    def on_PABit5(self, text): self.main_ctrl.change_PABit5(text)
    def on_PABit6(self, text): self.main_ctrl.change_PABit6(text)
    def on_PABit7(self, text): self.main_ctrl.change_PABit7(text)
    def on_PABit8(self, text): self.main_ctrl.change_PABit8(text)
    def on_PABit9(self, text): self.main_ctrl.change_PABit9(text)
    def on_PABit10(self, text): self.main_ctrl.change_PABit10(text)
    def on_PABit11(self, text): self.main_ctrl.change_PABit11(text)
    def on_PABit12(self, text): self.main_ctrl.change_PABit12(text)
    def on_PABit13(self, text): self.main_ctrl.change_PABit13(text)
    def on_PABit14(self, text): self.main_ctrl.change_PABit14(text)
    def on_PABit15(self, text): self.main_ctrl.change_PABit15(text)
    def on_PMAddr0(self, text): self.main_ctrl.change_PMAddr0(text)
    def on_PMAddr1(self, text): self.main_ctrl.change_PMAddr1(text)
    def on_PMAddr2(self, text): self.main_ctrl.change_PMAddr2(text)
    def on_PMAddr3(self, text): self.main_ctrl.change_PMAddr3(text)
    def on_Connect(self): self.main_ctrl.change_Connect(self.Connect)
    def on_Disconnect(self): self.main_ctrl.change_Disconnect(self.Disconnect)
