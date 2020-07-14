from flask import Flask, render_template, request, send_file
import os
import cv2
import numpy as np
from PIL import Image
import json
import io
from werkzeug.utils import secure_filename
import base64
from ocr_module import create_boxes


app = Flask(__name__,template_folder=".")

@app.route("/")
def index():
    return render_template("index.html")

def show_img(frame):
    cv2.imshow('img',frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def image_processing(img):
    img = Image.fromarray(img.astype("uint8"))
    rawBytes = io.BytesIO()
    img.save(rawBytes, "PNG")
    rawBytes.seek(0)
    img_base64 = base64.b64encode(rawBytes.getvalue()).decode('ascii')
    mime = "image/png"
    uri = "data:%s;base64,%s"%(mime, img_base64)
    return uri,img_base64

def resize(img,size=720,interpolation=cv2.INTER_LINEAR):
    h,w = img.shape[:2]
    c = None if len(img.shape)< 3 else img.shape[2]
    if h>=w: return cv2.resize(img,(size,size),interpolation)
    if h> w: dif = h
    else:    dif = w
    x_pos = int((dif-w)/2.)
    y_pos = int((dif-h)/2.)

    if c is None:
        mask = np.zeros((dif,dif),dtype=img.dtype)
        mask[y_pos:y_pos+h, x_pos:x_pos+w] = img[:h, :w]
    else:
        mask = np.zeros((dif,dif,c),dtype=img.dtype)
        mask[y_pos:y_pos+h, x_pos:x_pos+w,:] = img[:h, :w, :]
    return cv2.resize(mask,(size,size),interpolation)

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
        f = request.files['file'].read()
        
        oem=request.form['OEM VALUES']
        psm=request.form['PSM VALUES']

        npimg = np.fromstring(f,np.uint8)
        img = cv2.imdecode(npimg,cv2.IMREAD_COLOR)
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        
        # T = int(request.form['selection'])
        
        text=set(request.form['selection'].lower().split(','))
        # print(text)
        img = resize(img)
        
        create_boxes(img,text,[psm,oem])
        # convering the image
        uri,_ = image_processing(img)
        return render_template("./template/output.html",image=uri)


if __name__ == '__main__':
    app.run(host='127.0.0.1',debug=True)

