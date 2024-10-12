from typing import List, Dict
from aiohttp import web

from openapi_server.models.attribute_update200_response import AttributeUpdate200Response
from openapi_server.models.bridge_delete200_response import BridgeDelete200Response
from openapi_server import util


async def bridge_delete(request: web.Request, ) -> web.Response:
    """bridge_delete

    Delete bridge from the store.


    """
    return web.Response(status=200)


async def bridge_update(request: web.Request, ) -> web.Response:
    """bridge_update

    Update bridge in the store.


    """
    return web.Response(status=200)
