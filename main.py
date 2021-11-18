from rich import print

print("Hello, [bold magenta]World[/bold magenta]!", ":vampire:", locals())


from PIL import Image

background = Image.open("bg.jpg")
background.show()


from emoji import emojize

moj = emojize('Packages are :fire:')
print(moj)

