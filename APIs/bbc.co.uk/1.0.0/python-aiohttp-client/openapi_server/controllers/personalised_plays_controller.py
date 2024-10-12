from typing import List, Dict
from aiohttp import web

from openapi_server.models.body4 import Body4
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def my_plays_post(request: web.Request, authorization, x_api_key, body) -> web.Response:
    """Write Play Event

    

    :param authorization: Bearer OAUTH_TOKEN
    :type authorization: str
    :param x_api_key: API_KEY
    :type x_api_key: str
    :param body: 
    :type body: dict | bytes

    """
    body = Body4.from_dict(body)
    return web.Response(status=200)
