from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_license_result import GetLicenseResult
from openapi_server import util


async def get_license(request: web.Request, ) -> web.Response:
    """Returns license content.

    Returns license content.


    """
    return web.Response(status=200)


async def refresh(request: web.Request, ) -> web.Response:
    """Refreshes license content.

    Refreshes license content. This method returns OK immediately and license is refreshed asynchronously. It takes a while (usually a few seconds) for the license to be actually refreshed.


    """
    return web.Response(status=200)
