"""Main web service description."""

import uuid
from typing import Dict

from fastapi import FastAPI

import model


app = FastAPI()

# Global objects

_storage: Dict[str, model.Item] = {}


@app.get("/", response_model=model.Meta)
def show_meta():
    """Show metadata for the site."""
    return model.Meta()


@app.get("/items/{item_id}", response_model=model.Item)
async def retrieve_item(item_id: str):
    """Retrieve item."""

    return _storage[item_id]


@app.post("/items/", response_model=model.ItemId)
async def create_item(item: model.Item):
    """Allocate new item."""
    item_id = str(uuid.uuid4())
    _storage[item_id] = item

    return model.ItemId(item_id=item_id)
