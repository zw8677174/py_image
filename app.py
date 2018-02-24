# -*- coding:utf-8 -*-
from PIL import Image
from PIC import PIC

im = Image.open("./1.jpeg", mode="r")
im = im.convert(mode='L')

out = im.getpixel((851, 1279))
print(im.size)

data = dict()
for i in range(im.size[0]):
    data[i] = dict()

for i in range(im.size[0]):
    for j in range(im.size[1]):
        data[i][j] = im.getpixel((i, j))

data = dict(
    width=im.size[0],
    heigh=im.size[1],
    data=data
)
print data
exit()

pic = PIC(data)

out = pic.get_point(x=850, y=1200)
print(out)

