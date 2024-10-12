from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_collection import ApiCollection
from openapi_server.models.api_contract import ApiContract
from openapi_server.models.api_update_contract import ApiUpdateContract
from openapi_server.models.apis_list_by_service_default_response import ApisListByServiceDefaultResponse
from openapi_server import util


async def apis_create_or_update(request: web.Request, resource_group_name, service_name, api_id, api_version, subscription_id, parameters, if_match=None) -> web.Response:
    """apis_create_or_update

    Creates new or updates existing specified API of the API Management service instance.

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
    :param parameters: Create or update parameters.
    :type parameters: dict | bytes
    :param if_match: ETag of the Api Entity. For Create Api Etag should not be specified. For Update Etag should match the existing Entity or it can be * for unconditional update.
    :type if_match: str

    """
    parameters = ApiContract.from_dict(parameters)
    return web.Response(status=200)


async def apis_delete(request: web.Request, resource_group_name, service_name, api_id, if_match, api_version, subscription_id) -> web.Response:
    """apis_delete

    Deletes the specified API of the API Management service instance.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param api_id: API identifier. Must be unique in the current API Management service instance.
    :type api_id: str
    :param if_match: ETag of the API Entity. ETag should match the current entity state from the header response of the GET request or it should be * for unconditional update.
    :type if_match: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def apis_get(request: web.Request, resource_group_name, service_name, api_id, api_version, subscription_id) -> web.Response:
    """apis_get

    Gets the details of the API specified by its identifier.

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


async def apis_list_by_service(request: web.Request, resource_group_name, service_name, api_version, subscription_id, filter=None, top=None, skip=None) -> web.Response:
    """apis_list_by_service

    Lists all APIs of the API Management service instance.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param filter: | Field       | Supported operators    | Supported functions               | |-------------|------------------------|-----------------------------------| | id          | ge, le, eq, ne, gt, lt | substringof, startswith, endswith | | name        | ge, le, eq, ne, gt, lt | substringof, startswith, endswith | | description | ge, le, eq, ne, gt, lt | substringof, startswith, endswith | | serviceUrl  | ge, le, eq, ne, gt, lt | substringof, startswith, endswith | | path        | ge, le, eq, ne, gt, lt | substringof, startswith, endswith |
    :type filter: str
    :param top: Number of records to return.
    :type top: int
    :param skip: Number of records to skip.
    :type skip: int

    """
    return web.Response(status=200)


async def apis_update(request: web.Request, resource_group_name, service_name, api_id, if_match, api_version, subscription_id, parameters) -> web.Response:
    """apis_update

    Updates the specified API of the API Management service instance.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param api_id: API identifier. Must be unique in the current API Management service instance.
    :type api_id: str
    :param if_match: ETag of the API entity. ETag should match the current entity state in the header response of the GET request or it should be * for unconditional update.
    :type if_match: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: API Update Contract parameters.
    :type parameters: dict | bytes

    """
    parameters = ApiUpdateContract.from_dict(parameters)
    return web.Response(status=200)
