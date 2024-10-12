from typing import List, Dict
from aiohttp import web

from openapi_server.models.store_items import StoreItems
from openapi_server import util


async def get_by_account(request: web.Request, ) -> web.Response:
    """Get Stores

    Gets the stores and respective hosts of the account


    """
    return web.Response(status=200)
