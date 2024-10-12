from typing import List, Dict
from aiohttp import web

from openapi_server.models.catalog import Catalog
from openapi_server.models.error import Error
from openapi_server import util


async def get_catalog(request: web.Request, api_version, subscription_id, reserved_resource_type, location=None) -> web.Response:
    """Get the regions and skus that are available for RI purchase for the specified Azure subscription.

    

    :param api_version: Supported version.
    :type api_version: str
    :param subscription_id: Id of the subscription
    :type subscription_id: str
    :param reserved_resource_type: The type of the resource for which the skus should be provided.
    :type reserved_resource_type: str
    :param location: Filters the skus based on the location specified in this parameter. This can be an azure region or global
    :type location: str

    """
    return web.Response(status=200)
