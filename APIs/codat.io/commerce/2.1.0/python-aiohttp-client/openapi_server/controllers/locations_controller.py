from typing import List, Dict
from aiohttp import web

from openapi_server.models.locations_response import LocationsResponse
from openapi_server import util


async def list_locations(request: web.Request, company_id, connection_id) -> web.Response:
    """List locations

    Retrieve a list of locations as seen in the commerce platform.  A &#x60;location&#x60; is a geographic place at which stocks of products may be held, or from where orders were placed.

    :param company_id: 
    :type company_id: str
    :type company_id: str
    :param connection_id: 
    :type connection_id: str
    :type connection_id: str

    """
    return web.Response(status=200)
