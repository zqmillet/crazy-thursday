from random import choice
from os.path import dirname
from os.path import join
from json import loads

with open(join(dirname(__file__), 'corpus.jsonl'), 'r', encoding='utf8') as file:
    lines = file.readlines()

def main():
    print(loads(choice(lines))['body'])

if __name__ == '__main__':
    main()
