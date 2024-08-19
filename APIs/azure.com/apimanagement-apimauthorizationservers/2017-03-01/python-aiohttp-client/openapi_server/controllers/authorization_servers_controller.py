from typing import List, Dict
from aiohttp import web

from openapi_server.models.authorization_server_collection import AuthorizationServerCollection
from openapi_server.models.authorization_server_contract import AuthorizationServerContract
from openapi_server.models.authorization_server_get_default_response import AuthorizationServerGetDefaultResponse
from openapi_server.models.authorization_server_update_contract import AuthorizationServerUpdateContract
from openapi_server import util


async def authorization_server_create_or_update(request: web.Request, resource_group_name, service_name, authsid, api_version, subscription_id, parameters) -> web.Response:
    """authorization_server_create_or_update

    Creates new authorization server or updates an existing authorization server.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param authsid: Identifier of the authorization server.
    :type authsid: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Create or update parameters.
    :type parameters: dict | bytes

    """
    parameters = AuthorizationServerContract.from_dict(parameters)
    return web.Response(status=200)


async def authorization_server_delete(request: web.Request, resource_group_name, service_name, authsid, if_match, api_version, subscription_id) -> web.Response:
    """authorization_server_delete

    Deletes specific authorization server instance.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param authsid: Identifier of the authorization server.
    :type authsid: str
    :param if_match: The entity state (Etag) version of the authentication server to delete. A value of \&quot;*\&quot; can be used for If-Match to unconditionally apply the operation.
    :type if_match: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def authorization_server_get(request: web.Request, resource_group_name, service_name, authsid, api_version, subscription_id) -> web.Response:
    """authorization_server_get

    Gets the details of the authorization server specified by its identifier.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param authsid: Identifier of the authorization server.
    :type authsid: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def authorization_server_get_entity_tag(request: web.Request, resource_group_name, service_name, authsid, api_version, subscription_id) -> web.Response:
    """authorization_server_get_entity_tag

    Gets the entity state (Etag) version of the authorizationServer specified by its identifier.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param authsid: Identifier of the authorization server.
    :type authsid: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def authorization_server_list_by_service(request: web.Request, resource_group_name, service_name, api_version, subscription_id, filter=None, top=None, skip=None) -> web.Response:
    """authorization_server_list_by_service

    Lists a collection of authorization servers defined within a service instance.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param filter: | Field | Supported operators    | Supported functions                         | |-------|------------------------|---------------------------------------------| | id    | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | name  | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith |
    :type filter: str
    :param top: Number of records to return.
    :type top: int
    :param skip: Number of records to skip.
    :type skip: int

    """
    return web.Response(status=200)


async def authorization_server_update(request: web.Request, resource_group_name, service_name, authsid, if_match, api_version, subscription_id, parameters) -> web.Response:
    """authorization_server_update

    Updates the details of the authorization server specified by its identifier.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param authsid: Identifier of the authorization server.
    :type authsid: str
    :param if_match: The entity state (Etag) version of the authorization server to update. A value of \&quot;*\&quot; can be used for If-Match to unconditionally apply the operation.
    :type if_match: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: OAuth2 Server settings Update parameters.
    :type parameters: dict | bytes

    """
    parameters = AuthorizationServerUpdateContract.from_dict(parameters)
    return web.Response(status=200)
