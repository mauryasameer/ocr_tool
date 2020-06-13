import pytesseract
import cv2
from pytesseract import Output

def create_boxes(frame):

    output = pytesseract.image_to_data(frame, output_type=Output.DICT)

    boxes_len = len(output['text'])

    for i in range(boxes_len):

        if int(output['conf'][i])>60:

            (x,y,w,h) = (output['left'][i],output['top'][i],output['width'][i],output['height'][i])
            frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)




