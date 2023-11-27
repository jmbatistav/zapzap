from PyQt6.QtWidgets import QWidget
from zapzap.view.personalization_page import Ui_Personalization
import zapzap


class Personalization(QWidget, Ui_Personalization):
    def __init__(self):
        super(Personalization, self).__init__()
        self.setupUi(self)
