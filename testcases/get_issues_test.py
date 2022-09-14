from pytest import raises

from crazy_thursday.get_issues import get_issues
from crazy_thursday.get_issues import NotFoundException

def test_get_issues_with_404():
    with raises(NotFoundException):
        get_issues('gouliguojiashengsiyi_qinyinhuofubiquzhi', 'weixiaodegongzuo')

def test_get_issues_with_fastapi(auth):
    issues = list(get_issues('tiangolo', 'fastapi', auth=auth))
    import pdb; pdb.set_trace()
