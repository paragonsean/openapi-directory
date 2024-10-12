from typing import List, Dict
from aiohttp import web

from openapi_server.models.open_id_connect_provider_get200_response import OpenIdConnectProviderGet200Response
from openapi_server.models.open_id_connect_provider_list_by_service200_response import OpenIdConnectProviderListByService200Response
from openapi_server.models.open_id_connect_provider_list_by_service_default_response import OpenIdConnectProviderListByServiceDefaultResponse
from openapi_server.models.open_id_connect_provider_update_request import OpenIdConnectProviderUpdateRequest
from openapi_server import util


async def open_id_connect_provider_create_or_update(request: web.Request, resource_group_name, service_name, opid, api_version, subscription_id, parameters, if_match=None) -> web.Response:
    """open_id_connect_provider_create_or_update

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
    :param if_match: ETag of the Entity. Not required when creating an entity, but required when updating an entity.
    :type if_match: str

    """
    parameters = OpenIdConnectProviderGet200Response.from_dict(parameters)
    return web.Response(status=200)


async def open_id_connect_provider_delete(request: web.Request, resource_group_name, service_name, opid, if_match, api_version, subscription_id) -> web.Response:
    """open_id_connect_provider_delete

    Deletes specific OpenID Connect Provider of the API Management service instance.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param opid: Identifier of the OpenID Connect Provider.
    :type opid: str
    :param if_match: ETag of the Entity. ETag should match the current entity state from the header response of the GET request or it should be * for unconditional update.
    :type if_match: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def open_id_connect_provider_get(request: web.Request, resource_group_name, service_name, opid, api_version, subscription_id) -> web.Response:
    """open_id_connect_provider_get

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


async def open_id_connect_provider_get_entity_tag(request: web.Request, resource_group_name, service_name, opid, api_version, subscription_id) -> web.Response:
    """open_id_connect_provider_get_entity_tag

    Gets the entity state (Etag) version of the openIdConnectProvider specified by its identifier.

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


async def open_id_connect_provider_list_by_service(request: web.Request, resource_group_name, service_name, api_version, subscription_id, filter=None, top=None, skip=None) -> web.Response:
    """open_id_connect_provider_list_by_service

    Lists of all the OpenId Connect Providers.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param filter: | Field       | Supported operators    | Supported functions               | |-------------|------------------------|-----------------------------------|   |name | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith| |displayName | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith| 
    :type filter: str
    :param top: Number of records to return.
    :type top: int
    :param skip: Number of records to skip.
    :type skip: int

    """
    return web.Response(status=200)


async def open_id_connect_provider_update(request: web.Request, resource_group_name, service_name, opid, if_match, api_version, subscription_id, parameters) -> web.Response:
    """open_id_connect_provider_update

    Updates the specific OpenID Connect Provider.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param opid: Identifier of the OpenID Connect Provider.
    :type opid: str
    :param if_match: ETag of the Entity. ETag should match the current entity state from the header response of the GET request or it should be * for unconditional update.
    :type if_match: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Update parameters.
    :type parameters: dict | bytes

    """
    parameters = OpenIdConnectProviderUpdateRequest.from_dict(parameters)
    return web.Response(status=200)
