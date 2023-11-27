from PyQt6.QtWidgets import QWidget
from zapzap.view.donations_page import Ui_Donations
import zapzap


class Donations(QWidget, Ui_Donations):
    def __init__(self):
        super(Donations, self).__init__()
        self.setupUi(self)
