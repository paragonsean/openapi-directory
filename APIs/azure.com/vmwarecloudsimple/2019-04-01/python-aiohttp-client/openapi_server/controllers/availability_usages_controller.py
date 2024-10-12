from typing import List, Dict
from aiohttp import web

from openapi_server.models.csrp_error import CSRPError
from openapi_server.models.sku_availability_list_response import SkuAvailabilityListResponse
from openapi_server.models.usage_list_response import UsageListResponse
from openapi_server import util


async def skus_availability_list(request: web.Request, subscription_id, region_id, api_version, sku_id=None) -> web.Response:
    """Implements SkuAvailability List method

    Returns list of available resources in region

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param region_id: The region Id (westus, eastus)
    :type region_id: str
    :param api_version: Client API version.
    :type api_version: str
    :param sku_id: sku id, if no sku is passed availability for all skus will be returned
    :type sku_id: str

    """
    return web.Response(status=200)


async def usages_list(request: web.Request, subscription_id, region_id, api_version, filter=None) -> web.Response:
    """Implements Usages List method

    Returns list of usage in region

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param region_id: The region Id (westus, eastus)
    :type region_id: str
    :param api_version: Client API version.
    :type api_version: str
    :param filter: The filter to apply on the list operation. only name.value is allowed here as a filter e.g. $filter&#x3D;name.value eq &#39;xxxx&#39;
    :type filter: str

    """
    return web.Response(status=200)
