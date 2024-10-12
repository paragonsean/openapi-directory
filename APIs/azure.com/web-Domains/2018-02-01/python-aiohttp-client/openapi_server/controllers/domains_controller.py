from typing import List, Dict
from aiohttp import web

from openapi_server.models.domain import Domain
from openapi_server.models.domain_availablility_check_result import DomainAvailablilityCheckResult
from openapi_server.models.domain_collection import DomainCollection
from openapi_server.models.domain_control_center_sso_request import DomainControlCenterSsoRequest
from openapi_server.models.domain_ownership_identifier import DomainOwnershipIdentifier
from openapi_server.models.domain_ownership_identifier_collection import DomainOwnershipIdentifierCollection
from openapi_server.models.domain_patch_resource import DomainPatchResource
from openapi_server.models.domain_recommendation_search_parameters import DomainRecommendationSearchParameters
from openapi_server.models.domains_check_availability_default_response import DomainsCheckAvailabilityDefaultResponse
from openapi_server.models.domains_check_availability_request import DomainsCheckAvailabilityRequest
from openapi_server.models.name_identifier_collection import NameIdentifierCollection
from openapi_server import util


async def domains_check_availability(request: web.Request, subscription_id, api_version, identifier) -> web.Response:
    """Check if a domain is available for registration.

    Check if a domain is available for registration.

    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param identifier: Name of the domain.
    :type identifier: dict | bytes

    """
    identifier = DomainsCheckAvailabilityRequest.from_dict(identifier)
    return web.Response(status=200)


async def domains_create_or_update(request: web.Request, resource_group_name, domain_name, subscription_id, api_version, domain) -> web.Response:
    """Creates or updates a domain.

    Creates or updates a domain.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param domain_name: Name of the domain.
    :type domain_name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param domain: Domain registration information.
    :type domain: dict | bytes

    """
    domain = Domain.from_dict(domain)
    return web.Response(status=200)


async def domains_create_or_update_ownership_identifier(request: web.Request, resource_group_name, domain_name, name, subscription_id, api_version, domain_ownership_identifier) -> web.Response:
    """Creates an ownership identifier for a domain or updates identifier details for an existing identifer

    Creates an ownership identifier for a domain or updates identifier details for an existing identifer

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param domain_name: Name of domain.
    :type domain_name: str
    :param name: Name of identifier.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param domain_ownership_identifier: A JSON representation of the domain ownership properties.
    :type domain_ownership_identifier: dict | bytes

    """
    domain_ownership_identifier = DomainOwnershipIdentifier.from_dict(domain_ownership_identifier)
    return web.Response(status=200)


async def domains_delete(request: web.Request, resource_group_name, domain_name, subscription_id, api_version, force_hard_delete_domain=None) -> web.Response:
    """Delete a domain.

    Delete a domain.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param domain_name: Name of the domain.
    :type domain_name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param force_hard_delete_domain: Specify &lt;code&gt;true&lt;/code&gt; to delete the domain immediately. The default is &lt;code&gt;false&lt;/code&gt; which deletes the domain after 24 hours.
    :type force_hard_delete_domain: bool

    """
    return web.Response(status=200)


async def domains_delete_ownership_identifier(request: web.Request, resource_group_name, domain_name, name, subscription_id, api_version) -> web.Response:
    """Delete ownership identifier for domain

    Delete ownership identifier for domain

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param domain_name: Name of domain.
    :type domain_name: str
    :param name: Name of identifier.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def domains_get(request: web.Request, resource_group_name, domain_name, subscription_id, api_version) -> web.Response:
    """Get a domain.

    Get a domain.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param domain_name: Name of the domain.
    :type domain_name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def domains_get_control_center_sso_request(request: web.Request, subscription_id, api_version) -> web.Response:
    """Generate a single sign-on request for the domain management portal.

    Generate a single sign-on request for the domain management portal.

    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def domains_get_ownership_identifier(request: web.Request, resource_group_name, domain_name, name, subscription_id, api_version) -> web.Response:
    """Get ownership identifier for domain

    Get ownership identifier for domain

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param domain_name: Name of domain.
    :type domain_name: str
    :param name: Name of identifier.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def domains_list(request: web.Request, subscription_id, api_version) -> web.Response:
    """Get all domains in a subscription.

    Get all domains in a subscription.

    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def domains_list_by_resource_group(request: web.Request, resource_group_name, subscription_id, api_version) -> web.Response:
    """Get all domains in a resource group.

    Get all domains in a resource group.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def domains_list_ownership_identifiers(request: web.Request, resource_group_name, domain_name, subscription_id, api_version) -> web.Response:
    """Lists domain ownership identifiers.

    Lists domain ownership identifiers.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param domain_name: Name of domain.
    :type domain_name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def domains_list_recommendations(request: web.Request, subscription_id, api_version, parameters) -> web.Response:
    """Get domain name recommendations based on keywords.

    Get domain name recommendations based on keywords.

    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param parameters: Search parameters for domain name recommendations.
    :type parameters: dict | bytes

    """
    parameters = DomainRecommendationSearchParameters.from_dict(parameters)
    return web.Response(status=200)


async def domains_renew(request: web.Request, resource_group_name, domain_name, subscription_id, api_version) -> web.Response:
    """Renew a domain.

    Renew a domain.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param domain_name: Name of the domain.
    :type domain_name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def domains_update(request: web.Request, resource_group_name, domain_name, subscription_id, api_version, domain) -> web.Response:
    """Creates or updates a domain.

    Creates or updates a domain.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param domain_name: Name of the domain.
    :type domain_name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param domain: Domain registration information.
    :type domain: dict | bytes

    """
    domain = DomainPatchResource.from_dict(domain)
    return web.Response(status=200)


async def domains_update_ownership_identifier(request: web.Request, resource_group_name, domain_name, name, subscription_id, api_version, domain_ownership_identifier) -> web.Response:
    """Creates an ownership identifier for a domain or updates identifier details for an existing identifer

    Creates an ownership identifier for a domain or updates identifier details for an existing identifer

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param domain_name: Name of domain.
    :type domain_name: str
    :param name: Name of identifier.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param domain_ownership_identifier: A JSON representation of the domain ownership properties.
    :type domain_ownership_identifier: dict | bytes

    """
    domain_ownership_identifier = DomainOwnershipIdentifier.from_dict(domain_ownership_identifier)
    return web.Response(status=200)
