from typing import List, Dict
from aiohttp import web

from openapi_server.models.csrp_error import CSRPError
from openapi_server.models.customization_policies_list_response import CustomizationPoliciesListResponse
from openapi_server.models.customization_policy import CustomizationPolicy
from openapi_server import util


async def customization_policies_get(request: web.Request, api_version, subscription_id, region_id, pc_name, customization_policy_name) -> web.Response:
    """Implements get of customization policy

    Returns customization policy by its name

    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param region_id: The region Id (westus, eastus)
    :type region_id: str
    :param pc_name: The private cloud name
    :type pc_name: str
    :param customization_policy_name: customization policy name
    :type customization_policy_name: str

    """
    return web.Response(status=200)


async def customization_policies_list(request: web.Request, subscription_id, region_id, pc_name, api_version, filter=None) -> web.Response:
    """Implements get of customization policies list

    Returns list of customization policies in region for private cloud

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param region_id: The region Id (westus, eastus)
    :type region_id: str
    :param pc_name: The private cloud name
    :type pc_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param filter: The filter to apply on the list operation. only type is allowed here as a filter e.g. $filter&#x3D;type eq &#39;xxxx&#39;
    :type filter: str

    """
    return web.Response(status=200)
