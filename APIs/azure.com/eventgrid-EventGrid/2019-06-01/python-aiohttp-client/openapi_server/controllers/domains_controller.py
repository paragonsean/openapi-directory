from typing import List, Dict
from aiohttp import web

from openapi_server.models.domain import Domain
from openapi_server.models.domain_regenerate_key_request import DomainRegenerateKeyRequest
from openapi_server.models.domain_shared_access_keys import DomainSharedAccessKeys
from openapi_server.models.domain_update_parameters import DomainUpdateParameters
from openapi_server.models.domains_list_result import DomainsListResult
from openapi_server import util


async def domains_create_or_update(request: web.Request, subscription_id, resource_group_name, domain_name, api_version, domain_info) -> web.Response:
    """Create or update a domain.

    Asynchronously creates or updates a new domain with the specified parameters.

    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the user&#39;s subscription.
    :type resource_group_name: str
    :param domain_name: Name of the domain.
    :type domain_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param domain_info: Domain information.
    :type domain_info: dict | bytes

    """
    domain_info = Domain.from_dict(domain_info)
    return web.Response(status=200)


async def domains_delete(request: web.Request, subscription_id, resource_group_name, domain_name, api_version) -> web.Response:
    """Delete a domain.

    Delete existing domain.

    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the user&#39;s subscription.
    :type resource_group_name: str
    :param domain_name: Name of the domain.
    :type domain_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def domains_get(request: web.Request, subscription_id, resource_group_name, domain_name, api_version) -> web.Response:
    """Get a domain.

    Get properties of a domain.

    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the user&#39;s subscription.
    :type resource_group_name: str
    :param domain_name: Name of the domain.
    :type domain_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def domains_list_by_resource_group(request: web.Request, subscription_id, resource_group_name, api_version, filter=None, top=None) -> web.Response:
    """List domains under a resource group.

    List all the domains under a resource group.

    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the user&#39;s subscription.
    :type resource_group_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param filter: The query used to filter the search results using OData syntax. Filtering is permitted on the &#39;name&#39; property only and with limited number of OData operations. These operations are: the &#39;contains&#39; function as well as the following logical operations: not, and, or, eq (for equal), and ne (for not equal). No arithmetic operations are supported. The following is a valid filter example: $filter&#x3D;contains(namE, &#39;PATTERN&#39;) and name ne &#39;PATTERN-1&#39;. The following is not a valid filter example: $filter&#x3D;location eq &#39;westus&#39;.
    :type filter: str
    :param top: The number of results to return per page for the list operation. Valid range for top parameter is 1 to 100. If not specified, the default number of results to be returned is 20 items per page.
    :type top: int

    """
    return web.Response(status=200)


async def domains_list_by_subscription(request: web.Request, subscription_id, api_version, filter=None, top=None) -> web.Response:
    """List domains under an Azure subscription.

    List all the domains under an Azure subscription.

    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param filter: The query used to filter the search results using OData syntax. Filtering is permitted on the &#39;name&#39; property only and with limited number of OData operations. These operations are: the &#39;contains&#39; function as well as the following logical operations: not, and, or, eq (for equal), and ne (for not equal). No arithmetic operations are supported. The following is a valid filter example: $filter&#x3D;contains(namE, &#39;PATTERN&#39;) and name ne &#39;PATTERN-1&#39;. The following is not a valid filter example: $filter&#x3D;location eq &#39;westus&#39;.
    :type filter: str
    :param top: The number of results to return per page for the list operation. Valid range for top parameter is 1 to 100. If not specified, the default number of results to be returned is 20 items per page.
    :type top: int

    """
    return web.Response(status=200)


async def domains_list_shared_access_keys(request: web.Request, subscription_id, resource_group_name, domain_name, api_version) -> web.Response:
    """List keys for a domain.

    List the two keys used to publish to a domain.

    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the user&#39;s subscription.
    :type resource_group_name: str
    :param domain_name: Name of the domain.
    :type domain_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def domains_regenerate_key(request: web.Request, subscription_id, resource_group_name, domain_name, api_version, regenerate_key_request) -> web.Response:
    """Regenerate key for a domain.

    Regenerate a shared access key for a domain.

    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the user&#39;s subscription.
    :type resource_group_name: str
    :param domain_name: Name of the domain.
    :type domain_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param regenerate_key_request: Request body to regenerate key.
    :type regenerate_key_request: dict | bytes

    """
    regenerate_key_request = DomainRegenerateKeyRequest.from_dict(regenerate_key_request)
    return web.Response(status=200)


async def domains_update(request: web.Request, subscription_id, resource_group_name, domain_name, api_version, domain_update_parameters) -> web.Response:
    """Update a domain.

    Asynchronously updates a domain with the specified parameters.

    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the user&#39;s subscription.
    :type resource_group_name: str
    :param domain_name: Name of the domain.
    :type domain_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param domain_update_parameters: Domain update information.
    :type domain_update_parameters: dict | bytes

    """
    domain_update_parameters = DomainUpdateParameters.from_dict(domain_update_parameters)
    return web.Response(status=200)
