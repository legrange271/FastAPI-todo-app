from unittest import TestCase

from fastapi.testclient import TestClient

from main import app
from modules.apis.frontend import home
from modules.apis.items_crud_api import get_items, get_item, add_item

from modules.models.models import items, Item


class TestFrontend(TestCase):
    def test_home(self):
        self.assertEqual(home(), {"message":"Hello world!"})


class TestCRUD(TestCase):
    def setUp(self):
        self.client = TestClient(app)
        items.clear()

    def tearDown(self):
        items.clear()

    def test_get_items(self):
        items[1] = Item(name="Test 1")

        response = self.client.get("api/items")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"Items": {"1":{"name": "Test 1", "checked":None}}})
    