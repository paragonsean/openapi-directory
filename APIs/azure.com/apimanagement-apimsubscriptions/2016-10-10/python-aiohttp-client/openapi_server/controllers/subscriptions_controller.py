from typing import List, Dict
from aiohttp import web

from openapi_server.models.subscription_collection import SubscriptionCollection
from openapi_server.models.subscription_contract import SubscriptionContract
from openapi_server.models.subscription_create_parameters import SubscriptionCreateParameters
from openapi_server.models.subscription_update_parameters import SubscriptionUpdateParameters
from openapi_server.models.subscriptions_list_default_response import SubscriptionsListDefaultResponse
from openapi_server import util


async def subscriptions_create_or_update(request: web.Request, resource_group_name, service_name, sid, api_version, subscription_id, parameters) -> web.Response:
    """subscriptions_create_or_update

    Creates or updates the subscription of specified user to the specified product.

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
    :param parameters: Create parameters.
    :type parameters: dict | bytes

    """
    parameters = SubscriptionCreateParameters.from_dict(parameters)
    return web.Response(status=200)


async def subscriptions_delete(request: web.Request, resource_group_name, service_name, sid, if_match, api_version, subscription_id) -> web.Response:
    """subscriptions_delete

    Deletes the specified subscription.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param sid: Subscription entity Identifier. The entity represents the association between a user and a product in API Management.
    :type sid: str
    :param if_match: ETag of the Subscription Entity. ETag should match the current entity state from the header response of the GET request or it should be * for unconditional update.
    :type if_match: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def subscriptions_get(request: web.Request, resource_group_name, service_name, sid, api_version, subscription_id) -> web.Response:
    """subscriptions_get

    Gets the specified Subscription entity.

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


async def subscriptions_list(request: web.Request, resource_group_name, service_name, api_version, subscription_id, filter=None, top=None, skip=None) -> web.Response:
    """subscriptions_list

    Lists all subscriptions of the API Management service instance.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param filter: | Field        | Supported operators    | Supported functions                         | |--------------|------------------------|---------------------------------------------| | id           | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | name         | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | stateComment | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | userId       | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | productId    | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | state        | eq                     |                                             |
    :type filter: str
    :param top: Number of records to return.
    :type top: int
    :param skip: Number of records to skip.
    :type skip: int

    """
    return web.Response(status=200)


async def subscriptions_regenerate_primary_key(request: web.Request, resource_group_name, service_name, sid, api_version, subscription_id) -> web.Response:
    """subscriptions_regenerate_primary_key

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


async def subscriptions_regenerate_secondary_key(request: web.Request, resource_group_name, service_name, sid, api_version, subscription_id) -> web.Response:
    """subscriptions_regenerate_secondary_key

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


async def subscriptions_update(request: web.Request, resource_group_name, service_name, sid, if_match, api_version, subscription_id, parameters) -> web.Response:
    """subscriptions_update

    Updates the details of a subscription specified by its identifier.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param sid: Subscription entity Identifier. The entity represents the association between a user and a product in API Management.
    :type sid: str
    :param if_match: ETag of the Subscription Entity. ETag should match the current entity state from the header response of the GET request or it should be * for unconditional update.
    :type if_match: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Update parameters.
    :type parameters: dict | bytes

    """
    parameters = SubscriptionUpdateParameters.from_dict(parameters)
    return web.Response(status=200)
