from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.linked_service_list_response import LinkedServiceListResponse
from openapi_server.models.linked_service_resource import LinkedServiceResource
from openapi_server import util


async def linked_services_create_or_update(request: web.Request, subscription_id, resource_group_name, factory_name, linked_service_name, api_version, linked_service, if_match=None) -> web.Response:
    """linked_services_create_or_update

    Creates or updates a linked service.

    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param factory_name: The factory name.
    :type factory_name: str
    :param linked_service_name: The linked service name.
    :type linked_service_name: str
    :param api_version: The API version.
    :type api_version: str
    :param linked_service: Linked service resource definition.
    :type linked_service: dict | bytes
    :param if_match: ETag of the linkedService entity.  Should only be specified for update, for which it should match existing entity or can be * for unconditional update.
    :type if_match: str

    """
    linked_service = LinkedServiceResource.from_dict(linked_service)
    return web.Response(status=200)


async def linked_services_delete(request: web.Request, subscription_id, resource_group_name, factory_name, linked_service_name, api_version) -> web.Response:
    """linked_services_delete

    Deletes a linked service.

    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param factory_name: The factory name.
    :type factory_name: str
    :param linked_service_name: The linked service name.
    :type linked_service_name: str
    :param api_version: The API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def linked_services_get(request: web.Request, subscription_id, resource_group_name, factory_name, linked_service_name, api_version) -> web.Response:
    """linked_services_get

    Gets a linked service.

    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param factory_name: The factory name.
    :type factory_name: str
    :param linked_service_name: The linked service name.
    :type linked_service_name: str
    :param api_version: The API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def linked_services_list_by_factory(request: web.Request, subscription_id, resource_group_name, factory_name, api_version) -> web.Response:
    """linked_services_list_by_factory

    Lists linked services.

    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param factory_name: The factory name.
    :type factory_name: str
    :param api_version: The API version.
    :type api_version: str

    """
    return web.Response(status=200)
