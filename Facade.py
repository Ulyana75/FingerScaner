from ImageEditor import *
from SpecialPointsFinder import *


class Facade:
    def __init__(self, image_name):
        self.img_name = image_name
        self.img_editor = ImageEditor(image_name)
        self.got_scan = False

    def get_finger_scan(self, need_to_show=True):   # Выводит изображение отпечатка на экран
        self.img_editor.get_finger_scan(need_to_show)
        self.got_scan = True

    def write_finger_scan(self, filename):   # Записывает отпечаток в файл
        if not self.got_scan:
            self.get_finger_scan(False)
        cv2.imwrite(filename, self.img_editor.img)

    def get_points(self):
        self.img_editor.make_skeleton()
        return SpecialPointsFinder.findSpecialPoint(self.img_editor.img)


def CompareFingerScans(s1: Facade, s2: Facade):
    if not s1.got_scan:
        s1.get_finger_scan(False)
    if not s2.got_scan:
        s2.get_finger_scan(False)
    c1 = s1.get_points()
    c2 = s2.get_points()
    k = SpecialPointsFinder.comparePoint(c1, c2)
    p = len(c1[0]) + len(c1[1])
    q = len(c2[0]) + len(c2[1])
    d = k[0]
    return d * d / (p * q) * 100
