"""Test main server."""

import unittest


from fastapi.testclient import TestClient

import base64
from main import app
import model

client = TestClient(app)


def serialize_bytes(content: bytes) -> str:
    return base64.b64encode(content).decode()


class TestCommonPart(unittest.TestCase):
    """Test common part of service."""

    def test_read_meta(self):
        response = client.get("/")
        assert response.status_code == 200
        assert response.json() == {"version": "0.1.0"}

    def test_store_item(self):
        original = model.Item(path="names.txt", content=serialize_bytes(b"alice\n"))

        post_response = client.post("/items/", json=original.dict())
        assert post_response.status_code == 200

        item_id = model.ItemId(**post_response.json()).item_id
        get_response = client.get("/items/{}".format(item_id))
        assert get_response.status_code == 200

        result = model.Item(**get_response.json())
        assert original == result
