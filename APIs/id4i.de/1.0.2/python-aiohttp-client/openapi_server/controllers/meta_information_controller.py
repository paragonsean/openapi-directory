from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_error import ApiError
from openapi_server.models.app_info_presentation import AppInfoPresentation
from openapi_server import util


async def application_info(request: web.Request, ) -> web.Response:
    """Retrieve version information about ID4i

    Retrieving version information about ID4i.


    """
    return web.Response(status=200)
