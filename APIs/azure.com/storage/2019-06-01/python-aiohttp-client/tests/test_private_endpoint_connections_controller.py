# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.private_endpoint_connection import PrivateEndpointConnection


pytestmark = pytest.mark.asyncio

async def test_private_endpoint_connections_delete(client):
    """Test case for private_endpoint_connections_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Storage/storageAccounts/{account_name}/privateEndpointConnections/{private_endpoint_connection_name}'.format(resource_group_name='resource_group_name_example', account_name='account_name_example', subscription_id='subscription_id_example', private_endpoint_connection_name='private_endpoint_connection_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_endpoint_connections_get(client):
    """Test case for private_endpoint_connections_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Storage/storageAccounts/{account_name}/privateEndpointConnections/{private_endpoint_connection_name}'.format(resource_group_name='resource_group_name_example', account_name='account_name_example', subscription_id='subscription_id_example', private_endpoint_connection_name='private_endpoint_connection_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_endpoint_connections_put(client):
    """Test case for private_endpoint_connections_put

    
    """
    properties = {"properties":{"privateLinkServiceConnectionState":{"actionRequired":"actionRequired","description":"description","status":"Pending"},"privateEndpoint":{"id":"id"},"provisioningState":"Succeeded"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Storage/storageAccounts/{account_name}/privateEndpointConnections/{private_endpoint_connection_name}'.format(resource_group_name='resource_group_name_example', account_name='account_name_example', subscription_id='subscription_id_example', private_endpoint_connection_name='private_endpoint_connection_name_example'),
        headers=headers,
        json=properties,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

