from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_status import CreateStatus
from openapi_server.models.delete_status import DeleteStatus
from openapi_server.models.error import Error
from openapi_server.models.update_status import UpdateStatus
from openapi_server import util


async def bin_id_delete(request: web.Request, id) -> web.Response:
    """Delete a json bin

    

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def bin_id_get(request: web.Request, id) -> web.Response:
    """Return a json bin

    

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def bin_id_patch(request: web.Request, id) -> web.Response:
    """Partially update a json bin with JSON Merge Patch

    

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def bin_id_put(request: web.Request, id) -> web.Response:
    """Update a json bin

    

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def bin_post(request: web.Request, ) -> web.Response:
    """Create a json bin

    


    """
    return web.Response(status=200)
