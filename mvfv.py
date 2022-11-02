from pathlib import Path
from random import shuffle
import argparse
from subprocess import run

parser = argparse.ArgumentParser()
parser.add_argument("folder")
parser.add_argument("--size-lt", type=float)
parser.add_argument("--size-gt", type=float)
parser.parse_args()
args = parser.parse_args()

SEARCH_DIR = Path(args.folder)
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

accept = lambda f: f.exists() and f.is_file() and f.suffix.lower() in EXTENSIONS

if args.size_gt is not None:
    temp1 = accept
    accept = lambda f: temp1(f) and f.stat().st_size >= args.size_gt

if args.size_lt is not None:
    temp2 = accept
    accept = lambda f: temp2(f) and f.stat().st_size <= args.size_lt

files = [f for f in SEARCH_DIR.glob("**/*") if accept(f)]
print("{} files found.".format(len(files)))
shuffle(files)

run(["mplayer", "-vo", "xv", "-really-quiet", "-use-filename-title"] + files)
