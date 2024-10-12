from typing import List, Dict
from aiohttp import web

from openapi_server.models.subscription_collection import SubscriptionCollection
from openapi_server.models.subscription_contract import SubscriptionContract
from openapi_server.models.subscription_create_parameters import SubscriptionCreateParameters
from openapi_server.models.subscription_list_default_response import SubscriptionListDefaultResponse
from openapi_server.models.subscription_update_parameters import SubscriptionUpdateParameters
from openapi_server import util


async def subscription_create_or_update(request: web.Request, resource_group_name, service_name, sid, api_version, subscription_id, parameters, notify=None, if_match=None) -> web.Response:
    """subscription_create_or_update

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
    :param notify: Notify change in Subscription State.   - If false, do not send any email notification for change of state of subscription   - If true, send email notification of change of state of subscription 
    :type notify: bool
    :param if_match: ETag of the Entity. Not required when creating an entity, but required when updating an entity.
    :type if_match: str

    """
    parameters = SubscriptionCreateParameters.from_dict(parameters)
    return web.Response(status=200)


async def subscription_delete(request: web.Request, resource_group_name, service_name, sid, if_match, api_version, subscription_id) -> web.Response:
    """subscription_delete

    Deletes the specified subscription.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param sid: Subscription entity Identifier. The entity represents the association between a user and a product in API Management.
    :type sid: str
    :param if_match: ETag of the Entity. ETag should match the current entity state from the header response of the GET request or it should be * for unconditional update.
    :type if_match: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def subscription_get(request: web.Request, resource_group_name, service_name, sid, api_version, subscription_id) -> web.Response:
    """subscription_get

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


async def subscription_get_entity_tag(request: web.Request, resource_group_name, service_name, sid, api_version, subscription_id) -> web.Response:
    """subscription_get_entity_tag

    Gets the entity state (Etag) version of the apimanagement subscription specified by its identifier.

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


async def subscription_list(request: web.Request, resource_group_name, service_name, api_version, subscription_id, filter=None, top=None, skip=None) -> web.Response:
    """subscription_list

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


async def subscription_update(request: web.Request, resource_group_name, service_name, sid, if_match, api_version, subscription_id, parameters, notify=None) -> web.Response:
    """subscription_update

    Updates the details of a subscription specified by its identifier.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param sid: Subscription entity Identifier. The entity represents the association between a user and a product in API Management.
    :type sid: str
    :param if_match: ETag of the Entity. ETag should match the current entity state from the header response of the GET request or it should be * for unconditional update.
    :type if_match: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Update parameters.
    :type parameters: dict | bytes
    :param notify: Notify change in Subscription State.   - If false, do not send any email notification for change of state of subscription   - If true, send email notification of change of state of subscription 
    :type notify: bool

    """
    parameters = SubscriptionUpdateParameters.from_dict(parameters)
    return web.Response(status=200)
