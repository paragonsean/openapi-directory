from typing import List, Dict
from aiohttp import web

from openapi_server.models.domain import Domain
from openapi_server.models.domain_collection import DomainCollection
from openapi_server import util


async def domains_create_or_update_domain(request: web.Request, resource_group_name, domain_name, subscription_id, api_version, domain) -> web.Response:
    """Creates a domain

    

    :param resource_group_name: &amp;gt;Name of the resource group
    :type resource_group_name: str
    :param domain_name: Name of the domain
    :type domain_name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param domain: Domain registration information
    :type domain: dict | bytes

    """
    domain = Domain.from_dict(domain)
    return web.Response(status=200)


async def domains_delete_domain(request: web.Request, resource_group_name, domain_name, subscription_id, api_version, force_hard_delete_domain=None) -> web.Response:
    """Deletes a domain

    

    :param resource_group_name: Name of the resource group
    :type resource_group_name: str
    :param domain_name: Name of the domain
    :type domain_name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param force_hard_delete_domain: If true then the domain will be deleted immediately instead of after 24 hours
    :type force_hard_delete_domain: bool

    """
    return web.Response(status=200)


async def domains_get_domain(request: web.Request, resource_group_name, domain_name, subscription_id, api_version) -> web.Response:
    """Gets details of a domain

    

    :param resource_group_name: Name of the resource group
    :type resource_group_name: str
    :param domain_name: Name of the domain
    :type domain_name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def domains_get_domain_operation(request: web.Request, resource_group_name, domain_name, operation_id, subscription_id, api_version) -> web.Response:
    """Retrieves the latest status of a domain purchase operation

    

    :param resource_group_name: Name of the resource group
    :type resource_group_name: str
    :param domain_name: Name of the domain
    :type domain_name: str
    :param operation_id: Domain purchase operation Id
    :type operation_id: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def domains_get_domains(request: web.Request, resource_group_name, subscription_id, api_version) -> web.Response:
    """Lists domains under a resource group

    

    :param resource_group_name: Name of the resource group
    :type resource_group_name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def domains_update_domain(request: web.Request, resource_group_name, domain_name, subscription_id, api_version, domain) -> web.Response:
    """Creates a domain

    

    :param resource_group_name: &amp;gt;Name of the resource group
    :type resource_group_name: str
    :param domain_name: Name of the domain
    :type domain_name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param domain: Domain registration information
    :type domain: dict | bytes

    """
    domain = Domain.from_dict(domain)
    return web.Response(status=200)
