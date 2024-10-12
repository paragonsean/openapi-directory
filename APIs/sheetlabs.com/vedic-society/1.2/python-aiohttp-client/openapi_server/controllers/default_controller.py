from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def resources_get(request: web.Request, description) -> web.Response:
    """Fetch all meanings that contain a specific English string

    

    :param description: The string you are looking for in the word meaning, for example, chariot. Wildcards are allowed, for example, char\\*.
    :type description: str

    """
    return web.Response(status=200)
