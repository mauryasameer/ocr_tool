
  

# OCR web tool

  

  

In this project I have basically used the tessearact engine for the recognition of the text, the latest version of the tesseract is pretty proficient when it comes to the text classification, we can tweak it's various setting to get a better performace.

  

here is a working example

![Example](resources/example.gif)

  

## Getting Started

  
  

#### Install Tesseract 4 on Ubuntu

The exact commands used to install Tesseract 4 on Ubuntu will be different depending on whether you are using Ubuntu 18.04 or Ubuntu 17.04 and earlier.

  

To check your Ubuntu version you can use the lsb_release command:

  
  

```
$ lsb_release -a

```

```
No LSB modules are available.

Distributor ID: Ubuntu

Description: Ubuntu 18.04.1 LTS

Release: 18.04

Codename: bionic

```
For Ubuntu 18.04 users, Tesseract 4 is part of the main apt-get repository, making it super easy to install Tesseract via the following command:

  

`$ sudo apt install tesseract-ocr
`

If you’re using Ubuntu 14, 16, or 17 though, you’ll need a few extra commands due to dependency requirements.

  

The good news is that Alexander Pozdnyakov has created an Ubuntu PPA (Personal Package Archive) for Tesseract, which makes it super easy to install Tesseract 4 on older versions of Ubuntu.

  

Just add the alex-p/tesseract-ocr PPA repository to your system, update your package definitions, and then install Tesseract:

  
  

```
$ sudo add-apt-repository ppa:alex-p/tesseract-ocr

$ sudo apt-get update

$ sudo apt install tesseract-ocr

```

Assuming there are no errors, you should now have Tesseract 4 installed on your machine.

  

#### Install Tesseract 4 on macOS

Installing Tesseract on macOS is straightforward provided you have Homebrew, macOS’ “unofficial” package manager, installed on your system.

  

Just run the following command, making sure to specify the --HEAD switch, and Tesseract v4 will be installed on your Mac:

  

`
$ brew install tesseract --HEAD
`

If you already have Tesseract installed on your Mac, you’ll first want to unlink the original install:

  

`
$ brew unlink tesseract
`

And from there you can run the install command.

  
  

* I have used Google Colab for the training of the model as my laptop has weak configuration.

* I have used Resnet-34 as the main backend architecture and have done transfer learning on top of that.

* I am using FastAI as my deep learning framework which is a wrapper of Pytorch Library, for rapid development of my model.

  

### Prerequisites

  

  

For running the code you have to install the libraries I have mentioned in the requirements.txt

  

  

```
pip install -r requirements.txt

```
  
  

## Running the Application on Localhost

Run the following command

```
python app.py

```


the application will start running on localhost on port 5000

  

### Details

  

  

* pytesseract is the official wrapper of tesseract in python, there are different configuration present within the tessearact to tweak the performace.

* I understand that this is not from stractch implementation but given the time limitations I was not able to complete the training process so that's why I went with the tesseract.

* The tesseract can be retrained by following [this](https://tesseract-ocr.github.io/tessdoc/Training-Tesseract.html)

|oem  |value |
|--| --|
  |0 | Original Tesseract only.|
  |1 | Neural nets LSTM only.
  |2 | Tesseract + LSTM.
  |3 | Default, based on what is available.


|psm|value  |
|--|--|
  |0|  Orientation and script detection (OSD) only.
  |1|  Automatic page segmentation with OSD.
  |2 | Automatic page segmentation, but no OSD, or OCR. (not implemented)
|  3 | Fully automatic page segmentation, but no OSD. (Default)
|  4 | Assume a single column of text of variable sizes.
  |5 | Assume a single uniform block of vertically aligned text.
  |6 | Assume a single uniform block of text.
  |7 | Treat the image as a single text line.
  |8 | Treat the image as a single word.
  |9 | Treat the image as a single word in a circle.
  |10 | Treat the image as a single character.
  |11 | Sparse text. Find as much text as possible in no particular order.
  |12 | Sparse text with OSD.
  |13|  Raw line. Treat the image as a single text line,bypassing hacks that are Tesseract-specific.