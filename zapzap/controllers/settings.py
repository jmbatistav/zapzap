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

    def __init__(self, parent=None):
        super(Settings, self).__init__()
        self.setupUi(self)
        self.setParent(parent)

        self.setSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum,
                           QtWidgets.QSizePolicy.Policy.Maximum)

        # we have a parent, install an eventFilter so that when it's resized
        # the notification will be correctly moved to the right corner
        self.parent().installEventFilter(self)

        # raise the widget and adjust its size to the minimum
        self.raise_()
        self.adjustSize()

        self.corner = QtCore.Qt.Corner.TopLeftCorner
        self.margin = 10

        self.setGeo()
        self.setDefaultEventButtonInMenu()
        self.setPages()

        self.close()

    def setPages(self):
        # General
        self.pages_id['btn_general'] = self.settings_stacked.addWidget(
            General())

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
        self.pages_id['btn_about'] = self.settings_stacked.addWidget(About())

    def setDefaultEventButtonInMenu(self):
        for item in self.menu.findChildren(QPushButton):
            item.clicked.connect(self.buttonClick)

    def buttonClick(self):
        btn = self.sender()  # returns a pointer to the object that sent the signal
        btnName = btn.objectName()
        print(btnName)

        self.settings_stacked.setCurrentIndex(self.pages_id[btnName])

    def eventFilter(self, source, event):
        if source == self.parent() and event.type() == QtCore.QEvent.Type.Resize:
            self.setGeo()
        return super(Settings, self).eventFilter(source, event)

    def setGeo(self):
        parentRect = self.parent().rect()
        geo = self.geometry()
        geo.moveBottomLeft(
            parentRect.bottomLeft() + QtCore.QPoint(self.margin+40, -self.margin))
        self.setGeometry(geo)


# Settings page
""" self.zapSettings = Settings()
self.zapSettings.emitDisableUser.connect(self.emitDisableUser)
self.zapSettings.emitDeleteUser.connect(self.emitDeleteUser)
self.zapSettings.emitEditUser.connect(self.emitEditUser)
self.zapSettings.emitNewtUser.connect(self.emitNewUser)
self.zapSettings.emitSetSpellChecker.connect(self.emitSetSpellChecker)
self.zapSettings.emitDisableSpellChecker.connect(
    self.emitDisableSpellChecker)
self.zapSettings.emitNotifications.connect(self.emitNotifications)
self.zapSettings.emitQuit.connect(lambda x=None: self.closeEvent(x))
self.zapSettings.emitGoHome.connect(
    lambda: self.main_stacked.setCurrentIndex(0))
self.zapSettings.emitKeepBackground.connect(
    self.actionHide_on_close.setChecked)
self.zapSettings.emitDisableTrayIcon.connect(self.tray.setVisible)
self.zapSettings.emitSetHideMenuBar.connect(self.setHideMenuBar)
self.zapSettings.emitUpdateUIDecoration.connect(self.updateSCD)

self.zapSettings.emitUpdateTheme.connect(self.setThemeApp)

self.zapSettings.updateUsersShortcuts() """
