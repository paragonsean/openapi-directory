from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_marketplace_available_add_on_extension_response import ListMarketplaceAvailableAddOnExtensionResponse
from openapi_server.models.preview_marketplace_available_add_on_available_add_on_extension import PreviewMarketplaceAvailableAddOnAvailableAddOnExtension
from openapi_server import util


async def fetch_marketplace_available_add_on_extension(request: web.Request, available_add_on_sid, sid) -> web.Response:
    """fetch_marketplace_available_add_on_extension

    Fetch an instance of an Extension for the Available Add-on.

    :param available_add_on_sid: The SID of the AvailableAddOn resource with the extension to fetch.
    :type available_add_on_sid: str
    :param sid: The SID of the AvailableAddOn Extension resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def list_marketplace_available_add_on_extension(request: web.Request, available_add_on_sid, page_size=None, page=None, page_token=None) -> web.Response:
    """list_marketplace_available_add_on_extension

    Retrieve a list of Extensions for the Available Add-on.

    :param available_add_on_sid: The SID of the AvailableAddOn resource with the extensions to read.
    :type available_add_on_sid: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)
