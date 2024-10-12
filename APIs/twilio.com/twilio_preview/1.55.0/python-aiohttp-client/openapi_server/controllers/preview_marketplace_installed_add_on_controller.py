from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_marketplace_installed_add_on_response import ListMarketplaceInstalledAddOnResponse
from openapi_server.models.preview_marketplace_installed_add_on import PreviewMarketplaceInstalledAddOn
from openapi_server import util


async def create_marketplace_installed_add_on(request: web.Request, accept_terms_of_service, available_add_on_sid, configuration=None, unique_name=None) -> web.Response:
    """create_marketplace_installed_add_on

    Install an Add-on for the Account specified.

    :param accept_terms_of_service: Whether the Terms of Service were accepted.
    :type accept_terms_of_service: bool
    :param available_add_on_sid: The SID of the AvaliableAddOn to install.
    :type available_add_on_sid: str
    :param configuration: The JSON object that represents the configuration of the new Add-on being installed.
    :type configuration: dict | bytes
    :param unique_name: An application-defined string that uniquely identifies the resource. This value must be unique within the Account.
    :type unique_name: str

    """
    configuration = object.from_dict(configuration)
    return web.Response(status=200)


async def delete_marketplace_installed_add_on(request: web.Request, sid) -> web.Response:
    """delete_marketplace_installed_add_on

    Remove an Add-on installation from your account

    :param sid: The SID of the InstalledAddOn resource to delete.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_marketplace_installed_add_on(request: web.Request, sid) -> web.Response:
    """fetch_marketplace_installed_add_on

    Fetch an instance of an Add-on currently installed on this Account.

    :param sid: The SID of the InstalledAddOn resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def list_marketplace_installed_add_on(request: web.Request, page_size=None, page=None, page_token=None) -> web.Response:
    """list_marketplace_installed_add_on

    Retrieve a list of Add-ons currently installed on this Account.

    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def update_marketplace_installed_add_on(request: web.Request, sid, configuration=None, unique_name=None) -> web.Response:
    """update_marketplace_installed_add_on

    Update an Add-on installation for the Account specified.

    :param sid: The SID of the InstalledAddOn resource to update.
    :type sid: str
    :param configuration: Valid JSON object that conform to the configuration schema exposed by the associated AvailableAddOn resource. This is only required by Add-ons that need to be configured
    :type configuration: dict | bytes
    :param unique_name: An application-defined string that uniquely identifies the resource. This value must be unique within the Account.
    :type unique_name: str

    """
    configuration = object.from_dict(configuration)
    return web.Response(status=200)
