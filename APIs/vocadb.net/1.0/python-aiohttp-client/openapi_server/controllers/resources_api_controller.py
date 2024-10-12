from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def api_resources_culture_code_get(request: web.Request, culture_code, set_names=None) -> web.Response:
    """api_resources_culture_code_get

    

    :param culture_code: 
    :type culture_code: str
    :param set_names: 
    :type set_names: List[str]

    """
    return web.Response(status=200)
