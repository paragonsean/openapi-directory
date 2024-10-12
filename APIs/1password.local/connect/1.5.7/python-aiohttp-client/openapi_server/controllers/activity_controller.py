from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_request import APIRequest
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def get_api_activity(request: web.Request, limit=None, offset=None) -> web.Response:
    """Retrieve a list of API Requests that have been made.

    

    :param limit: How many API Events should be retrieved in a single request.
    :type limit: int
    :param offset: How far into the collection of API Events should the response start
    :type offset: int

    """
    return web.Response(status=200)
