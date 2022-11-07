import unittest

from main import is_prime


class PrimesTestCase(unittest.TestCase):
    """Tests for `primes.py`."""

    def test_is_prime(self):
        self.assertTrue(is_prime(7))


if __name__ == '_main_':
    unittest.main()

