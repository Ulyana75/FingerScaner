import cv2
from TemplateDeleter import TemplateDeleter
from config import crop_params


class ImageEditor:
    def __init__(self, name):
        self.img = cv2.imread(name, 0)

    def crop(self, params):
        self.img = self.img[params[0]:params[1], params[2]:params[3]]

    def left_only_black_and_white(self):
        self.img = cv2.medianBlur(self.img, 5)
        self.img = cv2.adaptiveThreshold(self.img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 1)

    def get_finger_scan(self, need_to_show):
        self.crop(crop_params)
        self.left_only_black_and_white()
        if need_to_show:
            cv2.imshow("finger_scan", self.img)
            cv2.waitKey()

    def make_skeleton(self):   # Получаем скелет изображения (отпечаток с тоникми линиями)
        w, h = self.img.shape
        self.change_pixels()
        count = 1
        while count != 0:
            count = TemplateDeleter.delete(self.img, w, h)
            if count:
                TemplateDeleter.delete2(self.img, w, h)
        self.change_pixels_back()

    def change_pixels(self):   # В алгоритмах кдаления по шаблонам белый цвет обозначается за 1,
        a, b = self.img.shape  # поэтому сопоставляем всем белым пикселям 1
        for i in range(0, a):
            for j in range(0, b):
                if self.img[i][j] == 255:
                    self.img[i][j] = 1

    def change_pixels_back(self):   # Обратно меняем 1 на 255
        a, b = self.img.shape
        for i in range(0, a):
            for j in range(0, b):
                if self.img[i][j] == 1:
                    self.img[i][j] = 255
