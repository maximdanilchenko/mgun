====
mgun
====

.. image:: https://badge.fury.io/py/mgun.svg
    :target: https://pypi.python.org/pypi/mgun
.. image:: https://travis-ci.org/maximdanilchenko/mgun.svg
    :target: https://travis-ci.org/maximdanilchenko/mgun
.. image:: https://codecov.io/gh/maximdanilchenko/mgun/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/maximdanilchenko/mgun

HTTP REST Json Client based on requests with dynamic url building

Install
-------

::

    pip install mgun

Quickstart
----------

.. code-block:: python


    from mgun import HttpClient

    client = HttpClient('https://httpbin.org', headers={'Authorization': '123'})  # headers - optional

    resp = client.anything.api.users[23].address.get({'q': '12'})

    print(resp.status)  # 200
    print(resp.data['url'])  # https://httpbin.org/anything/api/users/23/address?q=12
    print(resp.data['headers']['Authorization'])  # 123


Queries in one session
----------------------

.. code-block:: python


    with client.session() as s:  # also possible: with client.s() as s:
        resp = s.anything.api.users.get({'limit': '10'})  # request in this session
        s.anything.api.users[23].post({'data': [1, 2, 3]})
        s.anything.api.users[23].patch({'name': 'alex'})

