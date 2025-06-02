from textual.widget import Widget
from rich_pixels import Pixels
from PIL import Image


class ImageWidget(Widget):
    def __init__(self, image_path: str):
        super().__init__()
        img = Image.open("images/winter-images/1.jpg").resize((30, 30))
        self.pixels = Pixels.from_image(img)

    def render(self):
        return self.pixels
