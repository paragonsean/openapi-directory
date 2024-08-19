# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.suppression_contract import SuppressionContract


pytestmark = pytest.mark.asyncio

async def test_suppressions_create(client):
    """Test case for suppressions_create

    
    """
    suppression_contract = {"suppressionId":"suppressionId","ttl":"ttl"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/{resource_uri}/providers/Microsoft.Advisor/recommendations/{recommendation_id}/suppressions/{name}'.format(resource_uri='resource_uri_example', recommendation_id='recommendation_id_example', name='name_example'),
        headers=headers,
        json=suppression_contract,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_suppressions_delete(client):
    """Test case for suppressions_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/{resource_uri}/providers/Microsoft.Advisor/recommendations/{recommendation_id}/suppressions/{name}'.format(resource_uri='resource_uri_example', recommendation_id='recommendation_id_example', name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_suppressions_get(client):
    """Test case for suppressions_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{resource_uri}/providers/Microsoft.Advisor/recommendations/{recommendation_id}/suppressions/{name}'.format(resource_uri='resource_uri_example', recommendation_id='recommendation_id_example', name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_suppressions_list(client):
    """Test case for suppressions_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Advisor/suppressions'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

