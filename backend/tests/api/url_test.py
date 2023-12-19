import unittest
from fastapi.testclient import TestClient
from starlette.status import (
    HTTP_200_OK,
    HTTP_404_NOT_FOUND,
    HTTP_422_UNPROCESSABLE_ENTITY,
)
from tier_backend import main

BASE_URL = "http://0.0.0.0:80/"
DOMAIN = "tier.app"


class TestUrlEndpoints(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.init_app()
        cls.create_client()

    def test_default_route_returns_docs_message(self):
        expected_message = "See /docs for endpoint documentation"

        res = TestUrlEndpoints.client.get(BASE_URL)
        self.assertEqual(res.status_code, HTTP_200_OK)
        self.assertEqual(res.json().get("message"), expected_message)

    def test_post_get_urls_valid(self):
        expected_message = "youtu.be/QuoKNZjr8_U?t=23"
        urls = [
            "youtu.be/QuoKNZjr8_U?t=23",
            "www.youtu.be/QuoKNZjr8_U?t=23",
            "http://www.youtu.be/QuoKNZjr8_U?t=23",
            "https://www.youtu.be/QuoKNZjr8_U?t=23",
            "http://youtu.be/QuoKNZjr8_U?t=23",
            "https://youtu.be/QuoKNZjr8_U?t=23",
        ]
        expected_hash = None

        for i, url in enumerate(urls):
            res = TestUrlEndpoints.post(url=url)
            res_json = res.json()
            self.assertEqual(res.status_code, HTTP_200_OK)

            message = res_json.get("message")
            domain, hash = message.rsplit("/", 1)

            if i == 0:
                self.assertEqual(len(hash), 7)
                expected_hash = hash
            self.assertEqual(domain, DOMAIN)
            self.assertEqual(hash, expected_hash)

            res = TestUrlEndpoints.get(url=message)
            res_json = res.json()
            self.assertEqual(res.status_code, HTTP_200_OK)
            self.assertEqual(res_json.get("message"), expected_message)

    def test_post_invalid_url_raises_422(self):
        expected_message = "Invalid URL."
        url = "QuoKNZjr8_U?t=23"
        res = TestUrlEndpoints.post(url=url)
        self.assertEqual(res.status_code, HTTP_422_UNPROCESSABLE_ENTITY)
        self.assertEqual(res.json().get("detail"), expected_message)

    def test_get_invalid_url_raises_422(self):
        expected_message = "Invalid URL."
        url = "tier.app/123456"
        res = TestUrlEndpoints.get(url=url)
        self.assertEqual(res.status_code, HTTP_422_UNPROCESSABLE_ENTITY)
        self.assertEqual(res.json().get("detail"), expected_message)

    def test_get_missing_url_returns_404(self):
        expected_message = "URL does not exist."
        url = "tier.app/1234567"
        res = TestUrlEndpoints.get(url=url)
        self.assertEqual(res.status_code, HTTP_404_NOT_FOUND)
        self.assertEqual(res.json().get("detail"), expected_message)

    @classmethod
    def get(cls, url: str):
        return cls.client.get(
            f"{BASE_URL}decode_url",
            params={"url": url},
        )

    @classmethod
    def post(cls, url: str):
        return cls.client.post(
            f"{BASE_URL}encode_url",
            params={"url": url},
        )

    @classmethod
    def init_app(cls):
        cls.app = main.app

    @classmethod
    def create_client(cls):
        cls.client = TestClient(
            app=cls.app,
            base_url="http://0.0.0.0:80/",
        )


if __name__ == "__main__":
    unittest.main()
