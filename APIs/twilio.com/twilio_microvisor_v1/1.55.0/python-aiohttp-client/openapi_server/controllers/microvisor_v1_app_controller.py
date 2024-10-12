from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_app_response import ListAppResponse
from openapi_server.models.microvisor_v1_app import MicrovisorV1App
from openapi_server import util


async def delete_app(request: web.Request, sid) -> web.Response:
    """delete_app

    Delete a specific App.

    :param sid: A 34-character string that uniquely identifies this App.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_app(request: web.Request, sid) -> web.Response:
    """fetch_app

    Fetch a specific App.

    :param sid: A 34-character string that uniquely identifies this App.
    :type sid: str

    """
    return web.Response(status=200)


async def list_app(request: web.Request, page_size=None, page=None, page_token=None) -> web.Response:
    """list_app

    Retrieve a list of all Apps for an Account.

    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)
