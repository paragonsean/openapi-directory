from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def sales_shipment_track_repository_v1_delete_by_id_delete(request: web.Request, id) -> web.Response:
    """shipment/track/{id}

    Deletes a specified shipment track by ID.

    :param id: The shipment track ID.
    :type id: int

    """
    return web.Response(status=200)
