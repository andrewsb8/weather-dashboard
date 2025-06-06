from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PIL import Image


class ImageWidget(QLabel):
    def __init__(self, image_path, size=None, parent=None):
        super().__init__(parent)
        pixmap = QPixmap(image_path)
        if size:
            pixmap = pixmap.scaled(size[0], size[1])
        self.setPixmap(pixmap)
        self.setAlignment(Qt.AlignCenter)
