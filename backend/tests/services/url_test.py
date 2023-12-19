import unittest
from tier_backend.services.url import is_internal, get_clean_url, get_current_time_hash
from freezegun import freeze_time

SAMPLE_EXTERNAL_URL = "https://www.youtu.be/QuoKNZjr8_U?t=23"


class TestUrlService(unittest.TestCase):
    @freeze_time("2010-10-10")
    def test_get_current_time_hash_returns_hash(self):
        hash = get_current_time_hash()
        self.assertEqual(hash, "4f2yn52")

    def test_get_clean_url_internal_returns_url(self):
        clean_url = get_clean_url(
            url="https://www.tier.app/1234567", only_internal=True
        )
        self.assertEqual(clean_url, "tier.app/1234567")

    def test_get_clean_url_external_returns_url(self):
        clean_url = get_clean_url(url=SAMPLE_EXTERNAL_URL, only_internal=False)
        self.assertEqual(clean_url, "youtu.be/QuoKNZjr8_U?t=23")

    def test_get_clean_url_external_raises_value_error(self):
        with self.assertRaises(ValueError):
            get_clean_url(url=SAMPLE_EXTERNAL_URL, only_internal=True)

    def test_is_internal_returns_false(self):
        external_url = SAMPLE_EXTERNAL_URL
        self.assertFalse(is_internal(url=external_url))

    def test_is_internal_returns_true(self):
        internal_url = "tier.app/1234567"
        self.assertTrue(is_internal(url=internal_url))


if __name__ == "__main__":
    unittest.main()
