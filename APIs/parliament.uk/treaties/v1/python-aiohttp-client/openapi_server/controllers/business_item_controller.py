from typing import List, Dict
from aiohttp import web

from openapi_server.models.business_item_resource import BusinessItemResource
from openapi_server import util


async def get_business_item_by_id(request: web.Request, id) -> web.Response:
    """Returns business item by ID.

    

    :param id: Business item with the ID specified
    :type id: str

    """
    return web.Response(status=200)
