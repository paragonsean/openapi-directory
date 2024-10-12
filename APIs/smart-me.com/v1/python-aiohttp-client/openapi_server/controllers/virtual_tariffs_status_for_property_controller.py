from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def virtual_tariffs_status_for_property_get(request: web.Request, id) -> web.Response:
    """Gets the calculation status for a virtual tariff property

    

    :param id: 
    :type id: str

    """
    return web.Response(status=200)
