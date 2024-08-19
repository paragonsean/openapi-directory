from typing import List, Dict
from aiohttp import web

from openapi_server.models.items_channel_instance import ItemsChannelInstance
from openapi_server import util


async def channel_instances(request: web.Request, ) -> web.Response:
    """Retrieves a list of currently running channel instances.

    


    """
    return web.Response(status=200)
