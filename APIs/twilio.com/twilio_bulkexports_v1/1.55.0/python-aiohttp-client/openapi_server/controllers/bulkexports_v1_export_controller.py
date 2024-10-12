from typing import List, Dict
from aiohttp import web

from openapi_server.models.bulkexports_v1_export import BulkexportsV1Export
from openapi_server import util


async def fetch_export(request: web.Request, resource_type) -> web.Response:
    """fetch_export

    Fetch a specific Export.

    :param resource_type: The type of communication – Messages, Calls, Conferences, and Participants
    :type resource_type: str

    """
    return web.Response(status=200)
