import base64
from PIL import Image
from io import BytesIO

with open("E:\Pictures\IMG_20220410_184839.jpg", "rb") as image_file:
    data = base64.b64encode(image_file.read())

print(data)
        
with open("E:\Pictures\encode_IMG_20220410_184839.txt", "w") as file:
    file.write(str(data))

im = Image.open(BytesIO(base64.b64decode(data)))
im.save('E:\Pictures\image1.png', 'PNG')