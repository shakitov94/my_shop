from django.test import TestCase, Client


class TestHomepage(TestCase):
    def test_open_homepage_should_be_success(self):
        c = Client()
        response = c.get('http://127.0.0.1:8000/')
        assert response.content
        assert response.status_code == 200

    def test_post_homepage_should_return_400(self):
        c = Client()
        response = c.post('http://127.0.0.1:8000/')
        assert response.status_code == 400, f'should be {response.status_code}'

