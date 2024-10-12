from typing import List, Dict
from aiohttp import web

from openapi_server.models.address_response import AddressResponse
from openapi_server.models.hosting_environment import HostingEnvironment
from openapi_server.models.hosting_environment_collection import HostingEnvironmentCollection
from openapi_server.models.managed_hosting_environment import ManagedHostingEnvironment
from openapi_server.models.server_farm_collection import ServerFarmCollection
from openapi_server.models.site_collection import SiteCollection
from openapi_server import util


async def managed_hosting_environments_create_or_update_managed_hosting_environment(request: web.Request, resource_group_name, name, subscription_id, api_version, managed_hosting_environment_envelope) -> web.Response:
    """Create or update a managed hosting environment.

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of managed hosting environment
    :type name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param managed_hosting_environment_envelope: Properties of managed hosting environment
    :type managed_hosting_environment_envelope: dict | bytes

    """
    managed_hosting_environment_envelope = HostingEnvironment.from_dict(managed_hosting_environment_envelope)
    return web.Response(status=200)


async def managed_hosting_environments_delete_managed_hosting_environment(request: web.Request, resource_group_name, name, subscription_id, api_version, force_delete=None) -> web.Response:
    """Delete a managed hosting environment.

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of managed hosting environment
    :type name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param force_delete: Delete even if the managed hosting environment contains resources
    :type force_delete: bool

    """
    return web.Response(status=200)


async def managed_hosting_environments_get_managed_hosting_environment(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """Get properties of a managed hosting environment.

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of managed hosting environment
    :type name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def managed_hosting_environments_get_managed_hosting_environment_operation(request: web.Request, resource_group_name, name, operation_id, subscription_id, api_version) -> web.Response:
    """Get status of an operation on a managed hosting environment.

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of managed hosting environment
    :type name: str
    :param operation_id: operation identifier GUID
    :type operation_id: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def managed_hosting_environments_get_managed_hosting_environment_server_farms(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """Get all serverfarms (App Service Plans) on the managed hosting environment.

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of managed hosting environment
    :type name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def managed_hosting_environments_get_managed_hosting_environment_sites(request: web.Request, resource_group_name, name, subscription_id, api_version, properties_to_include=None) -> web.Response:
    """Get all sites on the managed hosting environment.

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of managed hosting environment
    :type name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param properties_to_include: Comma separated list of site properties to include
    :type properties_to_include: str

    """
    return web.Response(status=200)


async def managed_hosting_environments_get_managed_hosting_environment_vips(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """Get list of ip addresses assigned to a managed hosting environment

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of managed hosting environment
    :type name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def managed_hosting_environments_get_managed_hosting_environment_web_hosting_plans(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """Get all serverfarms (App Service Plans) on the managed hosting environment.

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of managed hosting environment
    :type name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def managed_hosting_environments_get_managed_hosting_environments(request: web.Request, resource_group_name, subscription_id, api_version) -> web.Response:
    """Get all managed hosting environments in a resource group.

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)
