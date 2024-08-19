from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def name_authorities_get(request: web.Request, output_format) -> web.Response:
    """Get all name authorities

    Gets a list of all name authorities responsible for naming decisions of the geographical names in the BC Geographical Names Information System (BCGNIS)

    :param output_format: The format of the output.
    :type output_format: str

    """
    return web.Response(status=200)
