from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.private_link_resource import PrivateLinkResource
from openapi_server.models.private_link_resource_list_result import PrivateLinkResourceListResult
from openapi_server import util


async def private_link_resources_get(request: web.Request, subscription_id, resource_group_name, config_store_name, api_version, group_name) -> web.Response:
    """private_link_resources_get

    Gets a private link resource that need to be created for a configuration store.

    :param subscription_id: The Microsoft Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group to which the container registry belongs.
    :type resource_group_name: str
    :param config_store_name: The name of the configuration store.
    :type config_store_name: str
    :param api_version: The client API version.
    :type api_version: str
    :param group_name: The name of the private link resource group.
    :type group_name: str

    """
    return web.Response(status=200)


async def private_link_resources_list_by_configuration_store(request: web.Request, subscription_id, resource_group_name, config_store_name, api_version) -> web.Response:
    """private_link_resources_list_by_configuration_store

    Gets the private link resources that need to be created for a configuration store.

    :param subscription_id: The Microsoft Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group to which the container registry belongs.
    :type resource_group_name: str
    :param config_store_name: The name of the configuration store.
    :type config_store_name: str
    :param api_version: The client API version.
    :type api_version: str

    """
    return web.Response(status=200)
