from typing import List, Dict
from aiohttp import web

from openapi_server.models.virtual_tariffs_of_folder import VirtualTariffsOfFolder
from openapi_server import util


async def virtual_tariffs_for_property_get(request: web.Request, id) -> web.Response:
    """Gets all Virtual Tariffs for a property (folder)

    Gets all Virtual Tariffs for a property (folder)

    :param id: 
    :type id: str

    """
    return web.Response(status=200)
