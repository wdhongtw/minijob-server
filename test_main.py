"""Test main server."""

import unittest


from fastapi.testclient import TestClient

import base64
from main import app
import model


def serialize_bytes(content: bytes) -> str:
    return base64.b64encode(content).decode()


class TestCommonPart(unittest.TestCase):
    """Test common part of service."""

    def setUp(self):
        self.client = TestClient(app)

    def test_read_meta(self):
        response = self.client.get("/")
        assert response.status_code == 200
        assert response.json() == {"version": "0.1.0"}

    def test_store_item(self):
        original = model.Item(path="names.txt", content=serialize_bytes(b"alice\n"))

        post_response = self.client.post("/items/", json=original.dict())
        assert post_response.status_code == 200

        item_id = model.ItemId(**post_response.json()).item_id
        get_response = self.client.get("/items/{}".format(item_id))
        assert get_response.status_code == 200

        result = model.Item(**get_response.json())
        assert original == result


class TestItemCollection(unittest.TestCase):
    """Test item collection."""

    def setUp(self):
        self.client = TestClient(app)

    def test_retrieve_all_item(self):
        content = b"a" * 0x400
        path = "dir/dummy.txt"
        item = model.Item(path=path, content=serialize_bytes(content))

        post_response = self.client.post("/items/", json=item.dict())
        assert post_response.status_code == 200

        container_response = self.client.get("/items/")
        assert container_response.status_code == 200

        items: List[model.ItemMeta] = [
            model.ItemMeta(**item_meta) for item_meta in container_response.json()
        ]
        assert len(items) != 0
        returned = items[0]
        assert returned.length == len(content)
        assert len(returned.item_id) != 0
