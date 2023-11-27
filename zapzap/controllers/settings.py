from PyQt6.QtWidgets import QWidget, QApplication, QPushButton
from PyQt6 import QtCore, QtWidgets, QtGui
from zapzap.view.settings import Ui_Settings
from zapzap.controllers.settings_pages.general import General
from zapzap.controllers.settings_pages.account import Account
from zapzap.controllers.settings_pages.notifications import Notifications
from zapzap.controllers.settings_pages.personalization import Personalization
from zapzap.controllers.settings_pages.donations import Donations
from zapzap.controllers.settings_pages.about import About
from gettext import gettext as _
import zapzap


class Settings(QWidget, Ui_Settings):

    pages_id = {}

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
        self.pages_id['btn_general'] = self.settings_stacked.addWidget(General())
        self.pages_id['btn_account'] = self.settings_stacked.addWidget(Account())
        self.pages_id['btn_notifications'] = self.settings_stacked.addWidget(Notifications())
        self.pages_id['btn_personalization'] = self.settings_stacked.addWidget(Personalization())
        self.pages_id['btn_donations'] = self.settings_stacked.addWidget(Donations())
        self.pages_id['btn_about'] = self.settings_stacked.addWidget(About())

        print(self.pages_id)

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

    @staticmethod
    def showDialog(parent):
        qtoaster = Settings(parent)
        qtoaster.show()


""" finalizei o painel principal das configurações

1 - desativar o painel antigo
2 - submeter

3 - barra lateral da home e o botão de configurações """


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