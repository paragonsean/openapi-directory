from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_diagnostic_get200_response import ApiDiagnosticGet200Response
from openapi_server.models.api_diagnostic_list_by_service200_response import ApiDiagnosticListByService200Response
from openapi_server.models.api_list_by_service_default_response import ApiListByServiceDefaultResponse
from openapi_server import util


async def api_diagnostic_create_or_update(request: web.Request, resource_group_name, service_name, api_id, diagnostic_id, api_version, subscription_id, parameters, if_match=None) -> web.Response:
    """api_diagnostic_create_or_update

    Creates a new Diagnostic for an API or updates an existing one.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param api_id: API identifier. Must be unique in the current API Management service instance.
    :type api_id: str
    :param diagnostic_id: Diagnostic identifier. Must be unique in the current API Management service instance.
    :type diagnostic_id: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Create parameters.
    :type parameters: dict | bytes
    :param if_match: ETag of the Entity. Not required when creating an entity, but required when updating an entity.
    :type if_match: str

    """
    parameters = ApiDiagnosticGet200Response.from_dict(parameters)
    return web.Response(status=200)


async def api_diagnostic_delete(request: web.Request, resource_group_name, service_name, api_id, diagnostic_id, if_match, api_version, subscription_id) -> web.Response:
    """api_diagnostic_delete

    Deletes the specified Diagnostic from an API.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param api_id: API identifier. Must be unique in the current API Management service instance.
    :type api_id: str
    :param diagnostic_id: Diagnostic identifier. Must be unique in the current API Management service instance.
    :type diagnostic_id: str
    :param if_match: ETag of the Entity. ETag should match the current entity state from the header response of the GET request or it should be * for unconditional update.
    :type if_match: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def api_diagnostic_get(request: web.Request, resource_group_name, service_name, api_id, diagnostic_id, api_version, subscription_id) -> web.Response:
    """api_diagnostic_get

    Gets the details of the Diagnostic for an API specified by its identifier.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param api_id: API identifier. Must be unique in the current API Management service instance.
    :type api_id: str
    :param diagnostic_id: Diagnostic identifier. Must be unique in the current API Management service instance.
    :type diagnostic_id: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def api_diagnostic_get_entity_tag(request: web.Request, resource_group_name, service_name, api_id, diagnostic_id, api_version, subscription_id) -> web.Response:
    """api_diagnostic_get_entity_tag

    Gets the entity state (Etag) version of the Diagnostic for an API specified by its identifier.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param api_id: API identifier. Must be unique in the current API Management service instance.
    :type api_id: str
    :param diagnostic_id: Diagnostic identifier. Must be unique in the current API Management service instance.
    :type diagnostic_id: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def api_diagnostic_list_by_service(request: web.Request, resource_group_name, service_name, api_id, api_version, subscription_id, filter=None, top=None, skip=None) -> web.Response:
    """api_diagnostic_list_by_service

    Lists all diagnostics of an API.

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
    :param filter: | Field       | Supported operators    | Supported functions               | |-------------|------------------------|-----------------------------------|   |name | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith| 
    :type filter: str
    :param top: Number of records to return.
    :type top: int
    :param skip: Number of records to skip.
    :type skip: int

    """
    return web.Response(status=200)


async def api_diagnostic_update(request: web.Request, resource_group_name, service_name, api_id, diagnostic_id, if_match, api_version, subscription_id, parameters) -> web.Response:
    """api_diagnostic_update

    Updates the details of the Diagnostic for an API specified by its identifier.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param api_id: API identifier. Must be unique in the current API Management service instance.
    :type api_id: str
    :param diagnostic_id: Diagnostic identifier. Must be unique in the current API Management service instance.
    :type diagnostic_id: str
    :param if_match: ETag of the Entity. ETag should match the current entity state from the header response of the GET request or it should be * for unconditional update.
    :type if_match: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Diagnostic Update parameters.
    :type parameters: dict | bytes

    """
    parameters = ApiDiagnosticGet200Response.from_dict(parameters)
    return web.Response(status=200)
