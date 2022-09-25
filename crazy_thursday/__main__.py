from random import choice
from os.path import dirname
from os.path import join
from json import loads

from rich.console import Console
from rich.markdown import Markdown

with open(join(dirname(__file__), 'corpus.jsonl'), 'r', encoding='utf8') as file:
    lines = file.readlines()

def main() -> None:
    """
    this is the entry of this package.
    """
    item = loads(choice(lines))
    markdown = Markdown(f"{item['body']}\n\n- **create by**: {item['user']['name']}\n- **create at**: {item['created_at']}")
    Console().print(markdown)

if __name__ == '__main__':
    main()
