from typing import List, Dict
from aiohttp import web

from openapi_server.models.cache_get200_response import CacheGet200Response
from openapi_server.models.cache_list_by_service200_response import CacheListByService200Response
from openapi_server.models.cache_list_by_service_default_response import CacheListByServiceDefaultResponse
from openapi_server.models.cache_update_request import CacheUpdateRequest
from openapi_server import util


async def cache_create_or_update(request: web.Request, resource_group_name, service_name, cache_id, api_version, subscription_id, parameters, if_match=None) -> web.Response:
    """cache_create_or_update

    Creates or updates an External Cache to be used in Api Management instance.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param cache_id: Identifier of the Cache entity. Cache identifier (should be either &#39;default&#39; or valid Azure region identifier).
    :type cache_id: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Create or Update parameters.
    :type parameters: dict | bytes
    :param if_match: ETag of the Entity. Not required when creating an entity, but required when updating an entity.
    :type if_match: str

    """
    parameters = CacheGet200Response.from_dict(parameters)
    return web.Response(status=200)


async def cache_delete(request: web.Request, resource_group_name, service_name, cache_id, if_match, api_version, subscription_id) -> web.Response:
    """cache_delete

    Deletes specific Cache.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param cache_id: Identifier of the Cache entity. Cache identifier (should be either &#39;default&#39; or valid Azure region identifier).
    :type cache_id: str
    :param if_match: ETag of the Entity. ETag should match the current entity state from the header response of the GET request or it should be * for unconditional update.
    :type if_match: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def cache_get(request: web.Request, resource_group_name, service_name, cache_id, api_version, subscription_id) -> web.Response:
    """cache_get

    Gets the details of the Cache specified by its identifier.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param cache_id: Identifier of the Cache entity. Cache identifier (should be either &#39;default&#39; or valid Azure region identifier).
    :type cache_id: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def cache_get_entity_tag(request: web.Request, resource_group_name, service_name, cache_id, api_version, subscription_id) -> web.Response:
    """cache_get_entity_tag

    Gets the entity state (Etag) version of the Cache specified by its identifier.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param cache_id: Identifier of the Cache entity. Cache identifier (should be either &#39;default&#39; or valid Azure region identifier).
    :type cache_id: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def cache_list_by_service(request: web.Request, resource_group_name, service_name, api_version, subscription_id, top=None, skip=None) -> web.Response:
    """cache_list_by_service

    Lists a collection of all external Caches in the specified service instance.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param top: Number of records to return.
    :type top: int
    :param skip: Number of records to skip.
    :type skip: int

    """
    return web.Response(status=200)


async def cache_update(request: web.Request, resource_group_name, service_name, cache_id, if_match, api_version, subscription_id, parameters) -> web.Response:
    """cache_update

    Updates the details of the cache specified by its identifier.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param cache_id: Identifier of the Cache entity. Cache identifier (should be either &#39;default&#39; or valid Azure region identifier).
    :type cache_id: str
    :param if_match: ETag of the Entity. ETag should match the current entity state from the header response of the GET request or it should be * for unconditional update.
    :type if_match: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Update parameters.
    :type parameters: dict | bytes

    """
    parameters = CacheUpdateRequest.from_dict(parameters)
    return web.Response(status=200)
