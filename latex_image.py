from PIL import Image

with Image.open(sys.argv[1]) as im:
    width, height = im.size
    print(width/height)
