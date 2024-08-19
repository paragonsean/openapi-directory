from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_model import ErrorModel
from openapi_server.models.extended_error_model import ExtendedErrorModel
from openapi_server.models.test_response import TestResponse
from openapi_server import util


async def utils_errors_errorcode_get(request: web.Request, errorcode) -> web.Response:
    """utils_errors_errorcode_get

    Returns a sample error object for the given error code. Useful for designing code to react to errors when they occur for real.

    :param errorcode: The code of the error you would like returned
    :type errorcode: str

    """
    return web.Response(status=200)


async def utils_test_get(request: web.Request, ) -> web.Response:
    """utils_test_get

    Returns the customer ID to the caller


    """
    return web.Response(status=200)
