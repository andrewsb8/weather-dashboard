from textual.widget import Widget
from rich_pixels import Pixels
from PIL import Image


class ImageWidget(Widget):
    def __init__(self, image_path: str, img_size: tuple=(-1,-1)):
        super().__init__()
        img = Image.open(image_path)
        if img_size != (-1,-1):
            img = img.resize(img_size)
        self.pixels = Pixels.from_image(img)

    def render(self):
        return self.pixels
