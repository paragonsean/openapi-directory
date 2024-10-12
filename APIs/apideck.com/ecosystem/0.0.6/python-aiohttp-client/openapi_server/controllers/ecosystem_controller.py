from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_ecosystem_response import GetEcosystemResponse
from openapi_server import util


async def ecosystems_one(request: web.Request, ecosystem_id) -> web.Response:
    """Get ecosystem

    Get ecosystem

    :param ecosystem_id: 
    :type ecosystem_id: str

    """
    return web.Response(status=200)
