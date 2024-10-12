from typing import List, Dict
from aiohttp import web

from openapi_server.models.events_v1_schema import EventsV1Schema
from openapi_server import util


async def fetch_schema(request: web.Request, id) -> web.Response:
    """fetch_schema

    Fetch a specific schema with its nested versions.

    :param id: The unique identifier of the schema. Each schema can have multiple versions, that share the same id.
    :type id: str

    """
    return web.Response(status=200)
