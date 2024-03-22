from unittest import TestCase
from unittest.mock import patch

from fastapi.testclient import TestClient

from main import app
from modules.apis.frontend import home

from modules.models.models import items, Item

from modules.utils.id_gen  import gen_unique_id


class TestFrontend(TestCase):
    def test_home(self):
        """Method to test correct response from home"""
        self.assertEqual(home(), {"message":"Hello world!"})


class TestCRUD(TestCase):

    def setUp(self):
        """Method to set up code for testing"""
        self.client = TestClient(app)
        items.clear()
        items["1"] = Item(name="Test 1")


    def tearDown(self):
        """Method to teardown after each test and start fresh"""
        items.clear()

    def test_get_items(self):
        """method for testing get items function returning right status and resposne"""
        response = self.client.get("api/items")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"Items": {"1":{"name": "Test 1", "checked":False}}})

    @patch('modules.apis.items_crud_api.gen_unique_id')
    def test_add_item_success(self, mock_uuid):
        """Method to test adding an item functionality"""
        mock_uuid.return_value = "2"
        response = self.client.post("api/items", json={"name": "Test 2"})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), {"id": "2", "name":"Test 2", "checked":False})
        self.assertEqual(items, {"1":Item(name="Test 1"), "2":Item(name="Test 2")})

    def test_get_item_exists(self):
        """test that the get item function works when item exists"""
        response = self.client.get("api/items/1")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"name": "Test 1", "checked":False})

        
    def test_get_item_doesnt_exists(self):
        """test that the get item function works when item doesnt exists"""
        response = self.client.get("api/items/2")
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json(), {"message": "ID not found"})

    def test_delete_item_success(self):
        """test deleting an item from the list"""
        response = self.client.delete("api/items/1")
        self.assertEqual(response.status_code, 204)
        self.assertEqual(items, {})

    def test_delete_item_fail(self):
        """test deleting an item from the list fialing"""
        response = self.client.delete("api/items/2")
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json(), {"message": "ID not found"})

    def test_update_item_success(self):
        """test whether checking an item works"""
        response = self.client.put("api/items/1", json={"checked": True})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), {"id": "1", "name":"Test 1", "checked":True})


    def test_update_item_fail(self):
        """test whether checking an item works"""
        response = self.client.put("api/items/2", json={"checked": True})
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json(), {"message": "ID not found"})

### TODO: add more unit tests