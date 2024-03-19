from unittest import TestCase

from main import home

class TestCRUD(TestCase):
    def test_home(self):
        self.assertEqual(home(), {"message":"Hello world!"})