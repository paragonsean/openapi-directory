from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.factory import Factory
from openapi_server.models.factory_list_response import FactoryListResponse
from openapi_server.models.factory_update_parameters import FactoryUpdateParameters
from openapi_server import util


async def factories_create_or_update(request: web.Request, subscription_id, resource_group_name, factory_name, api_version, factory) -> web.Response:
    """factories_create_or_update

    Creates or updates a factory.

    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param factory_name: The factory name.
    :type factory_name: str
    :param api_version: The API version.
    :type api_version: str
    :param factory: Factory resource definition.
    :type factory: dict | bytes

    """
    factory = Factory.from_dict(factory)
    return web.Response(status=200)


async def factories_delete(request: web.Request, subscription_id, resource_group_name, factory_name, api_version) -> web.Response:
    """factories_delete

    Deletes a factory.

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


async def factories_get(request: web.Request, subscription_id, resource_group_name, factory_name, api_version) -> web.Response:
    """factories_get

    Gets a factory.

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


async def factories_list(request: web.Request, subscription_id, api_version) -> web.Response:
    """factories_list

    Lists factories under the specified subscription.

    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param api_version: The API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def factories_list_by_resource_group(request: web.Request, subscription_id, resource_group_name, api_version) -> web.Response:
    """factories_list_by_resource_group

    Lists factories.

    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param api_version: The API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def factories_update(request: web.Request, subscription_id, resource_group_name, factory_name, api_version, factory_update_parameters) -> web.Response:
    """factories_update

    Updates a factory.

    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param factory_name: The factory name.
    :type factory_name: str
    :param api_version: The API version.
    :type api_version: str
    :param factory_update_parameters: The parameters for updating a factory.
    :type factory_update_parameters: dict | bytes

    """
    factory_update_parameters = FactoryUpdateParameters.from_dict(factory_update_parameters)
    return web.Response(status=200)
