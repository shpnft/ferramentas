from pathlib import Path
from PIL import Image
import sys

# noremap <leader>a yiB :execute '! python ~/Documentos/devel/tools/latex_image.py ' . shellescape(@",1) <CR>
q=next(Path().glob(sys.argv[1]+"*"))

with Image.open(q) as im:
    width, height = im.size
    print(f'{width/height:.2f}')
