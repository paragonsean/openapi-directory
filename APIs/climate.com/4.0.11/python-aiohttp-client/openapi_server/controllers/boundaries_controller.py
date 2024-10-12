from typing import List, Dict
from aiohttp import web

from openapi_server.models.boundaries import Boundaries
from openapi_server.models.boundaries_query import BoundariesQuery
from openapi_server.models.boundary import Boundary
from openapi_server.models.boundary_upload import BoundaryUpload
from openapi_server.models.error import Error
from openapi_server.models.uploaded_boundary_id import UploadedBoundaryId
from openapi_server import util


async def fetch_boundaries(request: web.Request, body=None) -> web.Response:
    """Retrieve Boundaries in batch

    Retrieve multiple **Boundaries** (up to 10 per request).

    :param body: 
    :type body: dict | bytes

    """
    body = BoundariesQuery.from_dict(body)
    return web.Response(status=200)


async def fetch_boundary_by_id(request: web.Request, boundary_id) -> web.Response:
    """Retrieve a Boundary by ID

    Retrieve a **Boundary** by ID.

    :param boundary_id: Unique identifier of the Boundary
    :type boundary_id: str
    :type boundary_id: str

    """
    return web.Response(status=200)


async def upload_boundary(request: web.Request, body=None) -> web.Response:
    """Upload a boundary

    Upload a **Boundary** entry by passing the geometry of the boundary. This will store the boundary but will not create field in Climate FieldView and will not link to an existing field in Climate FieldView. This is restricted to callers with **boundaries:write** scope. To upload a field boundary for field creation in Climate FieldView, please use **POST /v4/uploads**.

    :param body: 
    :type body: dict | bytes

    """
    body = BoundaryUpload.from_dict(body)
    return web.Response(status=200)
