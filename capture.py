import cv2
import pytesseract
from ocr_module import create_boxes

cap = cv2.VideoCapture(0)
read = 1
ocr = 0
while True:

    if read:
        _, img = cap.read()

    cv2.imshow('image',img)

    k = cv2.waitKey(1)

    if ocr:
        create_boxes(img)

    if k == ord('q'):
        break
    
    if k==ord('p'):
        read=not read

    if k==ord('o'):
        ocr = not ocr

cv2.destroyAllWindows()