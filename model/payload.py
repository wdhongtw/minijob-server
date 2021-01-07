"""Models for API request and response."""

from enum import Enum
from typing import Optional, Dict, List, Set
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


class ItemMeta(ItemId):
    """The item metadata model."""

    length: int

    # seconds since the epoch
    timestamp: int


class ItemDetail(ItemMeta, Item):
    """The item detail model."""


class JobState(str, Enum):
    """Job state."""

    CREATED = "created"
    PREPARED = "prepared"
    STARTED = "started"
    FINISHED = "finished"
    EXPIRED = "expired"


class JobStateFiles(BaseModel):
    """The job state and files model."""

    state: Optional[JobState]

    # Map from path to item_id
    resources: Optional[Dict[str, str]]
    # Map from path to item_id
    artifacts: Optional[Dict[str, str]]


class JobResult(BaseModel):
    """The job result model."""

    success: Optional[bool]
    reason: Optional[str]
    log: Optional[str]


class JobPatch(JobStateFiles):
    """The patch content for job."""

    result: Optional[JobResult]


class JobDescription(BaseModel):
    """The job description model."""

    name: str
    scripts: List[str]
    tags: Set[str]


class JobDetail(JobDescription, JobResult, JobStateFiles):
    """The full job model."""
