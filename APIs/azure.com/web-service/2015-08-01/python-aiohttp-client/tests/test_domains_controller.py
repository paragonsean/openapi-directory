# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.domain import Domain
from openapi_server.models.domain_collection import DomainCollection


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_domains_create_or_update_domain(client):
    """Test case for domains_create_or_update_domain

    Creates a domain
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

async def test_domains_delete_domain(client):
    """Test case for domains_delete_domain

    Deletes a domain
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

async def test_domains_get_domain(client):
    """Test case for domains_get_domain

    Gets details of a domain
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

async def test_domains_get_domain_operation(client):
    """Test case for domains_get_domain_operation

    Retrieves the latest status of a domain purchase operation
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DomainRegistration/domains/{domain_name}/operationresults/{operation_id}'.format(resource_group_name='resource_group_name_example', domain_name='domain_name_example', operation_id='operation_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_domains_get_domains(client):
    """Test case for domains_get_domains

    Lists domains under a resource group
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

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_domains_update_domain(client):
    """Test case for domains_update_domain

    Creates a domain
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

