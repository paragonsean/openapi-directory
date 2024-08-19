from typing import List, Dict
from aiohttp import web

from openapi_server.models.logger_get200_response import LoggerGet200Response
from openapi_server.models.logger_list_by_service200_response import LoggerListByService200Response
from openapi_server.models.logger_list_by_service_default_response import LoggerListByServiceDefaultResponse
from openapi_server.models.logger_update_request import LoggerUpdateRequest
from openapi_server import util


async def logger_create_or_update(request: web.Request, resource_group_name, service_name, logger_id, api_version, subscription_id, parameters, if_match=None) -> web.Response:
    """logger_create_or_update

    Creates or Updates a logger.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param logger_id: Logger identifier. Must be unique in the API Management service instance.
    :type logger_id: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Create parameters.
    :type parameters: dict | bytes
    :param if_match: ETag of the Entity. Not required when creating an entity, but required when updating an entity.
    :type if_match: str

    """
    parameters = LoggerGet200Response.from_dict(parameters)
    return web.Response(status=200)


async def logger_delete(request: web.Request, resource_group_name, service_name, logger_id, if_match, api_version, subscription_id, force=None) -> web.Response:
    """logger_delete

    Deletes the specified logger.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param logger_id: Logger identifier. Must be unique in the API Management service instance.
    :type logger_id: str
    :param if_match: ETag of the Entity. ETag should match the current entity state from the header response of the GET request or it should be * for unconditional update.
    :type if_match: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param force: Force deletion even if diagnostic is attached.
    :type force: bool

    """
    return web.Response(status=200)


async def logger_get(request: web.Request, resource_group_name, service_name, logger_id, api_version, subscription_id) -> web.Response:
    """logger_get

    Gets the details of the logger specified by its identifier.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param logger_id: Logger identifier. Must be unique in the API Management service instance.
    :type logger_id: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def logger_get_entity_tag(request: web.Request, resource_group_name, service_name, logger_id, api_version, subscription_id) -> web.Response:
    """logger_get_entity_tag

    Gets the entity state (Etag) version of the logger specified by its identifier.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param logger_id: Logger identifier. Must be unique in the API Management service instance.
    :type logger_id: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def logger_list_by_service(request: web.Request, resource_group_name, service_name, api_version, subscription_id, filter=None, top=None, skip=None) -> web.Response:
    """logger_list_by_service

    Lists a collection of loggers in the specified service instance.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param filter: | Field       | Supported operators    | Supported functions               | |-------------|------------------------|-----------------------------------|   |name | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith| |description | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith| |loggerType | eq |    | |resourceId | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith| 
    :type filter: str
    :param top: Number of records to return.
    :type top: int
    :param skip: Number of records to skip.
    :type skip: int

    """
    return web.Response(status=200)


async def logger_update(request: web.Request, resource_group_name, service_name, logger_id, if_match, api_version, subscription_id, parameters) -> web.Response:
    """logger_update

    Updates an existing logger.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param logger_id: Logger identifier. Must be unique in the API Management service instance.
    :type logger_id: str
    :param if_match: ETag of the Entity. ETag should match the current entity state from the header response of the GET request or it should be * for unconditional update.
    :type if_match: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Update parameters.
    :type parameters: dict | bytes

    """
    parameters = LoggerUpdateRequest.from_dict(parameters)
    return web.Response(status=200)
