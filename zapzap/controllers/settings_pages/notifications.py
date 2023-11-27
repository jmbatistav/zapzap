from PyQt6.QtWidgets import QWidget
from zapzap.view.notifications_page import Ui_Notifications
import zapzap


class Notifications(QWidget, Ui_Notifications):
    def __init__(self):
        super(Notifications, self).__init__()
        self.setupUi(self)
