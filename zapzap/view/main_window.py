from gettext import gettext as _
# Form implementation generated from reading ui file './zapzap/view/main_window.ui'
#
# Created by: PyQt6 UI code generator 6.5.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 600)
        MainWindow.setMinimumSize(QtCore.QSize(200, 200))
        self.appMargins = QtWidgets.QWidget(parent=MainWindow)
        self.appMargins.setObjectName("appMargins")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.appMargins)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.app = QtWidgets.QFrame(parent=self.appMargins)
        self.app.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.app.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.app.setObjectName("app")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.app)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.headbar = QtWidgets.QFrame(parent=self.app)
        self.headbar.setMinimumSize(QtCore.QSize(0, 35))
        self.headbar.setMaximumSize(QtCore.QSize(16777215, 35))
        self.headbar.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.headbar.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.headbar.setObjectName("headbar")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.headbar)
        self.horizontalLayout_6.setContentsMargins(7, 5, 7, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.leftButtons = QtWidgets.QFrame(parent=self.headbar)
        self.leftButtons.setMinimumSize(QtCore.QSize(50, 0))
        self.leftButtons.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.leftButtons.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.leftButtons.setObjectName("leftButtons")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.leftButtons)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(7)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.closeAppBtn_left = QtWidgets.QPushButton(parent=self.leftButtons)
        self.closeAppBtn_left.setMinimumSize(QtCore.QSize(25, 25))
        self.closeAppBtn_left.setMaximumSize(QtCore.QSize(25, 25))
        self.closeAppBtn_left.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.closeAppBtn_left.setText("")
        self.closeAppBtn_left.setObjectName("closeAppBtn_left")
        self.horizontalLayout.addWidget(self.closeAppBtn_left)
        self.minimizeAppBtn_left = QtWidgets.QPushButton(parent=self.leftButtons)
        self.minimizeAppBtn_left.setMinimumSize(QtCore.QSize(25, 25))
        self.minimizeAppBtn_left.setMaximumSize(QtCore.QSize(25, 25))
        self.minimizeAppBtn_left.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.minimizeAppBtn_left.setText("")
        self.minimizeAppBtn_left.setObjectName("minimizeAppBtn_left")
        self.horizontalLayout.addWidget(self.minimizeAppBtn_left)
        self.maximizeAppBtn_left = QtWidgets.QPushButton(parent=self.leftButtons)
        self.maximizeAppBtn_left.setMinimumSize(QtCore.QSize(25, 25))
        self.maximizeAppBtn_left.setMaximumSize(QtCore.QSize(25, 25))
        self.maximizeAppBtn_left.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.maximizeAppBtn_left.setText("")
        self.maximizeAppBtn_left.setObjectName("maximizeAppBtn_left")
        self.horizontalLayout.addWidget(self.maximizeAppBtn_left)
        self.settingsTopBtn_left = QtWidgets.QPushButton(parent=self.leftButtons)
        self.settingsTopBtn_left.setMinimumSize(QtCore.QSize(25, 25))
        self.settingsTopBtn_left.setMaximumSize(QtCore.QSize(25, 25))
        self.settingsTopBtn_left.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.settingsTopBtn_left.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.settingsTopBtn_left.setText("")
        self.settingsTopBtn_left.setObjectName("settingsTopBtn_left")
        self.horizontalLayout.addWidget(self.settingsTopBtn_left)
        self.horizontalLayout_6.addWidget(self.leftButtons)
        self.leftBox = QtWidgets.QFrame(parent=self.headbar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy)
        self.leftBox.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.leftBox.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.leftBox.setObjectName("leftBox")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.leftBox)
        self.horizontalLayout_7.setContentsMargins(7, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(7)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.zapBoxMenu = QtWidgets.QFrame(parent=self.leftBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.zapBoxMenu.sizePolicy().hasHeightForWidth())
        self.zapBoxMenu.setSizePolicy(sizePolicy)
        self.zapBoxMenu.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.zapBoxMenu.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.zapBoxMenu.setObjectName("zapBoxMenu")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.zapBoxMenu)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.zapMenu = QtWidgets.QHBoxLayout()
        self.zapMenu.setContentsMargins(0, -1, -1, -1)
        self.zapMenu.setSpacing(15)
        self.zapMenu.setObjectName("zapMenu")
        self.zFile = QtWidgets.QPushButton(parent=self.zapBoxMenu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.zFile.sizePolicy().hasHeightForWidth())
        self.zFile.setSizePolicy(sizePolicy)
        self.zFile.setObjectName("zFile")
        self.zapMenu.addWidget(self.zFile)
        self.zView = QtWidgets.QPushButton(parent=self.zapBoxMenu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.zView.sizePolicy().hasHeightForWidth())
        self.zView.setSizePolicy(sizePolicy)
        self.zView.setObjectName("zView")
        self.zapMenu.addWidget(self.zView)
        self.zChat = QtWidgets.QPushButton(parent=self.zapBoxMenu)
        self.zChat.setObjectName("zChat")
        self.zapMenu.addWidget(self.zChat)
        self.zHelp = QtWidgets.QPushButton(parent=self.zapBoxMenu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.zHelp.sizePolicy().hasHeightForWidth())
        self.zHelp.setSizePolicy(sizePolicy)
        self.zHelp.setObjectName("zHelp")
        self.zapMenu.addWidget(self.zHelp)
        self.horizontalLayout_2.addLayout(self.zapMenu)
        self.horizontalLayout_7.addWidget(self.zapBoxMenu)
        self.titleRightInfo = QtWidgets.QLabel(parent=self.leftBox)
        self.titleRightInfo.setMaximumSize(QtCore.QSize(16777215, 40))
        self.titleRightInfo.setText("")
        self.titleRightInfo.setObjectName("titleRightInfo")
        self.horizontalLayout_7.addWidget(self.titleRightInfo)
        self.horizontalLayout_6.addWidget(self.leftBox)
        self.rightButtons = QtWidgets.QFrame(parent=self.headbar)
        self.rightButtons.setMinimumSize(QtCore.QSize(0, 28))
        self.rightButtons.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.rightButtons.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.rightButtons.setObjectName("rightButtons")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.rightButtons)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setSpacing(7)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.settingsTopBtn = QtWidgets.QPushButton(parent=self.rightButtons)
        self.settingsTopBtn.setMinimumSize(QtCore.QSize(25, 25))
        self.settingsTopBtn.setMaximumSize(QtCore.QSize(25, 25))
        self.settingsTopBtn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.settingsTopBtn.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.settingsTopBtn.setText("")
        self.settingsTopBtn.setAutoDefault(False)
        self.settingsTopBtn.setDefault(False)
        self.settingsTopBtn.setObjectName("settingsTopBtn")
        self.horizontalLayout_8.addWidget(self.settingsTopBtn)
        self.minimizeAppBtn = QtWidgets.QPushButton(parent=self.rightButtons)
        self.minimizeAppBtn.setMinimumSize(QtCore.QSize(25, 25))
        self.minimizeAppBtn.setMaximumSize(QtCore.QSize(25, 25))
        self.minimizeAppBtn.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.minimizeAppBtn.setText("")
        self.minimizeAppBtn.setDefault(False)
        self.minimizeAppBtn.setObjectName("minimizeAppBtn")
        self.horizontalLayout_8.addWidget(self.minimizeAppBtn)
        self.maximizeAppBtn = QtWidgets.QPushButton(parent=self.rightButtons)
        self.maximizeAppBtn.setMinimumSize(QtCore.QSize(25, 25))
        self.maximizeAppBtn.setMaximumSize(QtCore.QSize(25, 25))
        self.maximizeAppBtn.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.maximizeAppBtn.setText("")
        self.maximizeAppBtn.setObjectName("maximizeAppBtn")
        self.horizontalLayout_8.addWidget(self.maximizeAppBtn)
        self.closeAppBtn = QtWidgets.QPushButton(parent=self.rightButtons)
        self.closeAppBtn.setMinimumSize(QtCore.QSize(25, 25))
        self.closeAppBtn.setMaximumSize(QtCore.QSize(25, 25))
        self.closeAppBtn.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.closeAppBtn.setText("")
        self.closeAppBtn.setObjectName("closeAppBtn")
        self.horizontalLayout_8.addWidget(self.closeAppBtn)
        self.horizontalLayout_6.addWidget(self.rightButtons)
        self.verticalLayout.addWidget(self.headbar)
        self.main_stacked = QtWidgets.QStackedWidget(parent=self.app)
        self.main_stacked.setObjectName("main_stacked")
        self.verticalLayout.addWidget(self.main_stacked)
        self.verticalLayout_2.addWidget(self.app)
        MainWindow.setCentralWidget(self.appMargins)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 28))
        self.menubar.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.menubar.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.menubar.setDefaultUp(False)
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(parent=self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuView = QtWidgets.QMenu(parent=self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuHelp = QtWidgets.QMenu(parent=self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuChat = QtWidgets.QMenu(parent=self.menubar)
        self.menuChat.setObjectName("menuChat")
        MainWindow.setMenuBar(self.menubar)
        self.actionSettings = QtGui.QAction(parent=MainWindow)
        self.actionSettings.setShortcut("Ctrl+P")
        self.actionSettings.setObjectName("actionSettings")
        self.actionQuit = QtGui.QAction(parent=MainWindow)
        self.actionQuit.setShortcut("Ctrl+Q")
        self.actionQuit.setObjectName("actionQuit")
        self.actionReload_Service = QtGui.QAction(parent=MainWindow)
        self.actionReload_Service.setShortcut("F5")
        self.actionReload_Service.setObjectName("actionReload_Service")
        self.actionDefault_size_page = QtGui.QAction(parent=MainWindow)
        self.actionDefault_size_page.setShortcut("Ctrl+0")
        self.actionDefault_size_page.setObjectName("actionDefault_size_page")
        self.actionToggle_Full_Screen = QtGui.QAction(parent=MainWindow)
        self.actionToggle_Full_Screen.setShortcut("F11")
        self.actionToggle_Full_Screen.setObjectName("actionToggle_Full_Screen")
        self.actionAuto_hide_menu_bar = QtGui.QAction(parent=MainWindow)
        self.actionAuto_hide_menu_bar.setCheckable(False)
        self.actionAuto_hide_menu_bar.setShortcut("Ctrl+M")
        self.actionAuto_hide_menu_bar.setObjectName("actionAuto_hide_menu_bar")
        self.actionLearn_More = QtGui.QAction(parent=MainWindow)
        self.actionLearn_More.setShortcut("")
        self.actionLearn_More.setObjectName("actionLearn_More")
        self.actionChangelog = QtGui.QAction(parent=MainWindow)
        self.actionChangelog.setShortcut("")
        self.actionChangelog.setObjectName("actionChangelog")
        self.actionSupport = QtGui.QAction(parent=MainWindow)
        self.actionSupport.setShortcut("")
        self.actionSupport.setObjectName("actionSupport")
        self.actionAbout_Zapzap = QtGui.QAction(parent=MainWindow)
        self.actionAbout_Zapzap.setShortcut("")
        self.actionAbout_Zapzap.setObjectName("actionAbout_Zapzap")
        self.actionHide_on_close = QtGui.QAction(parent=MainWindow)
        self.actionHide_on_close.setCheckable(True)
        self.actionHide_on_close.setChecked(True)
        self.actionHide_on_close.setStatusTip("")
        self.actionHide_on_close.setObjectName("actionHide_on_close")
        self.actionZoomIn = QtGui.QAction(parent=MainWindow)
        self.actionZoomIn.setShortcut("Ctrl++")
        self.actionZoomIn.setObjectName("actionZoomIn")
        self.actionZoomOut = QtGui.QAction(parent=MainWindow)
        self.actionZoomOut.setShortcut("Ctrl+-")
        self.actionZoomOut.setObjectName("actionZoomOut")
        self.actionDonations = QtGui.QAction(parent=MainWindow)
        self.actionDonations.setShortcut("")
        self.actionDonations.setObjectName("actionDonations")
        self.actionHome_page = QtGui.QAction(parent=MainWindow)
        self.actionHome_page.setShortcut("Esc")
        self.actionHome_page.setObjectName("actionHome_page")
        self.actionOpen_new_chat = QtGui.QAction(parent=MainWindow)
        self.actionOpen_new_chat.setShortcut("Ctrl+N")
        self.actionOpen_new_chat.setObjectName("actionOpen_new_chat")
        self.menuFile.addAction(self.actionSettings)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionDonations)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionHide_on_close)
        self.menuFile.addAction(self.actionQuit)
        self.menuView.addAction(self.actionReload_Service)
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionDefault_size_page)
        self.menuView.addAction(self.actionZoomIn)
        self.menuView.addAction(self.actionZoomOut)
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionToggle_Full_Screen)
        self.menuView.addAction(self.actionAuto_hide_menu_bar)
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionHome_page)
        self.menuHelp.addAction(self.actionLearn_More)
        self.menuHelp.addAction(self.actionChangelog)
        self.menuHelp.addAction(self.actionSupport)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionAbout_Zapzap)
        self.menuChat.addAction(self.actionOpen_new_chat)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuChat.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.main_stacked.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        
        MainWindow.setWindowTitle(_("ZapZap"))
        self.zFile.setText(_("File"))
        self.zView.setText(_("View"))
        self.zChat.setText(_("Chat"))
        self.zHelp.setText(_("Help"))
        self.menuFile.setTitle(_("File"))
        self.menuView.setTitle(_("View"))
        self.menuHelp.setTitle(_("Help"))
        self.menuChat.setTitle(_("Chat"))
        self.actionSettings.setText(_("Settings"))
        self.actionQuit.setText(_("Quit"))
        self.actionReload_Service.setText(_("Reload"))
        self.actionDefault_size_page.setText(_("Default size page"))
        self.actionToggle_Full_Screen.setText(_("Full Screen"))
        self.actionAuto_hide_menu_bar.setText(_("Hide menu bar"))
        self.actionLearn_More.setText(_("Learn More"))
        self.actionChangelog.setText(_("Changelog"))
        self.actionSupport.setText(_("Report issue..."))
        self.actionAbout_Zapzap.setText(_("About Zapzap"))
        self.actionHide_on_close.setText(_("Hide on close"))
        self.actionHide_on_close.setToolTip(_("Keep in background when closing window"))
        self.actionZoomIn.setText(_("Zoom in"))
        self.actionZoomOut.setText(_("Zoom out"))
        self.actionDonations.setText(_("Donations"))
        self.actionHome_page.setText(_("Home page"))
        self.actionOpen_new_chat.setText(_("Open new chat"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())