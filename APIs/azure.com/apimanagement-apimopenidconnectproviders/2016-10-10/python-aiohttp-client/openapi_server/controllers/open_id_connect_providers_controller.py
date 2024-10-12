from typing import List, Dict
from aiohttp import web

from openapi_server.models.open_id_connect_provider_collection import OpenIdConnectProviderCollection
from openapi_server.models.open_id_connect_providers_get_default_response import OpenIdConnectProvidersGetDefaultResponse
from openapi_server.models.openid_connect_provider_contract import OpenidConnectProviderContract
from openapi_server.models.openid_connect_provider_create_contract import OpenidConnectProviderCreateContract
from openapi_server.models.openid_connect_provider_update_contract import OpenidConnectProviderUpdateContract
from openapi_server import util


async def open_id_connect_providers_create_or_update(request: web.Request, resource_group_name, service_name, opid, api_version, subscription_id, parameters) -> web.Response:
    """open_id_connect_providers_create_or_update

    Creates or updates the OpenID Connect Provider.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param opid: Identifier of the OpenID Connect Provider.
    :type opid: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Create parameters.
    :type parameters: dict | bytes

    """
    parameters = OpenidConnectProviderCreateContract.from_dict(parameters)
    return web.Response(status=200)


async def open_id_connect_providers_delete(request: web.Request, resource_group_name, service_name, opid, if_match, api_version, subscription_id) -> web.Response:
    """open_id_connect_providers_delete

    Deletes specific OpenID Connect Provider of the API Management service instance.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param opid: Identifier of the OpenID Connect Provider.
    :type opid: str
    :param if_match: The entity state (Etag) version of the OpenID Connect Provider to delete. A value of \&quot;*\&quot; can be used for If-Match to unconditionally apply the operation.
    :type if_match: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def open_id_connect_providers_get(request: web.Request, resource_group_name, service_name, opid, api_version, subscription_id) -> web.Response:
    """open_id_connect_providers_get

    Gets specific OpenID Connect Provider.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param opid: Identifier of the OpenID Connect Provider.
    :type opid: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def open_id_connect_providers_list_by_service(request: web.Request, resource_group_name, service_name, api_version, subscription_id, filter=None, top=None, skip=None) -> web.Response:
    """open_id_connect_providers_list_by_service

    Lists all OpenID Connect Providers.

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


async def open_id_connect_providers_update(request: web.Request, resource_group_name, service_name, opid, if_match, api_version, subscription_id, parameters) -> web.Response:
    """open_id_connect_providers_update

    Updates the specific OpenID Connect Provider.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param opid: Identifier of the OpenID Connect Provider.
    :type opid: str
    :param if_match: The entity state (Etag) version of the OpenID Connect Provider to update. A value of \&quot;*\&quot; can be used for If-Match to unconditionally apply the operation.
    :type if_match: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Update parameters.
    :type parameters: dict | bytes

    """
    parameters = OpenidConnectProviderUpdateContract.from_dict(parameters)
    return web.Response(status=200)
