from Facade import *


def CalibreCropping(filename):
    lol = Facade(filename)
    lol.img_editor.crop(crop_params)
    cv2.imshow("lol", lol.img_editor.img)
    cv2.waitKey()


# CalibreCropping("misha1.jpg")

lol1 = Facade("misha1.jpg")
# lol2 = Facade("v-26.jpg")

lol1.write_finger_scan("lol81.jpg")
# lol2.write_finger_scan("lol73.jpg")

# print(CompareFingerScans(lol1, lol2))
