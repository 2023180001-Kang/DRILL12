# 맨 앞에 grass를 위한 클래스 만들기
from pico2d import load_image

class fontgrass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 10)

    def update(self):
        pass

    