from unittest import TestCase

from fastapi.testclient import TestClient

from main import app
from modules.apis.frontend import home

from modules.models.models import items, Item


class TestFrontend(TestCase):
    def test_home(self):
        """Method to test correct response from home"""
        self.assertEqual(home(), {"message":"Hello world!"})


class TestCRUD(TestCase):

    def setUp(self):
        """Method to set up code for testing"""
        self.client = TestClient(app)
        items.clear()
        items[1] = Item(name="Test 1")


    def tearDown(self):
        """Method to teardown after each test and start fresh"""
        items.clear()

    def test_get_items(self):
        """method for testing get items function returning right status and resposne"""
        response = self.client.get("api/items")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"Items": {"1":{"name": "Test 1", "checked":False}}})

    def test_add_item_success(self):
        """Method to test adding an item functionality"""
        response = self.client.post("api/items/2", json={"name": "Test 2"})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), {"id": 2, "name":"Test 2", "checked":False})
        self.assertEqual(items, {1:Item(name="Test 1"), 2:Item(name="Test 2")})
    
    def test_add_item_fails(self):
        """Method to test adding an item functionality when item exists"""
        response = self.client.post("api/items/1", json={"name": "Test 1"})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"message": "Item already exists"})

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

### TODO: add more unit tests