from PIL import Image

img = Image.open("spirit_original.jpg")
imgGray = img.convert("L")
imgGray.save("spirit_gris.jpg")