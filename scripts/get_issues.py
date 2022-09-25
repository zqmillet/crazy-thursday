"""
this module provides the function get_issues.
"""

from typing import Optional
from typing import Union
from typing import Dict
from typing import Tuple
from typing import List
from typing import Generator
from http import HTTPStatus
from enum import Enum
from time import sleep
from datetime import datetime
from logging import Logger
from logging import getLogger

from pydantic import BaseModel
from pydantic import Field
from pydantic import validator
from requests import Session
from tqdm import tqdm

class IssueState(Enum):
    """
    this class is enumeration of issue state.
    """
    CLOSE = 'closed'
    OPEN = 'open'

class User(BaseModel):
    """
    this class is user of issue.
    """
    name: str = Field(alias='login')
    id: int

class Label(BaseModel):
    """
    this class is label of issue.
    """
    id: int
    name: str

class Issue(BaseModel):
    """
    this is the is class Issue.
    """
    title: str
    body: Optional[str]
    number: int
    state: IssueState
    created_at: datetime
    user: User
    labels: List[Label]

    @validator('body')
    def validate_body(cls, value: Optional[str]) -> Optional[str]: # pylint: disable = no-self-argument
        """
        this function is used to remote first second lines of body.
        """
        if not value:
            return None
        return '\n'.join(value.splitlines()[2:])

def get_issues(
    owner: str,
    repository: str,
    page_index: int = 1,
    waiting_time: int = 1,
    auth: Optional[Tuple[str, str]] = None,
    logger: Optional[Logger] = None
) -> Generator[Issue, None, None]:
    """
    this function is used to get all issue of the specified repository.
    """
    logger = logger or getLogger('dummy')
    url = f'https://api.github.com/repos/{owner}/{repository}/issues'
    session = Session()
    session.auth = auth

    progress_bar: tqdm = tqdm(total=0)

    while True:
        parameters: Dict[str, Union[int, str]] = {'per_page': 100, 'page': page_index, 'state': 'all'}
        response = session.get(url, params=parameters)

        if response.status_code == HTTPStatus.FORBIDDEN:
            logger.warning('api rate limit exceeded, waiting %d seconds', waiting_time)
            sleep(waiting_time)
            waiting_time *= 2
            continue

        waiting_time = 1

        if not response.status_code == HTTPStatus.OK:
            logger.warning('there are something wrong when call the api, the response is %s', response.text)
            break

        delta_issues = [Issue(**item) for item in response.json()]
        if not delta_issues:
            break

        maximum_number = max(item.number for item in delta_issues)
        minimum_number = max(item.number for item in delta_issues)

        progress_bar.total = max(progress_bar.total, maximum_number) # type: ignore
        progress_bar.update(progress_bar.total - minimum_number - progress_bar.n) # type: ignore

        for issue in delta_issues:
            if 'add article' not in [label.name for label in issue.labels]:
                continue
            yield issue

        page_index += 1
