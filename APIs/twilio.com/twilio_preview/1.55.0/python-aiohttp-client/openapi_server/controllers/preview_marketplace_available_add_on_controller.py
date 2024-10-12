from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_marketplace_available_add_on_response import ListMarketplaceAvailableAddOnResponse
from openapi_server.models.preview_marketplace_available_add_on import PreviewMarketplaceAvailableAddOn
from openapi_server import util


async def fetch_marketplace_available_add_on(request: web.Request, sid) -> web.Response:
    """fetch_marketplace_available_add_on

    Fetch an instance of an Add-on currently available to be installed.

    :param sid: The SID of the AvailableAddOn resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def list_marketplace_available_add_on(request: web.Request, page_size=None, page=None, page_token=None) -> web.Response:
    """list_marketplace_available_add_on

    Retrieve a list of Add-ons currently available to be installed.

    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)
