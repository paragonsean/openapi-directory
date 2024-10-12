# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.peering_service_prefix import PeeringServicePrefix
from openapi_server.models.peering_service_prefix_list_result import PeeringServicePrefixListResult


pytestmark = pytest.mark.asyncio

async def test_peering_service_prefixes_create_or_update(client):
    """Test case for peering_service_prefixes_create_or_update

    
    """
    peering_service_prefix = {"properties":{"learnedType":"None","prefix":"prefix","prefixValidationState":"None","provisioningState":"Succeeded"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Peering/peeringServices/{peering_service_name}/prefixes/{prefix_name}'.format(resource_group_name='resource_group_name_example', peering_service_name='peering_service_name_example', prefix_name='prefix_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=peering_service_prefix,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_peering_service_prefixes_delete(client):
    """Test case for peering_service_prefixes_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Peering/peeringServices/{peering_service_name}/prefixes/{prefix_name}'.format(resource_group_name='resource_group_name_example', peering_service_name='peering_service_name_example', prefix_name='prefix_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_peering_service_prefixes_get(client):
    """Test case for peering_service_prefixes_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Peering/peeringServices/{peering_service_name}/prefixes/{prefix_name}'.format(resource_group_name='resource_group_name_example', peering_service_name='peering_service_name_example', prefix_name='prefix_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_prefixes_list_by_peering_service(client):
    """Test case for prefixes_list_by_peering_service

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Peering/peeringServices/{peering_service_name}/prefixes'.format(resource_group_name='resource_group_name_example', peering_service_name='peering_service_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

