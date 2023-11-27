from PyQt6.QtWidgets import QWidget
from zapzap.view.general_page import Ui_General
import zapzap


class General(QWidget, Ui_General):
    def __init__(self):
        super(General, self).__init__()
        self.setupUi(self)
