from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_version_set_get200_response import ApiVersionSetGet200Response
from openapi_server.models.api_version_set_list_by_service200_response import ApiVersionSetListByService200Response
from openapi_server.models.api_version_set_list_by_service_default_response import ApiVersionSetListByServiceDefaultResponse
from openapi_server.models.api_version_set_update_request import ApiVersionSetUpdateRequest
from openapi_server import util


async def api_version_set_create_or_update(request: web.Request, resource_group_name, service_name, version_set_id, api_version, subscription_id, parameters, if_match=None) -> web.Response:
    """api_version_set_create_or_update

    Creates or Updates a Api Version Set.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param version_set_id: Api Version Set identifier. Must be unique in the current API Management service instance.
    :type version_set_id: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Create or update parameters.
    :type parameters: dict | bytes
    :param if_match: ETag of the Entity. Not required when creating an entity, but required when updating an entity.
    :type if_match: str

    """
    parameters = ApiVersionSetGet200Response.from_dict(parameters)
    return web.Response(status=200)


async def api_version_set_delete(request: web.Request, resource_group_name, service_name, version_set_id, if_match, api_version, subscription_id) -> web.Response:
    """api_version_set_delete

    Deletes specific Api Version Set.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param version_set_id: Api Version Set identifier. Must be unique in the current API Management service instance.
    :type version_set_id: str
    :param if_match: ETag of the Entity. ETag should match the current entity state from the header response of the GET request or it should be * for unconditional update.
    :type if_match: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def api_version_set_get(request: web.Request, resource_group_name, service_name, version_set_id, api_version, subscription_id) -> web.Response:
    """api_version_set_get

    Gets the details of the Api Version Set specified by its identifier.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param version_set_id: Api Version Set identifier. Must be unique in the current API Management service instance.
    :type version_set_id: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def api_version_set_get_entity_tag(request: web.Request, resource_group_name, service_name, version_set_id, api_version, subscription_id) -> web.Response:
    """api_version_set_get_entity_tag

    Gets the entity state (Etag) version of the Api Version Set specified by its identifier.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param version_set_id: Api Version Set identifier. Must be unique in the current API Management service instance.
    :type version_set_id: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def api_version_set_list_by_service(request: web.Request, resource_group_name, service_name, api_version, subscription_id, filter=None, top=None, skip=None) -> web.Response:
    """api_version_set_list_by_service

    Lists a collection of API Version Sets in the specified service instance.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param filter: | Field       | Supported operators    | Supported functions               | |-------------|------------------------|-----------------------------------|   
    :type filter: str
    :param top: Number of records to return.
    :type top: int
    :param skip: Number of records to skip.
    :type skip: int

    """
    return web.Response(status=200)


async def api_version_set_update(request: web.Request, resource_group_name, service_name, version_set_id, if_match, api_version, subscription_id, parameters) -> web.Response:
    """api_version_set_update

    Updates the details of the Api VersionSet specified by its identifier.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param version_set_id: Api Version Set identifier. Must be unique in the current API Management service instance.
    :type version_set_id: str
    :param if_match: ETag of the Entity. ETag should match the current entity state from the header response of the GET request or it should be * for unconditional update.
    :type if_match: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Update parameters.
    :type parameters: dict | bytes

    """
    parameters = ApiVersionSetUpdateRequest.from_dict(parameters)
    return web.Response(status=200)
