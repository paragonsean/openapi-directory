# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.private_endpoint_connection import PrivateEndpointConnection
from openapi_server.models.private_endpoint_connection_list_result import PrivateEndpointConnectionListResult


pytestmark = pytest.mark.asyncio

async def test_private_endpoint_connections_create_or_update(client):
    """Test case for private_endpoint_connections_create_or_update

    
    """
    parameters = {"properties":{"privateLinkServiceConnectionState":{"actionsRequired":"actionsRequired","description":"description","status":"status"},"privateEndpoint":{"id":"id"}}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DocumentDB/databaseAccounts/{account_name}/privateEndpointConnections/{private_endpoint_connection_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', private_endpoint_connection_name='private_endpoint_connection_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


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
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DocumentDB/databaseAccounts/{account_name}/privateEndpointConnections/{private_endpoint_connection_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', private_endpoint_connection_name='private_endpoint_connection_name_example'),
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
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DocumentDB/databaseAccounts/{account_name}/privateEndpointConnections/{private_endpoint_connection_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', private_endpoint_connection_name='private_endpoint_connection_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_endpoint_connections_list_by_database_account(client):
    """Test case for private_endpoint_connections_list_by_database_account

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DocumentDB/databaseAccounts/{account_name}/privateEndpointConnections'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

