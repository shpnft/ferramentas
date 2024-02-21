from PIL import Image
import sys

# noremap <leader>a yiB :execute '! python ~/Documentos/devel/tools/latex_image.py ' . shellescape(@",1) <CR>
with Image.open(sys.argv[1]) as im:
    width, height = im.size
    print(f'{width/height:.2f}')
