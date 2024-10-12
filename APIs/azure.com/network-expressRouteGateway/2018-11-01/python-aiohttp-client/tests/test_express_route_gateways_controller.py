# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.express_route_gateway import ExpressRouteGateway
from openapi_server.models.express_route_gateway_list import ExpressRouteGatewayList


pytestmark = pytest.mark.asyncio

async def test_express_route_gateways_create_or_update(client):
    """Test case for express_route_gateways_create_or_update

    
    """
    put_express_route_gateway_parameters = {"etag":"etag","properties":{"autoScaleConfiguration":{"bounds":{"min":6,"max":0}},"provisioningState":"Succeeded","expressRouteConnections":[{"name":"name","properties":{"authorizationKey":"authorizationKey","expressRouteCircuitPeering":{"id":"id"},"routingWeight":1,"provisioningState":"Succeeded"}},{"name":"name","properties":{"authorizationKey":"authorizationKey","expressRouteCircuitPeering":{"id":"id"},"routingWeight":1,"provisioningState":"Succeeded"}}],"virtualHub":{"id":"id"}}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/expressRouteGateways/{express_route_gateway_name}'.format(resource_group_name='resource_group_name_example', express_route_gateway_name='express_route_gateway_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=put_express_route_gateway_parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_express_route_gateways_delete(client):
    """Test case for express_route_gateways_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/expressRouteGateways/{express_route_gateway_name}'.format(resource_group_name='resource_group_name_example', express_route_gateway_name='express_route_gateway_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_express_route_gateways_get(client):
    """Test case for express_route_gateways_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/expressRouteGateways/{express_route_gateway_name}'.format(resource_group_name='resource_group_name_example', express_route_gateway_name='express_route_gateway_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_express_route_gateways_list_by_resource_group(client):
    """Test case for express_route_gateways_list_by_resource_group

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/expressRouteGateways'.format(resource_group_name='resource_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_express_route_gateways_list_by_subscription(client):
    """Test case for express_route_gateways_list_by_subscription

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Network/expressRouteGateways'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

