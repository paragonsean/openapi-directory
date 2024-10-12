from typing import List, Dict
from aiohttp import web

from openapi_server.models.subscription_list_default_response import SubscriptionListDefaultResponse
from openapi_server import util


async def subscription_regenerate_primary_key(request: web.Request, resource_group_name, service_name, sid, api_version, subscription_id) -> web.Response:
    """subscription_regenerate_primary_key

    Regenerates primary key of existing subscription of the API Management service instance.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param sid: Subscription entity Identifier. The entity represents the association between a user and a product in API Management.
    :type sid: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def subscription_regenerate_secondary_key(request: web.Request, resource_group_name, service_name, sid, api_version, subscription_id) -> web.Response:
    """subscription_regenerate_secondary_key

    Regenerates secondary key of existing subscription of the API Management service instance.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param sid: Subscription entity Identifier. The entity represents the association between a user and a product in API Management.
    :type sid: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)
