from typing import List, Dict
from aiohttp import web

from openapi_server.models.directory_tenant import DirectoryTenant
from openapi_server.models.directory_tenant_list import DirectoryTenantList
from openapi_server import util


async def directory_tenants_create_or_update(request: web.Request, subscription_id, resource_group_name, tenant, api_version, new_tenant) -> web.Response:
    """directory_tenants_create_or_update

    Create or updates a directory tenant.

    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The resource group the resource is located under.
    :type resource_group_name: str
    :param tenant: Directory tenant name.
    :type tenant: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param new_tenant: New directory tenant properties.
    :type new_tenant: dict | bytes

    """
    new_tenant = DirectoryTenant.from_dict(new_tenant)
    return web.Response(status=200)


async def directory_tenants_delete(request: web.Request, subscription_id, resource_group_name, tenant, api_version) -> web.Response:
    """directory_tenants_delete

    Delete a directory tenant under a resource group.

    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The resource group the resource is located under.
    :type resource_group_name: str
    :param tenant: Directory tenant name.
    :type tenant: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def directory_tenants_get(request: web.Request, subscription_id, resource_group_name, tenant, api_version) -> web.Response:
    """directory_tenants_get

    Get a directory tenant by name.

    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The resource group the resource is located under.
    :type resource_group_name: str
    :param tenant: Directory tenant name.
    :type tenant: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def directory_tenants_list(request: web.Request, subscription_id, resource_group_name, api_version) -> web.Response:
    """directory_tenants_list

    Lists all the directory tenants under the current subscription and given resource group name.

    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The resource group the resource is located under.
    :type resource_group_name: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)
