from random import choice
from os.path import dirname
from os.path import join
from json import loads

from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel

with open(join(dirname(__file__), 'corpus.jsonl'), 'r', encoding='utf8') as file:
    lines = file.readlines()

def main() -> None:
    """
    this is the entry of this package.
    """
    item = loads(choice(lines))
    Console().print(
        Panel(
            renderable=Markdown(item['body'].strip()),
            subtitle=f"create by {item['user']['name']} at {item['created_at']}",
            subtitle_align='right',
        )
    )

if __name__ == '__main__':
    main()
