from typing import List, Dict
from aiohttp import web

from openapi_server.models.logger_collection import LoggerCollection
from openapi_server.models.logger_create_parameters import LoggerCreateParameters
from openapi_server.models.logger_response import LoggerResponse
from openapi_server.models.logger_update_parameters import LoggerUpdateParameters
from openapi_server.models.loggers_list_by_service_default_response import LoggersListByServiceDefaultResponse
from openapi_server import util


async def loggers_create_or_update(request: web.Request, resource_group_name, service_name, loggerid, api_version, subscription_id, parameters) -> web.Response:
    """loggers_create_or_update

    Creates or Updates a logger.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param loggerid: Logger identifier. Must be unique in the API Management service instance.
    :type loggerid: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Create parameters.
    :type parameters: dict | bytes

    """
    parameters = LoggerCreateParameters.from_dict(parameters)
    return web.Response(status=200)


async def loggers_delete(request: web.Request, resource_group_name, service_name, loggerid, if_match, api_version, subscription_id) -> web.Response:
    """loggers_delete

    Deletes the specified logger.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param loggerid: Logger identifier. Must be unique in the API Management service instance.
    :type loggerid: str
    :param if_match: The entity state (Etag) version of the logger to delete. A value of \&quot;*\&quot; can be used for If-Match to unconditionally apply the operation.
    :type if_match: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def loggers_get(request: web.Request, resource_group_name, service_name, loggerid, api_version, subscription_id) -> web.Response:
    """loggers_get

    Gets the details of the logger specified by its identifier.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param loggerid: Logger identifier. Must be unique in the API Management service instance.
    :type loggerid: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def loggers_list_by_service(request: web.Request, resource_group_name, service_name, api_version, subscription_id, filter=None, top=None, skip=None) -> web.Response:
    """loggers_list_by_service

    Lists a collection of loggers in the specified service instance.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param filter: | Field | Supported operators    | Supported functions                         | |-------|------------------------|---------------------------------------------| | id    | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | type  | eq                     |                                             |
    :type filter: str
    :param top: Number of records to return.
    :type top: int
    :param skip: Number of records to skip.
    :type skip: int

    """
    return web.Response(status=200)


async def loggers_update(request: web.Request, resource_group_name, service_name, loggerid, if_match, api_version, subscription_id, parameters) -> web.Response:
    """loggers_update

    Updates an existing logger.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param loggerid: Logger identifier. Must be unique in the API Management service instance.
    :type loggerid: str
    :param if_match: The entity state (Etag) version of the logger to update. A value of \&quot;*\&quot; can be used for If-Match to unconditionally apply the operation.
    :type if_match: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Update parameters.
    :type parameters: dict | bytes

    """
    parameters = LoggerUpdateParameters.from_dict(parameters)
    return web.Response(status=200)
