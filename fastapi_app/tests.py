from unittest import TestCase

from main import home

## TODO: Add more test

class TestCRUD(TestCase):
    def test_home(self):
        self.assertEqual(home(), {"message":"Hello world!"})