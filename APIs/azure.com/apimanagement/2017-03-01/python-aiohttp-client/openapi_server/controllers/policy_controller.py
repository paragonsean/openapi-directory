from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.policy_collection import PolicyCollection
from openapi_server.models.policy_contract import PolicyContract
from openapi_server import util


async def policy_create_or_update(request: web.Request, resource_group_name, service_name, policy_id, api_version, subscription_id, parameters) -> web.Response:
    """policy_create_or_update

    Creates or updates the global policy configuration of the Api Management service.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param policy_id: The identifier of the Policy.
    :type policy_id: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: The policy contents to apply.
    :type parameters: dict | bytes

    """
    parameters = PolicyContract.from_dict(parameters)
    return web.Response(status=200)


async def policy_delete(request: web.Request, resource_group_name, service_name, policy_id, if_match, api_version, subscription_id) -> web.Response:
    """policy_delete

    Deletes the global policy configuration of the Api Management Service.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param policy_id: The identifier of the Policy.
    :type policy_id: str
    :param if_match: The entity state (Etag) version of the policy to be deleted. A value of \&quot;*\&quot; can be used for If-Match to unconditionally apply the operation.
    :type if_match: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def policy_get(request: web.Request, resource_group_name, service_name, policy_id, api_version, subscription_id) -> web.Response:
    """policy_get

    Get the Global policy definition of the Api Management service.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param policy_id: The identifier of the Policy.
    :type policy_id: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def policy_list_by_service(request: web.Request, resource_group_name, service_name, api_version, subscription_id, scope=None) -> web.Response:
    """policy_list_by_service

    Lists all the Global Policy definitions of the Api Management service.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param scope: Policy scope.
    :type scope: str

    """
    return web.Response(status=200)
