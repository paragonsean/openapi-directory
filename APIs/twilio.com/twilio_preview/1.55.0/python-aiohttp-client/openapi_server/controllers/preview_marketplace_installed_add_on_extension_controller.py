from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_marketplace_installed_add_on_extension_response import ListMarketplaceInstalledAddOnExtensionResponse
from openapi_server.models.preview_marketplace_installed_add_on_installed_add_on_extension import PreviewMarketplaceInstalledAddOnInstalledAddOnExtension
from openapi_server import util


async def fetch_marketplace_installed_add_on_extension(request: web.Request, installed_add_on_sid, sid) -> web.Response:
    """fetch_marketplace_installed_add_on_extension

    Fetch an instance of an Extension for the Installed Add-on.

    :param installed_add_on_sid: The SID of the InstalledAddOn resource with the extension to fetch.
    :type installed_add_on_sid: str
    :param sid: The SID of the InstalledAddOn Extension resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def list_marketplace_installed_add_on_extension(request: web.Request, installed_add_on_sid, page_size=None, page=None, page_token=None) -> web.Response:
    """list_marketplace_installed_add_on_extension

    Retrieve a list of Extensions for the Installed Add-on.

    :param installed_add_on_sid: The SID of the InstalledAddOn resource with the extensions to read.
    :type installed_add_on_sid: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def update_marketplace_installed_add_on_extension(request: web.Request, installed_add_on_sid, sid, enabled) -> web.Response:
    """update_marketplace_installed_add_on_extension

    Update an Extension for an Add-on installation.

    :param installed_add_on_sid: The SID of the InstalledAddOn resource with the extension to update.
    :type installed_add_on_sid: str
    :param sid: The SID of the InstalledAddOn Extension resource to update.
    :type sid: str
    :param enabled: Whether the Extension should be invoked.
    :type enabled: bool

    """
    return web.Response(status=200)
