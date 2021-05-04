from PIL import Image
import cv2
import numpy as np

im = Image.open("venv/chemistry_recognition/乙烯//2.png").convert('L')
im.show()
mat = np.asarray(im)
ret2, th_1 = cv2.threshold(mat, 0, 225, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imshow('BINARY',th_1)
cv2.waitKey()