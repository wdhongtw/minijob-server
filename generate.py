"""Generate OpenAPI schema."""

import json

from fastapi.openapi.utils import get_openapi
from main import app


with open("openapi.json", "w") as file_:
    json.dump(
        get_openapi(
            title=app.title,
            version=app.version,
            openapi_version=app.openapi_version,
            description=app.description,
            routes=app.routes,
        ),
        file_,
        indent=2,
    )
