from typing import List, Dict
from aiohttp import web

from openapi_server.models.csrp_error import CSRPError
from openapi_server.models.private_cloud import PrivateCloud
from openapi_server.models.private_cloud_list import PrivateCloudList
from openapi_server import util


async def private_clouds_get(request: web.Request, subscription_id, pc_name, region_id, api_version) -> web.Response:
    """Implements private cloud GET method

    Returns private cloud by its name

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param pc_name: The private cloud name
    :type pc_name: str
    :param region_id: The region Id (westus, eastus)
    :type region_id: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def private_clouds_list(request: web.Request, subscription_id, region_id, api_version) -> web.Response:
    """Implements private cloud list GET method

    Returns list of private clouds in particular region

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param region_id: The region Id (westus, eastus)
    :type region_id: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)
