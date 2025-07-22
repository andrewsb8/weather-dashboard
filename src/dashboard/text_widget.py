from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QFont


class TextWidget(QLabel):
    def __init__(self, text: str, font: str, size: int):
        super().__init__(text)
        self.setFont(QFont(font, size))
