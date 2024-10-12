# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.local_network_gateway import LocalNetworkGateway
from openapi_server.models.local_network_gateway_list_result import LocalNetworkGatewayListResult
from openapi_server.models.virtual_network_gateway_connections_update_tags_request import VirtualNetworkGatewayConnectionsUpdateTagsRequest


pytestmark = pytest.mark.asyncio

async def test_local_network_gateways_create_or_update(client):
    """Test case for local_network_gateways_create_or_update

    
    """
    parameters = {"etag":"etag","properties":{"localNetworkAddressSpace":{"addressPrefixes":["addressPrefixes","addressPrefixes"]},"resourceGuid":"resourceGuid","gatewayIpAddress":"gatewayIpAddress","bgpSettings":{"bgpPeeringAddress":"bgpPeeringAddress","asn":5,"peerWeight":2},"provisioningState":"provisioningState"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/localNetworkGateways/{local_network_gateway_name}'.format(resource_group_name='resource_group_name_example', local_network_gateway_name='local_network_gateway_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_local_network_gateways_delete(client):
    """Test case for local_network_gateways_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/localNetworkGateways/{local_network_gateway_name}'.format(resource_group_name='resource_group_name_example', local_network_gateway_name='local_network_gateway_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_local_network_gateways_get(client):
    """Test case for local_network_gateways_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/localNetworkGateways/{local_network_gateway_name}'.format(resource_group_name='resource_group_name_example', local_network_gateway_name='local_network_gateway_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_local_network_gateways_list(client):
    """Test case for local_network_gateways_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/localNetworkGateways'.format(resource_group_name='resource_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_local_network_gateways_update_tags(client):
    """Test case for local_network_gateways_update_tags

    
    """
    parameters = openapi_server.VirtualNetworkGatewayConnectionsUpdateTagsRequest()
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/localNetworkGateways/{local_network_gateway_name}'.format(resource_group_name='resource_group_name_example', local_network_gateway_name='local_network_gateway_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

