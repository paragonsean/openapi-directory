# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.route import Route
from openapi_server.models.route_list_result import RouteListResult


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_routes_create_or_update(client):
    """Test case for routes_create_or_update

    
    """
    route_parameters = {"name":"name","etag":"etag","properties":{"addressPrefix":"addressPrefix","nextHopType":"VirtualNetworkGateway","nextHopIpAddress":"nextHopIpAddress","provisioningState":"provisioningState"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/routeTables/{route_table_name}/routes/{route_name}'.format(resource_group_name='resource_group_name_example', route_table_name='route_table_name_example', route_name='route_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=route_parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_routes_delete(client):
    """Test case for routes_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/routeTables/{route_table_name}/routes/{route_name}'.format(resource_group_name='resource_group_name_example', route_table_name='route_table_name_example', route_name='route_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_routes_get(client):
    """Test case for routes_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/routeTables/{route_table_name}/routes/{route_name}'.format(resource_group_name='resource_group_name_example', route_table_name='route_table_name_example', route_name='route_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_routes_list(client):
    """Test case for routes_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/routeTables/{route_table_name}/routes'.format(resource_group_name='resource_group_name_example', route_table_name='route_table_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

