"""
this script is used to download corpus from issues.
"""

from argparse import ArgumentParser
from os.path import dirname
from os.path import join
from datetime import datetime
from logging import DEBUG
from logging import info
from logging import basicConfig
from pytz import timezone

from scripts.get_issues import get_issues

from crazy_thursday import VERSION

basicConfig(level=DEBUG)

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

issues = list(get_issues(owner=arguments.owner, repository=arguments.repository))
print(f'there are {len(issues)} articles')

with open(arguments.output_file_path, 'w', encoding='utf8') as file:
    file.writelines([issue.json(ensure_ascii=False) + '\n' for issue in issues])

year, month, day, build = VERSION
now = datetime.now(timezone('Asia/Shanghai'))
info('now is %s', now)
today = now.date()
publish_date = datetime(year, month, day).date()

if today > publish_date:
    build *= 0
else:
    build += 1

with open(join(dirname(dirname(__file__)), 'crazy_thursday', '__init__.py'), 'w', encoding='utf8') as file:
    file.write(f'VERSION = ({today.year}, {today.month}, {today.day}, {build})')

info(f'new version is {today.year}.{today.month}.{today.day}.{build}')
