from PyQt6.QtWidgets import QWidget, QCheckBox
from PyQt6.QtCore import pyqtSignal, QSettings
from zapzap.view.avanced_page import Ui_Avanced
from gettext import gettext as _
from .tools import updateTextCheckBox
import zapzap


class Avanced(QWidget, Ui_Avanced):

    emitHideSettingsBar = pyqtSignal()

    def __init__(self):
        super(Avanced, self).__init__()
        self.setupUi(self)

        self.settings = QSettings(zapzap.__appname__, zapzap.__appname__)
        self.load()
        self.setActionCheckBox()

    def load(self):
        self.hideBarUsers.setChecked(self.settings.value(
            "system/hide_bar_users", False, bool))
        self.donationMessage.setChecked(self.settings.value(
            "system/donation_message", True, bool))

    def save(self):
        self.settings.setValue("system/hide_bar_users",
                               self.hideBarUsers.isChecked())
        self.settings.setValue("system/donation_message",
                               self.donationMessage.isChecked())

    def setActionCheckBox(self):
        for children in self.findChildren(QCheckBox):
            children.clicked.connect(self.checkClick)
            updateTextCheckBox(children)

    def checkClick(self):
        children = self.sender()

        updateTextCheckBox(children)
        self.save()

        childrenName = children.objectName()
        if childrenName == 'hideBarUsers':
            self.emitHideSettingsBar.emit()
