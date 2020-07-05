import cv2
import pytesseract
from ocr_module import create_boxes
PATH = 't.jpg'

img = cv2.imread(PATH)
img = cv2.resize(img,(500,500))

cv2.imshow('orig',img)


create_boxes(img)


cv2.imshow('box',img)

cv2.waitKey(0)

cv2.destroyAllWindows()