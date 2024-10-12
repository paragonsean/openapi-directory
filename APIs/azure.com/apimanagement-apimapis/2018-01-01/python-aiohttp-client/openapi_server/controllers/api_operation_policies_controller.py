from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_list_by_service_default_response import ApiListByServiceDefaultResponse
from openapi_server.models.api_operation_policy_get200_response import ApiOperationPolicyGet200Response
from openapi_server.models.api_operation_policy_list_by_operation200_response import ApiOperationPolicyListByOperation200Response
from openapi_server import util


async def api_operation_policy_create_or_update(request: web.Request, resource_group_name, service_name, api_id, operation_id, policy_id, api_version, subscription_id, parameters, if_match=None) -> web.Response:
    """api_operation_policy_create_or_update

    Creates or updates policy configuration for the API Operation level.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param api_id: API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev&#x3D;n as a suffix where n is the revision number.
    :type api_id: str
    :param operation_id: Operation identifier within an API. Must be unique in the current API Management service instance.
    :type operation_id: str
    :param policy_id: The identifier of the Policy.
    :type policy_id: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: The policy contents to apply.
    :type parameters: dict | bytes
    :param if_match: ETag of the Entity. Not required when creating an entity, but required when updating an entity.
    :type if_match: str

    """
    parameters = ApiOperationPolicyGet200Response.from_dict(parameters)
    return web.Response(status=200)


async def api_operation_policy_delete(request: web.Request, resource_group_name, service_name, api_id, operation_id, if_match, policy_id, api_version, subscription_id) -> web.Response:
    """api_operation_policy_delete

    Deletes the policy configuration at the Api Operation.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param api_id: API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev&#x3D;n as a suffix where n is the revision number.
    :type api_id: str
    :param operation_id: Operation identifier within an API. Must be unique in the current API Management service instance.
    :type operation_id: str
    :param if_match: ETag of the Entity. ETag should match the current entity state from the header response of the GET request or it should be * for unconditional update.
    :type if_match: str
    :param policy_id: The identifier of the Policy.
    :type policy_id: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def api_operation_policy_get(request: web.Request, resource_group_name, service_name, api_id, operation_id, policy_id, api_version, subscription_id) -> web.Response:
    """api_operation_policy_get

    Get the policy configuration at the API Operation level.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param api_id: API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev&#x3D;n as a suffix where n is the revision number.
    :type api_id: str
    :param operation_id: Operation identifier within an API. Must be unique in the current API Management service instance.
    :type operation_id: str
    :param policy_id: The identifier of the Policy.
    :type policy_id: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def api_operation_policy_get_entity_tag(request: web.Request, resource_group_name, service_name, api_id, operation_id, policy_id, api_version, subscription_id) -> web.Response:
    """api_operation_policy_get_entity_tag

    Gets the entity state (Etag) version of the API operation policy specified by its identifier.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param api_id: API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev&#x3D;n as a suffix where n is the revision number.
    :type api_id: str
    :param operation_id: Operation identifier within an API. Must be unique in the current API Management service instance.
    :type operation_id: str
    :param policy_id: The identifier of the Policy.
    :type policy_id: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def api_operation_policy_list_by_operation(request: web.Request, resource_group_name, service_name, api_id, operation_id, api_version, subscription_id) -> web.Response:
    """api_operation_policy_list_by_operation

    Get the list of policy configuration at the API Operation level.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param api_id: API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev&#x3D;n as a suffix where n is the revision number.
    :type api_id: str
    :param operation_id: Operation identifier within an API. Must be unique in the current API Management service instance.
    :type operation_id: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)
