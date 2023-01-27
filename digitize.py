import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("image_file")
args = parser.parse_args()

img = mpimg.imread(args.image_file)
imgplot = plt.imshow(img)
dados = plt.ginput(n=0, timeout=30)

xmax,ymax = img.shape[:2]
maior = max(xmax,ymax)/10
for x,y in [(x/maior,(ymax-y)/maior) for x,y in dados]:
    print(f"{x:.2f}\t{y:.2f}")
