from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_test_error_schema import ApiTestErrorSchema
from openapi_server.models.api_test_success_schema import ApiTestSuccessSchema
from openapi_server import util


async def api_test(request: web.Request, error=None, foo=None) -> web.Response:
    """api_test

    Checks API calling code.

    :param error: Error response to return
    :type error: str
    :param foo: example property to return
    :type foo: str

    """
    return web.Response(status=200)
