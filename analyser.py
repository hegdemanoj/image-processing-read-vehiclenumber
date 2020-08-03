import cv2
import pytesseract
from PIL import Image
from pytesseract import image_to_string
import matplotlib.pyplot as plt

def read_text(image):
    print('--- Start recognize text from image ---')
    print(image_to_string(image,lang='eng'))
    # print(pytesseract.get_string(image))
    print("------ Done -------")

def canny(image):
    gray = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray,(5,5),0)
    canny = cv2.Canny(blur,50,150)
    return canny
# image=Image.open('image2.jpg')
# newImg=cv2.imread(r'image2.jpg')

img = cv2.imread('image2.jpg')
# read_text(canny)
# cv2.namedWindow('image',cv2.WINDOW_NORMAL)
# cv2.resizeWindow('image', 600,600)
# cv2.imshow('image',canny)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# canny=canny(img)
gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
blur = cv2.GaussianBlur(gray,(5,5),0)
ret3,th3 = cv2.threshold(blur,50,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
plt.imshow(th3)
plt.show()