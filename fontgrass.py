# 맨 앞에 grass를 위한 클래스 만들기
from pico2d import load_image

class FrontGrass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

    def update(self):
        pass

    