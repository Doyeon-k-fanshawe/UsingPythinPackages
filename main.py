#imports always go at the top
from PIL import Image

background = Image.open("bg.jpg")
background.show()

from emoji import emojize

moj = emojize('Packages are :fire:')
print(moj)
