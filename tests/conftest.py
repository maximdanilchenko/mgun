import pytest

from mgun import HttpClient, HttpClientGroup


@pytest.fixture(params=[
    'one',
    'first',
    'second'
])
def client(request):
    if request.param == 'one':
        return HttpClient('https://httpbin.org')
    client_group = HttpClientGroup(
        ('first', 'https://httpbin.org'),
        ('second', 'https://httpbin.org', ('my-header', 'something')),
    )
    return client_group.first if request.param == 'first' else client_group.second
