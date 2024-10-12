from typing import List, Dict
from aiohttp import web

from openapi_server.models.scope_map import ScopeMap
from openapi_server.models.scope_map_list_result import ScopeMapListResult
from openapi_server.models.scope_map_update_parameters import ScopeMapUpdateParameters
from openapi_server import util


async def scope_maps_create(request: web.Request, api_version, subscription_id, resource_group_name, registry_name, scope_map_name, scope_map_create_parameters) -> web.Response:
    """scope_maps_create

    Creates a scope map for a container registry with the specified parameters.

    :param api_version: The client API version.
    :type api_version: str
    :param subscription_id: The Microsoft Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group to which the container registry belongs.
    :type resource_group_name: str
    :param registry_name: The name of the container registry.
    :type registry_name: str
    :param scope_map_name: The name of the scope map.
    :type scope_map_name: str
    :param scope_map_create_parameters: The parameters for creating a scope map.
    :type scope_map_create_parameters: dict | bytes

    """
    scope_map_create_parameters = ScopeMap.from_dict(scope_map_create_parameters)
    return web.Response(status=200)


async def scope_maps_delete(request: web.Request, api_version, subscription_id, resource_group_name, registry_name, scope_map_name) -> web.Response:
    """scope_maps_delete

    Deletes a scope map from a container registry.

    :param api_version: The client API version.
    :type api_version: str
    :param subscription_id: The Microsoft Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group to which the container registry belongs.
    :type resource_group_name: str
    :param registry_name: The name of the container registry.
    :type registry_name: str
    :param scope_map_name: The name of the scope map.
    :type scope_map_name: str

    """
    return web.Response(status=200)


async def scope_maps_get(request: web.Request, api_version, subscription_id, resource_group_name, registry_name, scope_map_name) -> web.Response:
    """scope_maps_get

    Gets the properties of the specified scope map.

    :param api_version: The client API version.
    :type api_version: str
    :param subscription_id: The Microsoft Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group to which the container registry belongs.
    :type resource_group_name: str
    :param registry_name: The name of the container registry.
    :type registry_name: str
    :param scope_map_name: The name of the scope map.
    :type scope_map_name: str

    """
    return web.Response(status=200)


async def scope_maps_list(request: web.Request, api_version, subscription_id, resource_group_name, registry_name) -> web.Response:
    """scope_maps_list

    Lists all the scope maps for the specified container registry.

    :param api_version: The client API version.
    :type api_version: str
    :param subscription_id: The Microsoft Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group to which the container registry belongs.
    :type resource_group_name: str
    :param registry_name: The name of the container registry.
    :type registry_name: str

    """
    return web.Response(status=200)


async def scope_maps_update(request: web.Request, api_version, subscription_id, resource_group_name, registry_name, scope_map_name, scope_map_update_parameters) -> web.Response:
    """scope_maps_update

    Updates a scope map with the specified parameters.

    :param api_version: The client API version.
    :type api_version: str
    :param subscription_id: The Microsoft Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group to which the container registry belongs.
    :type resource_group_name: str
    :param registry_name: The name of the container registry.
    :type registry_name: str
    :param scope_map_name: The name of the scope map.
    :type scope_map_name: str
    :param scope_map_update_parameters: The parameters for updating a scope map.
    :type scope_map_update_parameters: dict | bytes

    """
    scope_map_update_parameters = ScopeMapUpdateParameters.from_dict(scope_map_update_parameters)
    return web.Response(status=200)
