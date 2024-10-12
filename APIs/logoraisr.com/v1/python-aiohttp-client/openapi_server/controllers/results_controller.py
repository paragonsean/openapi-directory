from typing import List, Dict
from aiohttp import web

from openapi_server.models.result_response import ResultResponse
from openapi_server import util


async def results_read(request: web.Request, result_file_id) -> web.Response:
    """Get the result from image processing

    This GET-Method returns the URL where the result can downloaded from.

    :param result_file_id: Id of the result_file for which the result_file_url is generated.
    :type result_file_id: str

    """
    return web.Response(status=200)
