from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.storage_domain import StorageDomain
from openapi_server.models.storage_domain_list import StorageDomainList
from openapi_server import util


async def storage_domains_create_or_update(request: web.Request, storage_domain_name, subscription_id, resource_group_name, manager_name, api_version, storage_domain) -> web.Response:
    """storage_domains_create_or_update

    Creates or updates the storage domain.

    :param storage_domain_name: The storage domain name.
    :type storage_domain_name: str
    :param subscription_id: The subscription id
    :type subscription_id: str
    :param resource_group_name: The resource group name
    :type resource_group_name: str
    :param manager_name: The manager name
    :type manager_name: str
    :param api_version: The api version
    :type api_version: str
    :param storage_domain: The storageDomain.
    :type storage_domain: dict | bytes

    """
    storage_domain = StorageDomain.from_dict(storage_domain)
    return web.Response(status=200)


async def storage_domains_delete(request: web.Request, storage_domain_name, subscription_id, resource_group_name, manager_name, api_version) -> web.Response:
    """storage_domains_delete

    Deletes the storage domain.

    :param storage_domain_name: The storage domain name.
    :type storage_domain_name: str
    :param subscription_id: The subscription id
    :type subscription_id: str
    :param resource_group_name: The resource group name
    :type resource_group_name: str
    :param manager_name: The manager name
    :type manager_name: str
    :param api_version: The api version
    :type api_version: str

    """
    return web.Response(status=200)


async def storage_domains_get(request: web.Request, storage_domain_name, subscription_id, resource_group_name, manager_name, api_version) -> web.Response:
    """storage_domains_get

    Returns the properties of the specified storage domain name.

    :param storage_domain_name: The storage domain name.
    :type storage_domain_name: str
    :param subscription_id: The subscription id
    :type subscription_id: str
    :param resource_group_name: The resource group name
    :type resource_group_name: str
    :param manager_name: The manager name
    :type manager_name: str
    :param api_version: The api version
    :type api_version: str

    """
    return web.Response(status=200)


async def storage_domains_list_by_manager(request: web.Request, subscription_id, resource_group_name, manager_name, api_version) -> web.Response:
    """storage_domains_list_by_manager

    Retrieves all the storage domains in a manager.

    :param subscription_id: The subscription id
    :type subscription_id: str
    :param resource_group_name: The resource group name
    :type resource_group_name: str
    :param manager_name: The manager name
    :type manager_name: str
    :param api_version: The api version
    :type api_version: str

    """
    return web.Response(status=200)
