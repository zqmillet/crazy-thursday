from typing import List
from typing import Optional
from http import HTTPStatus
from enum import Enum
from tqdm import tqdm
from time import sleep

from pydantic import BaseModel
from pydantic import Field
from requests import Session

class NotFoundException(Exception):
    def __init__(self, owner, repository):
        super().__init__(f'cannot find the repository {owner}/{repository}')

class IssueState(Enum):
    CLOSE = 'closed'
    OPEN = 'open'

class Issue(BaseModel):
    title: str
    body: Optional[str]
    number: int
    state: IssueState

def get_issues(owner, repository, page_index=1, waiting_time=1, auth=None):
    session = Session()
    session.auth = auth

    url = f'https://api.github.com/repos/{owner}/{repository}/issues'

    page_index = 1
    progress_bar = tqdm(total=0)

    while True:
        parameters = {'per_page': 100, 'page': page_index, 'state': ['all']}
        response = session.get(url, params=parameters)

        if response.status_code == HTTPStatus.NOT_FOUND:
            raise NotFoundException(owner, repository)

        if response.status_code == HTTPStatus.FORBIDDEN:
            print(f'api rate limit exceeded, waiting {waiting_time}s', response.text)
            sleep(waiting_time)
            waiting_time *= 2
            continue

        waiting_time = 1

        if not response.status_code == HTTPStatus.OK:
            break

        delta_issues = [Issue(**item) for item in response.json()]
        if not delta_issues:
            print('exit on', page_index)
            break

        maximum_number = max(item.number for item in delta_issues)
        minimum_number = max(item.number for item in delta_issues)

        progress_bar.total = max(progress_bar.total, maximum_number)

        progress_bar.update(progress_bar.total - minimum_number - progress_bar.n)

        yield from delta_issues
        page_index += 1
