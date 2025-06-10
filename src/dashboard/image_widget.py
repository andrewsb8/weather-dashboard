from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PyQt5.QtSvg import QSvgWidget


class ImageWidget(QLabel):
    def __init__(self, image_path, size=None, svg=False):
        super().__init__()
        self.image_path = image_path
        self.size = size
        if svg:
            self.svg_image()
        else:
            self.image()

    def svg_image(self):
        self.svgmap = QSvgWidget(self.image_path)
        if self.size:
            self.svgmap.setFixedSize(200, 200)

    def image(self):
        self.pixmap = QPixmap(self.image_path)
        if self.size:
            self.pixmap = self.pixmap.scaled(self.size[0], self.size[1])
        self.setPixmap(self.pixmap)
        self.setAlignment(Qt.AlignCenter)
