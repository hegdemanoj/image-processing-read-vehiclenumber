from PIL import Image
import pytesseract

text = pytesseract.image_to_string(Image.open('i1.jpeg'),lang='eng')
print(text)