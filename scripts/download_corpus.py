"""
this script is used to download corpus from issues.
"""

from argparse import ArgumentParser
from os.path import dirname
from os.path import join
from datetime import datetime
from subprocess import call

from crazy_thursday.get_issues import get_issues
from crazy_thursday import VERSION

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

argument_parser.add_argument(
    '--username',
    action='store',
    type=str,
    required=True,
    help='specify the github username'
)

argument_parser.add_argument(
    '--token',
    action='store',
    type=str,
    required=True,
    help='specify the github token'
)

arguments = argument_parser.parse_args()

with open(arguments.output_file_path, 'w', encoding='utf8') as file:
    for issue in get_issues(owner=arguments.owner, repository=arguments.repository):
        file.write(issue.json(ensure_ascii=False) + '\n')

year, month, day, build = VERSION
today = datetime.today().date()
publish_date = datetime(year, month, day).date()

if today == publish_date:
    build += 1
else:
    build = 0

with open(join(dirname(dirname(__file__)), 'crazy_thursday', '__init__.py'), 'w', encoding='utf8') as file:
    file.write(f'VERSION = ({year}, {month}, {day}, {build})')

call(['git', 'add', '.'])
call(['git', 'commit', '-m', 'add corpus'])
call(['git', 'remote', 'set-url', 'origin', f'https://{arguments.username}:{arguments.token}@github.com/zqmillet/crazy-thursday.git'])
call(['git', 'push', 'origin', 'master'])
