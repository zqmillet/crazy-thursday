"""
this script is used to download corpus from issues.
"""

from argparse import ArgumentParser
from os.path import dirname
from os.path import join

from crazy_thursday.get_issues import get_issues

argument_parser = ArgumentParser()

argument_parser.add_argument(
    '--owner',
    action='store',
    type=str,
    default='zqmillet',
    help='specify the owner of repository'
)

argument_parser.add_argument(
    '--repository',
    action='store',
    type=str,
    default='crazy-thursday',
    help='specify the name of repository'
)

argument_parser.add_argument(
    '--output-file-path',
    action='store',
    type=str,
    default=join(dirname(dirname(__file__)), 'crazy_thursday', 'corpus.jsonl'),
    help='specify the output file path'
)

arguments = argument_parser.parse_args()

with open(arguments.output_file_path, 'w', encoding='utf8') as file:
    for issue in get_issues(owner=arguments.owner, repository=arguments.repository):
        file.write(issue.json(ensure_ascii=False) + '\n')
