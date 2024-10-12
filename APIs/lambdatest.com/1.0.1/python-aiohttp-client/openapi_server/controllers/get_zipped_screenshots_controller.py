from typing import List, Dict
from aiohttp import web

from openapi_server.models.access_denied import AccessDenied
from openapi_server.models.forbidden import Forbidden
from openapi_server.models.screenshot_not_found import ScreenshotNotFound
from openapi_server.models.zipped_screenshots_success import ZippedScreenshotsSuccess
from openapi_server import util


async def zipped_screenshots(request: web.Request, test_id) -> web.Response:
    """Fetch Zipped Screenshots

    Fetch Zipped Screenshots

    :param test_id: Test ID that Zipped Screenshots you want to fetch
    :type test_id: str

    """
    return web.Response(status=200)
