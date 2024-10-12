from typing import List, Dict
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.lab_cost import LabCost
from openapi_server import util


async def costs_create_or_update(request: web.Request, subscription_id, resource_group_name, lab_name, name, api_version, lab_cost) -> web.Response:
    """costs_create_or_update

    Create or replace an existing cost.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_name: The name of the lab.
    :type lab_name: str
    :param name: The name of the cost.
    :type name: str
    :param api_version: Client API version.
    :type api_version: str
    :param lab_cost: A cost item.
    :type lab_cost: dict | bytes

    """
    lab_cost = LabCost.from_dict(lab_cost)
    return web.Response(status=200)


async def costs_get(request: web.Request, subscription_id, resource_group_name, lab_name, name, api_version, expand=None) -> web.Response:
    """costs_get

    Get cost.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_name: The name of the lab.
    :type lab_name: str
    :param name: The name of the cost.
    :type name: str
    :param api_version: Client API version.
    :type api_version: str
    :param expand: Specify the $expand query. Example: &#39;properties($expand&#x3D;labCostDetails)&#39;
    :type expand: str

    """
    return web.Response(status=200)
