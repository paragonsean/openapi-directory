# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.csrp_error import CSRPError
from openapi_server.models.virtual_network import VirtualNetwork
from openapi_server.models.virtual_network_list_response import VirtualNetworkListResponse


pytestmark = pytest.mark.asyncio

async def test_virtual_networks_get(client):
    """Test case for virtual_networks_get

    Implements virtual network GET method
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.VMwareCloudSimple/locations/{region_id}/privateClouds/{pc_name}/virtualNetworks/{virtual_network_name}'.format(subscription_id='subscription_id_example', region_id='region_id_example', pc_name='pc_name_example', virtual_network_name='virtual_network_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_networks_list(client):
    """Test case for virtual_networks_list

    Implements list available virtual networks within a subscription method
    """
    params = [('api-version', 'api_version_example'),
                    ('resourcePoolName', 'resource_pool_name_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.VMwareCloudSimple/locations/{region_id}/privateClouds/{pc_name}/virtualNetworks'.format(subscription_id='subscription_id_example', region_id='region_id_example', pc_name='pc_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

