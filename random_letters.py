import string
import random

try:
    while True:
            a=list(string.ascii_lowercase)
            random.shuffle(a)
            for i in a:
                input(f"letra {i}\t")
except KeyboardInterrupt:
    pass
        
