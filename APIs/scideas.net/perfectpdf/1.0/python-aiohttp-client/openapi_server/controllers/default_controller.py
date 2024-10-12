from typing import List, Dict
from aiohttp import web

from openapi_server.models.inline_response200 import InlineResponse200
from openapi_server.models.perfectpdf_api_body import PerfectpdfApiBody
from openapi_server import util


async def perfectpdf_api_post(request: web.Request, body) -> web.Response:
    """Returns PDF document.

    

    :param body: 
    :type body: dict | bytes

    """
    body = PerfectpdfApiBody.from_dict(body)
    return web.Response(status=200)
