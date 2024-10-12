from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def v1_email_disposable_get(request: web.Request, email, key, format=None) -> web.Response:
    """v1_email_disposable_get

    The Disposable Email Checker API does checking on a single email address and returns if it is from a disposable email provider in either JSON or XML format.

    :param email: The email address to check if is from a disposable email provider.
    :type email: str
    :param key: API key.
    :type key: str
    :param format: Return the result in json (default) or xml format.
    :type format: str

    """
    return web.Response(status=200)
