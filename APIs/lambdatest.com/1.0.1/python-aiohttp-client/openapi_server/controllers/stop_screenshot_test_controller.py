from typing import List, Dict
from aiohttp import web

from openapi_server.models.access_denied import AccessDenied
from openapi_server.models.forbidden import Forbidden
from openapi_server.models.stop_screenshot_not_found import StopScreenshotNotFound
from openapi_server.models.stop_screenshot_success import StopScreenshotSuccess
from openapi_server import util


async def stop_screenshots_test(request: web.Request, test_id) -> web.Response:
    """Stop specified screenshot test

    Stop specified screenshot test

    :param test_id: Test ID that details you want to stop
    :type test_id: str

    """
    return web.Response(status=200)
