from typing import List, Dict
from aiohttp import web

from openapi_server.models.smart_list import SmartList
from openapi_server import util


async def get_smart_list_collection(request: web.Request, ) -> web.Response:
    """Retrieves the collection of SmartList resources.

    


    """
    return web.Response(status=200)


async def get_smart_list_item(request: web.Request, id) -> web.Response:
    """Retrieves a SmartList resource.

    

    :param id: 
    :type id: str

    """
    return web.Response(status=200)
