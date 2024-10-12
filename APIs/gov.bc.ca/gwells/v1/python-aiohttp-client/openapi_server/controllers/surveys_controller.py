from typing import List, Dict
from aiohttp import web

from openapi_server.models.survey import Survey
from openapi_server import util


async def surveys_list(request: web.Request, ) -> web.Response:
    """surveys_list

    returns a list of active surveys


    """
    return web.Response(status=200)
