# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.domain_availablility_check_result import DomainAvailablilityCheckResult
from openapi_server.models.domain_collection import DomainCollection
from openapi_server.models.domain_control_center_sso_request import DomainControlCenterSsoRequest
from openapi_server.models.domain_recommendation_search_parameters import DomainRecommendationSearchParameters
from openapi_server.models.domain_registration_input import DomainRegistrationInput
from openapi_server.models.name_identifier import NameIdentifier
from openapi_server.models.name_identifier_collection import NameIdentifierCollection


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_global_domain_registration_check_domain_availability(client):
    """Test case for global_domain_registration_check_domain_availability

    Checks if a domain is available for registration
    """
    identifier = {"name":"name"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/providers/Microsoft.DomainRegistration/checkDomainAvailability'.format(subscription_id='subscription_id_example'),
        headers=headers,
        json=identifier,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_global_domain_registration_get_all_domains(client):
    """Test case for global_domain_registration_get_all_domains

    Lists all domains in a subscription
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.DomainRegistration/domains'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_global_domain_registration_get_domain_control_center_sso_request(client):
    """Test case for global_domain_registration_get_domain_control_center_sso_request

    Generates a single sign on request for domain management portal
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/providers/Microsoft.DomainRegistration/generateSsoRequest'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_global_domain_registration_list_domain_recommendations(client):
    """Test case for global_domain_registration_list_domain_recommendations

    Lists domain recommendations based on keywords
    """
    parameters = {"keywords":"keywords","maxDomainRecommendations":0}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/providers/Microsoft.DomainRegistration/listDomainRecommendations'.format(subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_global_domain_registration_validate_domain_purchase_information(client):
    """Test case for global_domain_registration_validate_domain_purchase_information

    Validates domain registration information
    """
    domain_registration_input = {"properties":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/providers/Microsoft.DomainRegistration/validateDomainRegistrationInformation'.format(subscription_id='subscription_id_example'),
        headers=headers,
        json=domain_registration_input,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

