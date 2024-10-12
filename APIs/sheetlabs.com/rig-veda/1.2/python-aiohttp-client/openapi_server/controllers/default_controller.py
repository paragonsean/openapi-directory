from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def resources_get(request: web.Request, sungforcategory) -> web.Response:
    """Fetch all verses sung for a specific category of god, person, or object

    

    :param sungforcategory: Click to select one of these available values.
    :type sungforcategory: str

    """
    return web.Response(status=200)
