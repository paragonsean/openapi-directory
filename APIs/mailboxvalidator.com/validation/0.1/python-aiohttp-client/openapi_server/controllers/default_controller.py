from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def v1_validation_single_get(request: web.Request, email, key, format=None) -> web.Response:
    """v1_validation_single_get

    The Single Validation API does validation on a single email address and returns all the validation results in either JSON or XML format.

    :param email: The email address to be validated.
    :type email: str
    :param key: API key.
    :type key: str
    :param format: Return the result in json (default) or xml format.
    :type format: str

    """
    return web.Response(status=200)
