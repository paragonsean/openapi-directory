from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_diagnostic_logger_create_or_update200_response import ApiDiagnosticLoggerCreateOrUpdate200Response
from openapi_server.models.api_diagnostic_logger_list_by_service200_response import ApiDiagnosticLoggerListByService200Response
from openapi_server.models.api_list_by_service_default_response import ApiListByServiceDefaultResponse
from openapi_server import util


async def api_diagnostic_logger_check_entity_exists(request: web.Request, resource_group_name, service_name, api_id, diagnostic_id, loggerid, api_version, subscription_id) -> web.Response:
    """api_diagnostic_logger_check_entity_exists

    Checks that logger entity specified by identifier is associated with the diagnostics entity.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param api_id: API identifier. Must be unique in the current API Management service instance.
    :type api_id: str
    :param diagnostic_id: Diagnostic identifier. Must be unique in the current API Management service instance.
    :type diagnostic_id: str
    :param loggerid: Logger identifier. Must be unique in the API Management service instance.
    :type loggerid: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def api_diagnostic_logger_create_or_update(request: web.Request, resource_group_name, service_name, api_id, diagnostic_id, loggerid, api_version, subscription_id) -> web.Response:
    """api_diagnostic_logger_create_or_update

    Attaches a logger to a diagnostic for an API.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param api_id: API identifier. Must be unique in the current API Management service instance.
    :type api_id: str
    :param diagnostic_id: Diagnostic identifier. Must be unique in the current API Management service instance.
    :type diagnostic_id: str
    :param loggerid: Logger identifier. Must be unique in the API Management service instance.
    :type loggerid: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def api_diagnostic_logger_delete(request: web.Request, resource_group_name, service_name, api_id, diagnostic_id, loggerid, api_version, subscription_id) -> web.Response:
    """api_diagnostic_logger_delete

    Deletes the specified Logger from Diagnostic for an API.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param api_id: API identifier. Must be unique in the current API Management service instance.
    :type api_id: str
    :param diagnostic_id: Diagnostic identifier. Must be unique in the current API Management service instance.
    :type diagnostic_id: str
    :param loggerid: Logger identifier. Must be unique in the API Management service instance.
    :type loggerid: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def api_diagnostic_logger_list_by_service(request: web.Request, resource_group_name, service_name, api_id, api_version, subscription_id, diagnostic_id, filter=None, top=None, skip=None) -> web.Response:
    """api_diagnostic_logger_list_by_service

    Lists all loggers associated with the specified Diagnostic of an API.

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
    :param diagnostic_id: Diagnostic identifier. Must be unique in the current API Management service instance.
    :type diagnostic_id: str
    :param filter: | Field       | Supported operators    | Supported functions               | |-------------|------------------------|-----------------------------------| | id          | ge, le, eq, ne, gt, lt | substringof, startswith, endswith | | type        | eq                     |                                   |
    :type filter: str
    :param top: Number of records to return.
    :type top: int
    :param skip: Number of records to skip.
    :type skip: int

    """
    return web.Response(status=200)
