# -*- coding:utf-8 -*-
from PIL import Image
from PIC import PIC
import numpy as np

im = Image.open("./1.jpeg", mode="r")
im = im.convert(mode='L')
pim = im.load()

data = dict(
    width=im.size[0],
    heigh=im.size[1],
    data=pim
)

pic = PIC(data)
data = pic.k_means_fuc()


im.save('out.jpeg')

