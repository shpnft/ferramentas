from random import shuffle
import re

def print_problems(listas):
    from string import ascii_lowercase
    problemas=[]
    for i,lista in zip(ascii_lowercase, listas):
        temp = [f"{i}-{l.strip()}" for l in re.split(",| e ",lista)]
        problemas = problemas + temp
    shuffle(problemas)
    for problema in problemas:
        print(problema)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("listas", nargs='*')
    args = parser.parse_args()

    print_problems(args.listas)
    # se ao invés de colocar as listas na linha de comando for 
    # preferível fornecê-las como "linhas" use
    # cat << end| xargs -d "\n" python prob_shuff.py


