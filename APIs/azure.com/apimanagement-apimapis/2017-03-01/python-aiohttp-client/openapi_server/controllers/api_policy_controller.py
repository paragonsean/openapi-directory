from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_list_by_service_default_response import ApiListByServiceDefaultResponse
from openapi_server.models.api_operation_policy_get200_response import ApiOperationPolicyGet200Response
from openapi_server.models.api_operation_policy_list_by_operation200_response import ApiOperationPolicyListByOperation200Response
from openapi_server import util


async def api_policy_create_or_update(request: web.Request, resource_group_name, service_name, api_id, policy_id, if_match, api_version, subscription_id, parameters) -> web.Response:
    """api_policy_create_or_update

    Creates or updates policy configuration for the API.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param api_id: API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev&#x3D;n as a suffix where n is the revision number.
    :type api_id: str
    :param policy_id: The identifier of the Policy.
    :type policy_id: str
    :param if_match: The entity state (Etag) version of the Api Policy to update. A value of \&quot;*\&quot; can be used for If-Match to unconditionally apply the operation.
    :type if_match: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: The policy contents to apply.
    :type parameters: dict | bytes

    """
    parameters = ApiOperationPolicyGet200Response.from_dict(parameters)
    return web.Response(status=200)


async def api_policy_delete(request: web.Request, resource_group_name, service_name, api_id, policy_id, if_match, api_version, subscription_id) -> web.Response:
    """api_policy_delete

    Deletes the policy configuration at the Api.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param api_id: API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev&#x3D;n as a suffix where n is the revision number.
    :type api_id: str
    :param policy_id: The identifier of the Policy.
    :type policy_id: str
    :param if_match: The entity state (Etag) version of the Api policy to update. A value of \&quot;*\&quot; can be used for If-Match to unconditionally apply the operation.
    :type if_match: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def api_policy_get(request: web.Request, resource_group_name, service_name, api_id, policy_id, api_version, subscription_id) -> web.Response:
    """api_policy_get

    Get the policy configuration at the API level.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param api_id: API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev&#x3D;n as a suffix where n is the revision number.
    :type api_id: str
    :param policy_id: The identifier of the Policy.
    :type policy_id: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def api_policy_get_entity_tag(request: web.Request, resource_group_name, service_name, api_id, policy_id, api_version, subscription_id) -> web.Response:
    """api_policy_get_entity_tag

    Gets the entity state (Etag) version of the API policy specified by its identifier.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param api_id: API identifier. Must be unique in the current API Management service instance.
    :type api_id: str
    :param policy_id: The identifier of the Policy.
    :type policy_id: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def api_policy_list_by_api(request: web.Request, resource_group_name, service_name, api_id, api_version, subscription_id) -> web.Response:
    """api_policy_list_by_api

    Get the policy configuration at the API level.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param api_id: API identifier. Must be unique in the current API Management service instance.
    :type api_id: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)
