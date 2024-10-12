# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.connector_list_result import ConnectorListResult
from openapi_server.models.connector_resource_format import ConnectorResourceFormat


pytestmark = pytest.mark.asyncio

async def test_connectors_create_or_update(client):
    """Test case for connectors_create_or_update

    
    """
    parameters = {"properties":{"isInternal":True,"connectorProperties":{"key":"{}"},"connectorType":"None","connectorId":0,"created":"2000-01-23T04:56:07.000+00:00","displayName":"displayName","tenantId":"tenantId","connectorName":"connectorName","description":"description","lastModified":"2000-01-23T04:56:07.000+00:00","state":"Creating"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.CustomerInsights/hubs/{hub_name}/connectors/{connector_name}'.format(resource_group_name='resource_group_name_example', hub_name='hub_name_example', connector_name='connector_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_connectors_delete(client):
    """Test case for connectors_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.CustomerInsights/hubs/{hub_name}/connectors/{connector_name}'.format(resource_group_name='resource_group_name_example', hub_name='hub_name_example', connector_name='connector_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_connectors_get(client):
    """Test case for connectors_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.CustomerInsights/hubs/{hub_name}/connectors/{connector_name}'.format(resource_group_name='resource_group_name_example', hub_name='hub_name_example', connector_name='connector_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_connectors_list_by_hub(client):
    """Test case for connectors_list_by_hub

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.CustomerInsights/hubs/{hub_name}/connectors'.format(resource_group_name='resource_group_name_example', hub_name='hub_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

