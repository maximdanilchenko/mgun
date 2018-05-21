import json


class TestUrlBuilder:
    def test_url(self, client):
        assert client.__str__() == 'https://httpbin.org'

    def test_simple_url(self, client):
        assert client.api.__str__() == 'https://httpbin.org/api'

    def test_parameter_url(self, client):
        assert client.api.users[34].first.__str__() == 'https://httpbin.org/api/users/34/first'

    def test_str_parameters_url(self, client):
        assert client['api'].users['f3d4a'].first.__str__() == 'https://httpbin.org/api/users/f3d4a/first'


class TestHttpRequests:
    def test_get(self, client):
        response = client.get_.get()
        assert response.status == 200

    def test_delete(self, client):
        response = client.delete_.delete()
        assert response.status == 200

    def test_get_with_data(self, client):
        data = {'q': '1'}
        response = client.get_.get(data)
        assert response.status == 200
        assert response.data['args'] == data

    def test_post(self, client):
        data = {'data': [1, 2, 3]}
        response = client.post_.post(data)
        assert response.status == 200
        assert json.loads(response.data['data']) == data
        print(response)

    def test_put(self, client):
        data = {'data': [1, 2, 3]}
        response = client.put_.put(data)
        assert response.status == 200
        assert json.loads(response.data['data']) == data
        print(response)

    def test_patch(self, client):
        data = {'data': [1, 2, 3]}
        response = client.patch_.patch(data)
        assert response.status == 200
        assert json.loads(response.data['data']) == data
        print(response)

    def test_session(self, client):
        with client.session() as s:
            response = s.get_.get()
        assert response.status == 200

    def test_s(self, client):
        with client.s() as s:
            response = s.get_.get()
        assert response.status == 200
