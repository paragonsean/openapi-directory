from typing import List, Dict
from aiohttp import web

from openapi_server.models.access_denied import AccessDenied
from openapi_server.models.forbidden import Forbidden
from openapi_server.models.screenshot_payload import ScreenshotPayload
from openapi_server.models.start_screenshot_bad_request import StartScreenshotBadRequest
from openapi_server.models.start_screenshot_success import StartScreenshotSuccess
from openapi_server import util


async def start_screenshot_test(request: web.Request, body) -> web.Response:
    """Start Screenshot Test

    Start Screenshot Test

    :param body: start screenshot test payload.
    :type body: dict | bytes

    """
    body = ScreenshotPayload.from_dict(body)
    return web.Response(status=200)
