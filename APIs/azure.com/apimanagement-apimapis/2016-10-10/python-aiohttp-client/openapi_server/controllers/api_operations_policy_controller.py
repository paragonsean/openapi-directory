from typing import List, Dict
from aiohttp import web

from openapi_server.models.apis_list_by_service_default_response import ApisListByServiceDefaultResponse
from openapi_server import util


async def api_operations_policy_create_or_update(request: web.Request, resource_group_name, service_name, api_id, operation_id, if_match, api_version, subscription_id, parameters) -> web.Response:
    """api_operations_policy_create_or_update

    Creates or updates policy configuration for the API Operation level.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param api_id: API identifier. Must be unique in the current API Management service instance.
    :type api_id: str
    :param operation_id: Operation identifier within an API. Must be unique in the current API Management service instance.
    :type operation_id: str
    :param if_match: The entity state (Etag) version of the Api Operation policy to update. A value of \&quot;*\&quot; can be used for If-Match to unconditionally apply the operation.
    :type if_match: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: The policy contents to apply.
    :type parameters: 

    """
    return web.Response(status=200)


async def api_operations_policy_delete(request: web.Request, resource_group_name, service_name, api_id, operation_id, if_match, api_version, subscription_id) -> web.Response:
    """api_operations_policy_delete

    Deletes the policy configuration at the Api Operation.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param api_id: API identifier. Must be unique in the current API Management service instance.
    :type api_id: str
    :param operation_id: Operation identifier within an API. Must be unique in the current API Management service instance.
    :type operation_id: str
    :param if_match: The entity state (Etag) version of the Api operation policy to update. A value of \&quot;*\&quot; can be used for If-Match to unconditionally apply the operation.
    :type if_match: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def api_operations_policy_get(request: web.Request, resource_group_name, service_name, api_id, operation_id, api_version, subscription_id) -> web.Response:
    """api_operations_policy_get

    Get the policy configuration at the API Operation level.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param api_id: API identifier. Must be unique in the current API Management service instance.
    :type api_id: str
    :param operation_id: Operation identifier within an API. Must be unique in the current API Management service instance.
    :type operation_id: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)
