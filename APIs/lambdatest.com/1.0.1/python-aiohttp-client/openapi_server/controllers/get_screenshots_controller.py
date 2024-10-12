from typing import List, Dict
from aiohttp import web

from openapi_server.models.access_denied import AccessDenied
from openapi_server.models.forbidden import Forbidden
from openapi_server.models.screenshot_not_found import ScreenshotNotFound
from openapi_server.models.screenshot_test_response import ScreenshotTestResponse
from openapi_server import util


async def screenshots(request: web.Request, test_id) -> web.Response:
    """Fetch specified screenshot details

    To fetch specified screenshot details

    :param test_id: Test ID that details you want to fetch
    :type test_id: str

    """
    return web.Response(status=200)
