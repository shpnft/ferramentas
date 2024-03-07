from pathlib import Path
from PIL import Image
import sys

# noremap <leader>a yiB :execute '! python ~/Documentos/devel/tools/latex_image.py ' . shellescape(@",1) <CR>
q = Path(sys.argv[1])
if not q.exists():
    q=list(Path().glob(sys.argv[1]+"*"))[0]

with Image.open(q) as im:
    width, height = im.size
    print(f'{width/height:.2f}')
