====
mgun
====

.. image:: https://badge.fury.io/py/mgun.svg
    :target: https://pypi.python.org/pypi/mgun
.. image:: https://travis-ci.org/maximdanilchenko/mgun.svg
    :target: https://travis-ci.org/maximdanilchenko/mgun
.. image:: https://codecov.io/gh/maximdanilchenko/mgun/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/maximdanilchenko/mgun

HTTP REST Client based on requests with dynamic url building

Install
-------

::

    pip install mgun

Quickstart
----------

.. code-block:: python


    from mgun import HttpClient

    client = HttpClient('https://httpbin.org')

    resp = client.anything.api.users[23].address.get({'q': '12'})

    print(resp.status)  # 200
    print(resp.data['url'])  # https://httpbin.org/anything/api/users/23/address?q=12


