from collections import namedtuple

import requests

METHOD_GET = 'GET'
METHOD_DELETE = 'DELETE'
METHOD_POST = 'POST'
METHOD_PUT = 'PUT'
METHOD_PATCH = 'PATCH'
CONTENT_TYPE = 'CONTENT-TYPE'
JSON_TYPE = 'application/json'

GET_METHODS = [METHOD_GET,
               METHOD_DELETE]

POST_METHODS = [METHOD_POST,
                METHOD_PUT,
                METHOD_PATCH]

ALL_METHODS = GET_METHODS + POST_METHODS

ALL_METHODS_LOWER = [method.lower() for method in ALL_METHODS]

__all__ = ['HttpClient',
           'HttpClientGroup',
           'METHOD_GET',
           'METHOD_DELETE',
           'METHOD_POST',
           'METHOD_PUT',
           'METHOD_PATCH']

ApiInfo = namedtuple('ApiInfo', ['url', 'headers'])
ApiResponse = namedtuple('ApiResponse', ['status', 'data'])


def format_path(path):
    return '{}'.format(path).strip('_')


def format_response(response):
    content_type = response.headers.get(CONTENT_TYPE, '').lower()
    if JSON_TYPE not in content_type:
        return ApiResponse(response.status_code, response.text)
    return ApiResponse(response.status_code, response.json())


class UrlBuilder:
    def __init__(self, http_client, url, headers, *args):
        self.base_url = url
        self.headers = headers
        self.http_client = http_client
        self.sub_url = [format_path(arg) for arg in args]

    def __getattr__(self, item):
        self.sub_url.append(format_path(item))
        return self

    __getitem__ = __getattr__

    def __str__(self):
        return '{}/{}'.format(self.base_url,
                              "/".join(self.sub_url)) if self.sub_url else self.base_url

    __repr__ = __str__

    def request(self, method, content=None, params=None, session=None, headers=None):
        if method not in ALL_METHODS:
            raise UnsupportedHttpMethod()
        if method in GET_METHODS and content:
            raise ContentInGet()
        return self._make_request(method=method,
                                  url=self.__str__(),
                                  content=content,
                                  params=params,
                                  session=session,
                                  headers=headers)

    def _make_request(self, session, method, url, content=None, params=None, headers=None):
        if session:
            response = session.request(method, url, params=params, json=content, headers=headers)
        else:
            response = requests.request(method, url, params=params, json=content, headers=headers)
        return format_response(response)

    def get(self, params=None, **kwargs):
        return self.request(method=METHOD_GET,
                            params=params,
                            **kwargs)

    def delete(self, params=None, **kwargs):
        return self.request(method=METHOD_DELETE,
                            params=params,
                            **kwargs)

    def post(self, content=None, **kwargs):
        return self.request(method=METHOD_POST,
                            content=content,
                            **kwargs)

    def put(self, content=None, **kwargs):
        return self.request(method=METHOD_PUT,
                            content=content,
                            **kwargs)

    def patch(self, content=None, **kwargs):
        return self.request(method=METHOD_PATCH,
                            content=content,
                            **kwargs)


class UnsupportedHttpMethod(Exception):
    pass


class ContentInGet(Exception):
    pass


class NoBaseUrl(Exception):
    pass


class HttpClient:
    def __init__(self, url, headers=None):
        self.url = url
        self.headers = headers

    s = session = requests.session

    def __str__(self):
        return self.url

    def __getattr__(self, name):
        if name in ALL_METHODS_LOWER:
            return getattr(UrlBuilder(self, self.url, self.headers), name)
        return UrlBuilder(self, self.url, self.headers, name)

    __getitem__ = __getattr__


class HttpClientGroup:
    def __init__(self, *rules):
        self.urls = {rule[0]: HttpClient(rule[1], dict(rule[2:]))
                     for rule in rules}

    def __getattr__(self, name):
        if name in self.urls:
            return self.urls.get(name)
        else:
            raise NoBaseUrl('{} is not in urls'.format(name))
