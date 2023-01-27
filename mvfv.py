from pathlib import Path
from random import shuffle
import argparse
from subprocess import run

def accept(f, min_size, max_size):
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
    if min_size is not None and f.stat().st_size < min_size: return False
    if max_size is not None and f.stat().st_size > max_size: return False

    return True

parser = argparse.ArgumentParser()
parser.add_argument("folder")
parser.add_argument("--max-size", type=float)
parser.add_argument("--min-size", type=float)
args = parser.parse_args()

SEARCH_DIR = Path(args.folder)

files = [f for f in SEARCH_DIR.glob("**/*") if accept(f, args.min_size, args.max_size)]
print("{} files found.".format(len(files)))
shuffle(files)

run(["mplayer", "-vo", "xv", "-really-quiet", "-use-filename-title"] + files)
