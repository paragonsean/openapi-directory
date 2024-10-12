from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.pet import Pet
from openapi_server import util


async def create_pets(request: web.Request, ) -> web.Response:
    """Create a pet

    


    """
    return web.Response(status=200)


async def list_pets(request: web.Request, limit=None) -> web.Response:
    """List all pets

    

    :param limit: How many items to return at one time (max 100)
    :type limit: int

    """
    return web.Response(status=200)


async def show_pet_by_id(request: web.Request, pet_id) -> web.Response:
    """Info for a specific pet

    

    :param pet_id: The id of the pet to retrieve
    :type pet_id: str

    """
    return web.Response(status=200)
