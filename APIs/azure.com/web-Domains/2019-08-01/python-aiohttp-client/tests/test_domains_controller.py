# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.domain import Domain
from openapi_server.models.domain_availability_check_result import DomainAvailabilityCheckResult
from openapi_server.models.domain_collection import DomainCollection
from openapi_server.models.domain_control_center_sso_request import DomainControlCenterSsoRequest
from openapi_server.models.domain_ownership_identifier import DomainOwnershipIdentifier
from openapi_server.models.domain_ownership_identifier_collection import DomainOwnershipIdentifierCollection
from openapi_server.models.domain_patch_resource import DomainPatchResource
from openapi_server.models.domain_recommendation_search_parameters import DomainRecommendationSearchParameters
from openapi_server.models.domains_check_availability_default_response import DomainsCheckAvailabilityDefaultResponse
from openapi_server.models.domains_check_availability_request import DomainsCheckAvailabilityRequest
from openapi_server.models.name_identifier_collection import NameIdentifierCollection


pytestmark = pytest.mark.asyncio

async def test_domains_check_availability(client):
    """Test case for domains_check_availability

    Check if a domain is available for registration.
    """
    identifier = openapi_server.DomainsCheckAvailabilityRequest()
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

async def test_domains_create_or_update(client):
    """Test case for domains_create_or_update

    Creates or updates a domain.
    """
    domain = {"properties":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DomainRegistration/domains/{domain_name}'.format(resource_group_name='resource_group_name_example', domain_name='domain_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=domain,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_domains_create_or_update_ownership_identifier(client):
    """Test case for domains_create_or_update_ownership_identifier

    Creates an ownership identifier for a domain or updates identifier details for an existing identifer
    """
    domain_ownership_identifier = {"properties":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DomainRegistration/domains/{domain_name}/domainOwnershipIdentifiers/{name}'.format(resource_group_name='resource_group_name_example', domain_name='domain_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=domain_ownership_identifier,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_domains_delete(client):
    """Test case for domains_delete

    Delete a domain.
    """
    params = [('forceHardDeleteDomain', True),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DomainRegistration/domains/{domain_name}'.format(resource_group_name='resource_group_name_example', domain_name='domain_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_domains_delete_ownership_identifier(client):
    """Test case for domains_delete_ownership_identifier

    Delete ownership identifier for domain
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DomainRegistration/domains/{domain_name}/domainOwnershipIdentifiers/{name}'.format(resource_group_name='resource_group_name_example', domain_name='domain_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_domains_get(client):
    """Test case for domains_get

    Get a domain.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DomainRegistration/domains/{domain_name}'.format(resource_group_name='resource_group_name_example', domain_name='domain_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_domains_get_control_center_sso_request(client):
    """Test case for domains_get_control_center_sso_request

    Generate a single sign-on request for the domain management portal.
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

async def test_domains_get_ownership_identifier(client):
    """Test case for domains_get_ownership_identifier

    Get ownership identifier for domain
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DomainRegistration/domains/{domain_name}/domainOwnershipIdentifiers/{name}'.format(resource_group_name='resource_group_name_example', domain_name='domain_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_domains_list(client):
    """Test case for domains_list

    Get all domains in a subscription.
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

async def test_domains_list_by_resource_group(client):
    """Test case for domains_list_by_resource_group

    Get all domains in a resource group.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DomainRegistration/domains'.format(resource_group_name='resource_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_domains_list_ownership_identifiers(client):
    """Test case for domains_list_ownership_identifiers

    Lists domain ownership identifiers.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DomainRegistration/domains/{domain_name}/domainOwnershipIdentifiers'.format(resource_group_name='resource_group_name_example', domain_name='domain_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_domains_list_recommendations(client):
    """Test case for domains_list_recommendations

    Get domain name recommendations based on keywords.
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

async def test_domains_renew(client):
    """Test case for domains_renew

    Renew a domain.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DomainRegistration/domains/{domain_name}/renew'.format(resource_group_name='resource_group_name_example', domain_name='domain_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_domains_update(client):
    """Test case for domains_update

    Creates or updates a domain.
    """
    domain = {"properties":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DomainRegistration/domains/{domain_name}'.format(resource_group_name='resource_group_name_example', domain_name='domain_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=domain,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_domains_update_ownership_identifier(client):
    """Test case for domains_update_ownership_identifier

    Creates an ownership identifier for a domain or updates identifier details for an existing identifer
    """
    domain_ownership_identifier = {"properties":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DomainRegistration/domains/{domain_name}/domainOwnershipIdentifiers/{name}'.format(resource_group_name='resource_group_name_example', domain_name='domain_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=domain_ownership_identifier,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

