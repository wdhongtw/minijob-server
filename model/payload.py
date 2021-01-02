"""Models for API request and response."""

from typing import Optional
from pydantic import BaseModel


class Meta(BaseModel):
    """Metadata for the server."""

    version: str = "0.1.0"


class Item(BaseModel):
    """The item model."""

    path: str
    # Base64 encoded file content
    content: str


class ItemId(BaseModel):
    """The item ID model."""

    item_id: str
