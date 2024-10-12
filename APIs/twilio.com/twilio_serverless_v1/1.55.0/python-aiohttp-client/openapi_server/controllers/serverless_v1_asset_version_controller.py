from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_asset_version_response import ListAssetVersionResponse
from openapi_server.models.serverless_v1_service_asset_asset_version import ServerlessV1ServiceAssetAssetVersion
from openapi_server import util


async def fetch_asset_version(request: web.Request, service_sid, asset_sid, sid) -> web.Response:
    """fetch_asset_version

    Retrieve a specific Asset Version.

    :param service_sid: The SID of the Service to fetch the Asset Version resource from.
    :type service_sid: str
    :param asset_sid: The SID of the Asset resource that is the parent of the Asset Version resource to fetch.
    :type asset_sid: str
    :param sid: The SID of the Asset Version resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def list_asset_version(request: web.Request, service_sid, asset_sid, page_size=None, page=None, page_token=None) -> web.Response:
    """list_asset_version

    Retrieve a list of all Asset Versions.

    :param service_sid: The SID of the Service to read the Asset Version resource from.
    :type service_sid: str
    :param asset_sid: The SID of the Asset resource that is the parent of the Asset Version resources to read.
    :type asset_sid: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)
