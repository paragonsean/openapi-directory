# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.private_endpoint_connection import PrivateEndpointConnection
from openapi_server.models.private_endpoint_connection_list_result import PrivateEndpointConnectionListResult


pytestmark = pytest.mark.asyncio

async def test_private_endpoint_connections_create_or_update(client):
    """Test case for private_endpoint_connections_create_or_update

    
    """
    private_endpoint_connection = {"name":"name","id":"id","type":"type","properties":{"privateLinkServiceConnectionState":{"actionsRequired":"None","description":"description","status":"Pending"},"privateEndpoint":{"id":"id"},"provisioningState":"Creating"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.AppConfiguration/configurationStores/{config_store_name}/privateEndpointConnections/{private_endpoint_connection_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', config_store_name='config_store_name_example', private_endpoint_connection_name='private_endpoint_connection_name_example'),
        headers=headers,
        json=private_endpoint_connection,
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
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.AppConfiguration/configurationStores/{config_store_name}/privateEndpointConnections/{private_endpoint_connection_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', config_store_name='config_store_name_example', private_endpoint_connection_name='private_endpoint_connection_name_example'),
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
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.AppConfiguration/configurationStores/{config_store_name}/privateEndpointConnections/{private_endpoint_connection_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', config_store_name='config_store_name_example', private_endpoint_connection_name='private_endpoint_connection_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_endpoint_connections_list_by_configuration_store(client):
    """Test case for private_endpoint_connections_list_by_configuration_store

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.AppConfiguration/configurationStores/{config_store_name}/privateEndpointConnections'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', config_store_name='config_store_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

