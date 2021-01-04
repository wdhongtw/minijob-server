"""Main web service description."""

import base64
import datetime
import uuid
from typing import Dict, List

from fastapi import FastAPI

import model


app = FastAPI()

# Global objects

_storage: Dict[str, model.ItemDetail] = {}


@app.get("/", response_model=model.Meta)
def show_meta():
    """Show metadata for the site."""
    return model.Meta()


@app.get("/items/", response_model=List[model.ItemMeta])
async def retrieve_all_item_detail():
    """Get all metadata of items."""
    return [model.ItemMeta(**detail.dict()) for detail in _storage.values()]


@app.get("/items/{item_id}", response_model=model.Item)
async def retrieve_item(item_id: str):
    """Retrieve item."""

    return _storage[item_id]


@app.post("/items/", response_model=model.ItemId)
async def create_item(item: model.Item):
    """Allocate new item."""
    length = len(base64.b64decode(item.content.encode()))
    timestamp = int(datetime.datetime.now().timestamp())
    item_id = str(uuid.uuid4())
    _storage[item_id] = model.ItemDetail(
        **item.dict(), length=length, timestamp=timestamp, item_id=item_id
    )

    return model.ItemId(item_id=item_id)
