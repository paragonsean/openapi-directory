from typing import List, Dict
from aiohttp import web

from openapi_server.models.apis_list_by_service_default_response import ApisListByServiceDefaultResponse
from openapi_server.models.operation_collection import OperationCollection
from openapi_server.models.operation_contract import OperationContract
from openapi_server.models.operation_update_contract import OperationUpdateContract
from openapi_server import util


async def api_operations_create_or_update(request: web.Request, resource_group_name, service_name, api_id, operation_id, api_version, subscription_id, parameters) -> web.Response:
    """api_operations_create_or_update

    Creates a new API operation or updates an existing one.

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
    :param parameters: Create parameters.
    :type parameters: dict | bytes

    """
    parameters = OperationContract.from_dict(parameters)
    return web.Response(status=200)


async def api_operations_delete(request: web.Request, resource_group_name, service_name, api_id, operation_id, if_match, api_version, subscription_id) -> web.Response:
    """api_operations_delete

    Deletes the specified operation.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param api_id: API identifier. Must be unique in the current API Management service instance.
    :type api_id: str
    :param operation_id: Operation identifier within an API. Must be unique in the current API Management service instance.
    :type operation_id: str
    :param if_match: ETag of the API Operation Entity. ETag should match the current entity state from the header response of the GET request or it should be * for unconditional update.
    :type if_match: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def api_operations_get(request: web.Request, resource_group_name, service_name, api_id, operation_id, api_version, subscription_id) -> web.Response:
    """api_operations_get

    Gets the details of the API Operation specified by its identifier.

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


async def api_operations_list_by_apis(request: web.Request, resource_group_name, service_name, api_id, api_version, subscription_id, filter=None, top=None, skip=None) -> web.Response:
    """api_operations_list_by_apis

    Lists a collection of the operations for the specified API.

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
    :param filter: | Field       | Supported operators    | Supported functions               | |-------------|------------------------|-----------------------------------| | name        | ge, le, eq, ne, gt, lt | substringof, startswith, endswith | | method      | ge, le, eq, ne, gt, lt | substringof, startswith, endswith | | description | ge, le, eq, ne, gt, lt | substringof, startswith, endswith | | urlTemplate | ge, le, eq, ne, gt, lt | substringof, startswith, endswith |
    :type filter: str
    :param top: Number of records to return.
    :type top: int
    :param skip: Number of records to skip.
    :type skip: int

    """
    return web.Response(status=200)


async def api_operations_update(request: web.Request, resource_group_name, service_name, api_id, operation_id, if_match, api_version, subscription_id, parameters) -> web.Response:
    """api_operations_update

    Updates the details of the operation specified by its identifier.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param api_id: API identifier. Must be unique in the current API Management service instance.
    :type api_id: str
    :param operation_id: Operation identifier within an API. Must be unique in the current API Management service instance.
    :type operation_id: str
    :param if_match: ETag of the API Operation Entity. ETag should match the current entity state from the header response of the GET request or it should be * for unconditional update.
    :type if_match: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: API Operation Update parameters.
    :type parameters: dict | bytes

    """
    parameters = OperationUpdateContract.from_dict(parameters)
    return web.Response(status=200)
