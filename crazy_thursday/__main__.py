from random import choice
from os.path import dirname
from os.path import join
from os import get_terminal_size
from json import loads

columns = get_terminal_size().columns

with open(join(dirname(__file__), 'corpus.jsonl'), 'r', encoding='utf8') as file:
    lines = file.readlines()

def main():
    """
    this is the entry of this package.
    """
    item = loads(choice(lines))
    print(item['body'] or item['title'])
    print(('by ' + item['user']['name']).rjust(columns))
    print(('at ' + item['created_at']).rjust(columns))

if __name__ == '__main__':
    main()
