from typing import List, Dict
from aiohttp import web

from openapi_server.models.domain_service import DomainService
from openapi_server.models.domain_service_list_result import DomainServiceListResult
from openapi_server.models.operation_entity_list_result import OperationEntityListResult
from openapi_server import util


async def domain_service_operations_list(request: web.Request, api_version) -> web.Response:
    """domain_service_operations_list

    Lists all the available Domain Services operations.

    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def domain_services_create_or_update(request: web.Request, api_version, subscription_id, resource_group_name, domain_service_name, domain_service) -> web.Response:
    """Create or Update Domain Service (PUT Resource)

    The Create Domain Service operation creates a new domain service with the specified parameters. If the specific service already exists, then any patchable properties will be updated and any immutable properties will remain unchanged.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the user&#39;s subscription. The name is case insensitive.
    :type resource_group_name: str
    :param domain_service_name: The name of the domain service.
    :type domain_service_name: str
    :param domain_service: Properties supplied to the Create or Update a Domain Service operation.
    :type domain_service: dict | bytes

    """
    domain_service = DomainService.from_dict(domain_service)
    return web.Response(status=200)


async def domain_services_delete(request: web.Request, api_version, subscription_id, resource_group_name, domain_service_name) -> web.Response:
    """Delete Domain Service (DELETE Resource)

    The Delete Domain Service operation deletes an existing Domain Service.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the user&#39;s subscription. The name is case insensitive.
    :type resource_group_name: str
    :param domain_service_name: The name of the domain service.
    :type domain_service_name: str

    """
    return web.Response(status=200)


async def domain_services_get(request: web.Request, api_version, subscription_id, resource_group_name, domain_service_name) -> web.Response:
    """Get Domain Service (GET Resources)

    The Get Domain Service operation retrieves a json representation of the Domain Service.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the user&#39;s subscription. The name is case insensitive.
    :type resource_group_name: str
    :param domain_service_name: The name of the domain service.
    :type domain_service_name: str

    """
    return web.Response(status=200)


async def domain_services_list(request: web.Request, api_version, subscription_id) -> web.Response:
    """List Domain Services in Subscription (GET Resources)

    The List Domain Services in Subscription operation lists all the domain services available under the given subscription (and across all resource groups within that subscription).

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def domain_services_list_by_resource_group(request: web.Request, api_version, subscription_id, resource_group_name) -> web.Response:
    """List Domain Services in Resource Group (GET Resources)

    The List Domain Services in Resource Group operation lists all the domain services available under the given resource group.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the user&#39;s subscription. The name is case insensitive.
    :type resource_group_name: str

    """
    return web.Response(status=200)


async def domain_services_update(request: web.Request, api_version, subscription_id, resource_group_name, domain_service_name, domain_service) -> web.Response:
    """Update Domain Service (PATCH Resource)

    The Update Domain Service operation can be used to update the existing deployment. The update call only supports the properties listed in the PATCH body.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the user&#39;s subscription. The name is case insensitive.
    :type resource_group_name: str
    :param domain_service_name: The name of the domain service.
    :type domain_service_name: str
    :param domain_service: Properties supplied to the Update a Domain Service operation.
    :type domain_service: dict | bytes

    """
    domain_service = DomainService.from_dict(domain_service)
    return web.Response(status=200)
