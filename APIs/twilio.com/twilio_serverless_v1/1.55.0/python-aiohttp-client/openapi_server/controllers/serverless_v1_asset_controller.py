from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_asset_response import ListAssetResponse
from openapi_server.models.serverless_v1_service_asset import ServerlessV1ServiceAsset
from openapi_server import util


async def create_asset(request: web.Request, service_sid, friendly_name) -> web.Response:
    """create_asset

    Create a new Asset resource.

    :param service_sid: The SID of the Service to create the Asset resource under.
    :type service_sid: str
    :param friendly_name: A descriptive string that you create to describe the Asset resource. It can be a maximum of 255 characters.
    :type friendly_name: str

    """
    return web.Response(status=200)


async def delete_asset(request: web.Request, service_sid, sid) -> web.Response:
    """delete_asset

    Delete an Asset resource.

    :param service_sid: The SID of the Service to delete the Asset resource from.
    :type service_sid: str
    :param sid: The SID that identifies the Asset resource to delete.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_asset(request: web.Request, service_sid, sid) -> web.Response:
    """fetch_asset

    Retrieve a specific Asset resource.

    :param service_sid: The SID of the Service to fetch the Asset resource from.
    :type service_sid: str
    :param sid: The SID that identifies the Asset resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def list_asset(request: web.Request, service_sid, page_size=None, page=None, page_token=None) -> web.Response:
    """list_asset

    Retrieve a list of all Assets.

    :param service_sid: The SID of the Service to read the Asset resources from.
    :type service_sid: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def update_asset(request: web.Request, service_sid, sid, friendly_name) -> web.Response:
    """update_asset

    Update a specific Asset resource.

    :param service_sid: The SID of the Service to update the Asset resource from.
    :type service_sid: str
    :param sid: The SID that identifies the Asset resource to update.
    :type sid: str
    :param friendly_name: A descriptive string that you create to describe the Asset resource. It can be a maximum of 255 characters.
    :type friendly_name: str

    """
    return web.Response(status=200)
