from pytest import fixture

def pytest_addoption(parser):
    """
    this function is used to add some option of pytest.
    """
    parser.addoption(
        '--token',
        type=str,
        action='store',
        required=True,
    )

    parser.addoption(
        '--username',
        type=str,
        action='store',
        required=True
    )

@fixture(name='username', scope='session')
def _username(request):
    return request.config.getoption('username')

@fixture(name='token', scope='session')
def _token(request):
    return request.config.getoption('token')

@fixture(name='auth', scope='session')
def _auth(username, token):
    return (username, token)
