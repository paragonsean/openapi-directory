from typing import List, Dict
from aiohttp import web

from openapi_server.models.private_link_service import PrivateLinkService
from openapi_server.models.private_link_services_list_by_subscription_default_response import PrivateLinkServicesListBySubscriptionDefaultResponse
from openapi_server import util


async def private_link_services_create_or_update(request: web.Request, resource_group_name, service_name, api_version, subscription_id, parameters) -> web.Response:
    """private_link_services_create_or_update

    Creates or updates an private link service in the specified resource group.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the private link service.
    :type service_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters supplied to the create or update private link service operation.
    :type parameters: dict | bytes

    """
    parameters = PrivateLinkService.from_dict(parameters)
    return web.Response(status=200)
