from typing import List, Dict
from aiohttp import web

from openapi_server.models.result import Result
from openapi_server import util


async def reports_get_dev_ops(request: web.Request, api_version) -> web.Response:
    """reports_get_dev_ops

    Checks if the user is enabled for Dev Ops access.

    :param api_version: The version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)
