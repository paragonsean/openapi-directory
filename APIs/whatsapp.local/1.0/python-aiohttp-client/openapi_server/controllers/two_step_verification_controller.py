from typing import List, Dict
from aiohttp import web

from openapi_server.models.enable_two_step_request_body import EnableTwoStepRequestBody
from openapi_server import util


async def disable_two_step(request: web.Request, ) -> web.Response:
    """Disable-Two-Step

    


    """
    return web.Response(status=200)


async def enable_two_step(request: web.Request, body) -> web.Response:
    """Enable-Two-Step

    

    :param body: 
    :type body: dict | bytes

    """
    body = EnableTwoStepRequestBody.from_dict(body)
    return web.Response(status=200)
