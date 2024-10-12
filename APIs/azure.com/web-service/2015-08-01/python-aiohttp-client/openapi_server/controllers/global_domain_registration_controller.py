from typing import List, Dict
from aiohttp import web

from openapi_server.models.domain_availablility_check_result import DomainAvailablilityCheckResult
from openapi_server.models.domain_collection import DomainCollection
from openapi_server.models.domain_control_center_sso_request import DomainControlCenterSsoRequest
from openapi_server.models.domain_recommendation_search_parameters import DomainRecommendationSearchParameters
from openapi_server.models.domain_registration_input import DomainRegistrationInput
from openapi_server.models.name_identifier import NameIdentifier
from openapi_server.models.name_identifier_collection import NameIdentifierCollection
from openapi_server import util


async def global_domain_registration_check_domain_availability(request: web.Request, subscription_id, api_version, identifier) -> web.Response:
    """Checks if a domain is available for registration

    

    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param identifier: Name of the domain
    :type identifier: dict | bytes

    """
    identifier = NameIdentifier.from_dict(identifier)
    return web.Response(status=200)


async def global_domain_registration_get_all_domains(request: web.Request, subscription_id, api_version) -> web.Response:
    """Lists all domains in a subscription

    

    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def global_domain_registration_get_domain_control_center_sso_request(request: web.Request, subscription_id, api_version) -> web.Response:
    """Generates a single sign on request for domain management portal

    

    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def global_domain_registration_list_domain_recommendations(request: web.Request, subscription_id, api_version, parameters) -> web.Response:
    """Lists domain recommendations based on keywords

    

    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param parameters: Domain recommendation search parameters
    :type parameters: dict | bytes

    """
    parameters = DomainRecommendationSearchParameters.from_dict(parameters)
    return web.Response(status=200)


async def global_domain_registration_validate_domain_purchase_information(request: web.Request, subscription_id, api_version, domain_registration_input) -> web.Response:
    """Validates domain registration information

    

    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param domain_registration_input: Domain registration information
    :type domain_registration_input: dict | bytes

    """
    domain_registration_input = DomainRegistrationInput.from_dict(domain_registration_input)
    return web.Response(status=200)
