import matplotlib.pyplot as plt
import argparse

def onClick (event):
    if event.xdata is None:
        return
    if event.ydata is None:
        return
    try:
        onClick.p.append((event.xdata, event.ydata))
    except AttributeError:
        onClick.p=[(event.xdata, event.ydata)]

parser = argparse.ArgumentParser()
parser.add_argument("imagem")
parser.parse_args()
args = parser.parse_args()

img = plt.imread(args.imagem)
xmax, ymax = img.shape[:2]

ax = plt.imshow(img,extent=[0,ymax,0,xmax])
fig = ax.get_figure()
fig.canvas.mpl_connect('button_press_event', onClick)
plt.show()

print(f"xmax: {xmax}, ymax: {ymax}")
try:
    for p in onClick.p:
        print(f"x: {p[0]:.2f}, y: {p[1]:.2f}")
except AttributeError:
    pass

