from gettext import gettext as _
# Form implementation generated from reading ui file './zapzap/view/ui/account_page.ui'
#
# Created by: PyQt6 UI code generator 6.6.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Account(object):
    def setupUi(self, Account):
        Account.setObjectName("Account")
        Account.resize(400, 300)

        self.retranslateUi(Account)
        QtCore.QMetaObject.connectSlotsByName(Account)

    def retranslateUi(self, Account):
        
        Account.setWindowTitle(_("Form"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Account = QtWidgets.QWidget()
    ui = Ui_Account()
    ui.setupUi(Account)
    Account.show()
    sys.exit(app.exec())