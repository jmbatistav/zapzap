from PyQt6.QtWidgets import QWidget
from zapzap.view.about_page import Ui_About
import zapzap


class About(QWidget, Ui_About):
    def __init__(self):
        super(About, self).__init__()
        self.setupUi(self)
