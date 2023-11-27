from PyQt6.QtWidgets import QWidget
from zapzap.view.account_page import Ui_Account
import zapzap


class Account(QWidget, Ui_Account):
    def __init__(self):
        super(Account, self).__init__()
        self.setupUi(self)
