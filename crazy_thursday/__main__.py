from random import choice
from os.path import dirname
from os.path import join
from json import loads

with open(join(dirname(__file__), 'corpus.jsonl'), 'r', encoding='utf8') as file:
    lines = file.readlines()

def main():
    item = loads(choice(lines))
    print(item['body'] or item['title'])

if __name__ == '__main__':
    main()
