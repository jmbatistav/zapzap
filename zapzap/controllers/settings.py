from PyQt6.QtWidgets import QWidget, QApplication, QPushButton
from PyQt6 import QtCore, QtWidgets
from PyQt6.QtCore import pyqtSignal
from zapzap.view.settings import Ui_Settings
from zapzap.controllers.settings_pages.general import General
from zapzap.controllers.settings_pages.account import Account
from zapzap.controllers.settings_pages.notifications import Notifications
from zapzap.controllers.settings_pages.personalization import Personalization
from zapzap.controllers.settings_pages.donations import Donations
from zapzap.controllers.settings_pages.about import About
from zapzap.model.user import User
from gettext import gettext as _
import zapzap


class Settings(QWidget, Ui_Settings):

    pages_id = {}

    # account
    emitDisableUser = pyqtSignal(User)
    emitDeleteUser = pyqtSignal(User)
    emitEditUser = pyqtSignal(User)
    emitNewtUser = pyqtSignal(User)

    # personalization
    emitUpdateTheme = pyqtSignal(str)
    emitDisableTrayIcon = pyqtSignal(bool)
    emitNotifications = pyqtSignal()

    # Quit
    emitQuit = pyqtSignal()
    emitCloseSettings = pyqtSignal()

    # Whatsapp Settings
    emitOpenSettingsWhatsapp = pyqtSignal()

    def __init__(self, parent=None):
        super(Settings, self).__init__()
        self.setupUi(self)
        self.setParent(parent)

        self.setDefaultEventButtonInMenu()
        self.setPages()

        self.btn_close.clicked.connect(self.emitCloseSettings.emit)

    def setPages(self):
        # General
        self.generalPage = General()
        self.generalPage.emitOpenSettingsWhatsapp = self.emitOpenSettingsWhatsapp
        self.pages_id['btn_general'] = self.settings_stacked.addWidget(self.generalPage)

        # Account
        self.accountPage = Account()
        self.accountPage.emitDisableUser = self.emitDisableUser
        self.accountPage.emitDeleteUser = self.emitDeleteUser
        self.accountPage.emitEditUser = self.emitEditUser
        self.accountPage.emitNewtUser = self.emitNewtUser
        self.pages_id['btn_account'] = self.settings_stacked.addWidget(
            self.accountPage)

        # Notifications
        self.pages_id['btn_notifications'] = self.settings_stacked.addWidget(
            Notifications())

        # Personalization
        self.persoPage = Personalization()
        self.persoPage.emitUpdateTheme = self.emitUpdateTheme
        self.persoPage.emitDisableTrayIcon = self.emitDisableTrayIcon
        self.persoPage.emitNotifications = self.emitNotifications
        self.pages_id['btn_personalization'] = self.settings_stacked.addWidget(
            self.persoPage)

        # Donations
        self.pages_id['btn_donations'] = self.settings_stacked.addWidget(
            Donations())

        # About
        self.aboutPage = About()
        self.aboutPage.emitCloseSettings = self.emitCloseSettings
        self.pages_id['btn_about'] = self.settings_stacked.addWidget(self.aboutPage)

    def setDefaultEventButtonInMenu(self):
        for item in self.menu.findChildren(QPushButton):
            item.clicked.connect(self.buttonClick)

    def buttonClick(self):
        btn = self.sender()  # returns a pointer to the object that sent the signal
        btnName = btn.objectName()

        try:
            self.settings_stacked.setCurrentIndex(self.pages_id[btnName])
        except:
            self.emitQuit.emit()

