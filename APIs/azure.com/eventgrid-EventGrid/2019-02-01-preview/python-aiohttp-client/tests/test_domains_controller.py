# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.domain import Domain
from openapi_server.models.domain_regenerate_key_request import DomainRegenerateKeyRequest
from openapi_server.models.domain_shared_access_keys import DomainSharedAccessKeys
from openapi_server.models.domain_update_parameters import DomainUpdateParameters
from openapi_server.models.domains_list_result import DomainsListResult


pytestmark = pytest.mark.asyncio

async def test_domains_create_or_update(client):
    """Test case for domains_create_or_update

    Create or update a domain
    """
    domain_info = {"properties":{"endpoint":"endpoint","inputSchema":"EventGridSchema","inputSchemaMapping":{"inputSchemaMappingType":"Json"},"provisioningState":"Creating"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.EventGrid/domains/{domain_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', domain_name='domain_name_example'),
        headers=headers,
        json=domain_info,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_domains_delete(client):
    """Test case for domains_delete

    Delete a domain
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.EventGrid/domains/{domain_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', domain_name='domain_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_domains_get(client):
    """Test case for domains_get

    Get a domain
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.EventGrid/domains/{domain_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', domain_name='domain_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_domains_list_by_resource_group(client):
    """Test case for domains_list_by_resource_group

    List domains under a resource group
    """
    params = [('api-version', 'api_version_example'),
                    ('$filter', 'filter_example'),
                    ('$top', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.EventGrid/domains'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_domains_list_by_subscription(client):
    """Test case for domains_list_by_subscription

    List domains under an Azure subscription
    """
    params = [('api-version', 'api_version_example'),
                    ('$filter', 'filter_example'),
                    ('$top', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.EventGrid/domains'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_domains_list_shared_access_keys(client):
    """Test case for domains_list_shared_access_keys

    List keys for a domain
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.EventGrid/domains/{domain_name}/listKeys'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', domain_name='domain_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_domains_regenerate_key(client):
    """Test case for domains_regenerate_key

    Regenerate key for a domain
    """
    regenerate_key_request = {"keyName":"keyName"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.EventGrid/domains/{domain_name}/regenerateKey'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', domain_name='domain_name_example'),
        headers=headers,
        json=regenerate_key_request,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_domains_update(client):
    """Test case for domains_update

    Update a domain
    """
    domain_update_parameters = {"tags":{"key":"tags"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.EventGrid/domains/{domain_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', domain_name='domain_name_example'),
        headers=headers,
        json=domain_update_parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

