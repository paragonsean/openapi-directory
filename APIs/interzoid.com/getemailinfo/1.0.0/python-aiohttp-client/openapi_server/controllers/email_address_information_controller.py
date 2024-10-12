from typing import List, Dict
from aiohttp import web

from openapi_server.models.getemailinfo200_response import Getemailinfo200Response
from openapi_server import util


async def getemailinfo(request: web.Request, license, email) -> web.Response:
    """Gets email validation information for an email address

    Get email validation information and other demographics for an email address.

    :param license: Your Interzoid license API key. Register at www.interzoid.com/register
    :type license: str
    :param email: Email address to retrieve validation information
    :type email: str

    """
    return web.Response(status=200)
