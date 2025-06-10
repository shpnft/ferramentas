import matplotlib.pyplot as plt
import argparse

def onClick(event):
    if event.xdata is None:
        return
    if event.ydata is None:
        return
    print(event.xdata, event.ydata)

parser = argparse.ArgumentParser()
parser.add_argument("imagem")
parser.parse_args()
args = parser.parse_args()

img = plt.imread(args.imagem)

fig, ax = plt.subplots()
ax.imshow(img)

fig.canvas.mpl_connect('button_press_event', onClick)

plt.show()

