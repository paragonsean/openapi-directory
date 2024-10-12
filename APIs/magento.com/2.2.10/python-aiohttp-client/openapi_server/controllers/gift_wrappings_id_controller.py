from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.gift_wrapping_data_wrapping_interface import GiftWrappingDataWrappingInterface
from openapi_server import util


async def gift_wrapping_wrapping_repository_v1_delete_by_id_delete(request: web.Request, id) -> web.Response:
    """gift-wrappings/{id}

    Delete gift wrapping

    :param id: 
    :type id: int

    """
    return web.Response(status=200)


async def gift_wrapping_wrapping_repository_v1_get_get(request: web.Request, id, store_id=None) -> web.Response:
    """gift-wrappings/{id}

    Return data object for specified wrapping ID and store.

    :param id: 
    :type id: int
    :param store_id: 
    :type store_id: int

    """
    return web.Response(status=200)
