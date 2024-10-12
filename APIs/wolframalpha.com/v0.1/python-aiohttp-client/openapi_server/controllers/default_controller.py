from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_wolfram_alpha_results(request: web.Request, input) -> web.Response:
    """Get Wolfram|Alpha results

    

    :param input: the input
    :type input: str

    """
    return web.Response(status=200)


async def get_wolfram_cloud_results(request: web.Request, input) -> web.Response:
    """Evaluate Wolfram Language code

    

    :param input: the input expression
    :type input: str

    """
    return web.Response(status=200)
