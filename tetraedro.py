#https://stackoverflow.com/a/57319639/20287521
import matplotlib.pyplot as plt
import argparse
import string

def onClick (event):
    if event.xdata is None:
        return
    if event.ydata is None:
        return
    try:
        onClick.p.append((event.xdata, event.ydata))
    except AttributeError:
        onClick.p=[(event.xdata, event.ydata)]

    print(len(onClick.p))

parser = argparse.ArgumentParser()
parser.add_argument("imagem")
parser.add_argument("letra")
parser.parse_args()
args = parser.parse_args()

img = plt.imread(args.imagem)
ax = plt.imshow(img)
fig = ax.get_figure()

cid = fig.canvas.mpl_connect('button_press_event', onClick)
plt.show()

xmax, ymax = img.shape[:2]
try:
    ql = len(onClick.p)
except AttributeError:
    ql=0

q0=string.ascii_uppercase.find(args.letra)
ql=ql+q0

for l in string.ascii_uppercase[q0:ql]:
    x,y=onClick.p.pop(0)
    x=x*10/max(xmax,ymax)
    y=(ymax-y)*10/max(xmax,ymax)

    print(f"\\coordinate ({l}) at ({x:.2f},{y:.2f});")
