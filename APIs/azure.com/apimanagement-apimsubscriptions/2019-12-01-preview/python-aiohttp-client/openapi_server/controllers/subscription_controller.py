from typing import List, Dict
from aiohttp import web

from openapi_server.models.subscription_create_or_update_request import SubscriptionCreateOrUpdateRequest
from openapi_server.models.subscription_get200_response import SubscriptionGet200Response
from openapi_server.models.subscription_list200_response import SubscriptionList200Response
from openapi_server.models.subscription_list_default_response import SubscriptionListDefaultResponse
from openapi_server.models.subscription_list_secrets200_response import SubscriptionListSecrets200Response
from openapi_server.models.subscription_update_request import SubscriptionUpdateRequest
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
    parameters = SubscriptionCreateOrUpdateRequest.from_dict(parameters)
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
    :param filter: |   Field     |     Usage     |     Supported operators     |     Supported functions     |&lt;/br&gt;|-------------|-------------|-------------|-------------|&lt;/br&gt;| name | filter | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | &lt;/br&gt;| displayName | filter | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | &lt;/br&gt;| stateComment | filter | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | &lt;/br&gt;| ownerId | filter | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | &lt;/br&gt;| scope | filter | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | &lt;/br&gt;| userId | filter | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | &lt;/br&gt;| productId | filter | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | &lt;/br&gt;| state | filter | eq |     | &lt;/br&gt;| user | expand |     |     | &lt;/br&gt;
    :type filter: str
    :param top: Number of records to return.
    :type top: int
    :param skip: Number of records to skip.
    :type skip: int

    """
    return web.Response(status=200)


async def subscription_list_secrets(request: web.Request, resource_group_name, service_name, sid, api_version, subscription_id) -> web.Response:
    """subscription_list_secrets

    Gets the subscription keys.

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
    parameters = SubscriptionUpdateRequest.from_dict(parameters)
    return web.Response(status=200)
