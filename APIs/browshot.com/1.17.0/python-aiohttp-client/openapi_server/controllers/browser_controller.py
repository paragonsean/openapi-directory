from typing import List, Dict
from aiohttp import web

from openapi_server.models.browser import Browser
from openapi_server.models.browser_error import BrowserError
from openapi_server.models.browser_list import BrowserList
from openapi_server import util


async def get_browser_info(request: web.Request, id) -> web.Response:
    """Get information about a browser

    Get information about a browser.

    :param id: browser ID
    :type id: int

    """
    return web.Response(status=200)


async def get_browsers_info(request: web.Request, ) -> web.Response:
    """Get all browsers

    Get all browsers.


    """
    return web.Response(status=200)
