from pathlib import Path
from random import shuffle
import argparse
from subprocess import run

def accept(f, size_gt, size_lt ):
    EXTENSIONS = {
            ".mp4",
            ".mkv",
            ".wmv",
            ".avi",
            ".webm",
            ".mts",
            ".mov",
            ".mpg",
            ".m4v",
            ".mpeg",
            ".asf",
            ".3gp",
            }

    if not f.exists(): return False
    if not f.is_file(): return False
    if not f.suffix.lower() in EXTENSIONS: return False
    if size_gt is not None and f.stat().st_size < size_gt: return False
    if size_lt is not None and f.stat().st_size > size_lt: return False

    return True

parser = argparse.ArgumentParser()
parser.add_argument("folder")
parser.add_argument("--size-lt", type=float)
parser.add_argument("--size-gt", type=float)
parser.parse_args()
args = parser.parse_args()

SEARCH_DIR = Path(args.folder)

files = [f for f in SEARCH_DIR.glob("**/*") if accept(f, args.size_gt, args.size_lt)]
print("{} files found.".format(len(files)))
shuffle(files)

run(["mplayer", "-vo", "xv", "-really-quiet", "-use-filename-title"] + files)
