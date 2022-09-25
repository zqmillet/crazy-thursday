from scripts.get_issues import get_issues

def test_get_issues_with_fastapi(auth):
    """
    - get all issue from fastapi.
    - assert that the issue is empty.
    """

    issues = list(get_issues('tiangolo', 'fastapi', auth=auth))
    assert not issues

def test_get_issues_with_crazy_thursday(auth):
    """
    - get all issue from crazy_thursday.
    - assert that the issue is not empty.
    """

    issues = list(get_issues('zqmillet', 'crazy-thursday', auth=auth))
    assert issues
