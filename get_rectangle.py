import matplotlib.pyplot as plt
from matplotlib.widgets import RectangleSelector
import argparse

def onselect(eclick,erelease,xmax,ymax):
    print(f"""
        \\coordinate (X0) at ($(A.south west)!{eclick.xdata/xmax:.2f}!(A.south east)$);
        \\coordinate (X1) at ($(A.south west)!{erelease.xdata/xmax:.2f}!(A.south east)$);
        \\coordinate (Y0) at ($(A.north west)!{eclick.ydata/ymax:.2f}!(A.south west)$);
        \\coordinate (Y1) at ($(A.north west)!{erelease.ydata/ymax:.2f}!(A.south west)$);
        \\draw<2-> [red] (X0|-Y0) rectangle (X1|-Y1);
        """)

parser = argparse.ArgumentParser()
parser.add_argument("imagem")
parser.parse_args()
args = parser.parse_args()

img = plt.imread(args.imagem)
ymax, xmax = img.shape[:2]

fig, ax = plt.subplots()
ax.imshow(img)

rect_selector = RectangleSelector(ax,lambda x,y: onselect(x,y,xmax,ymax))

plt.show()

