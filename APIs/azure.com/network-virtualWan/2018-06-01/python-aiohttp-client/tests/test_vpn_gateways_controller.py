# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.virtual_hubs_list_default_response import VirtualHubsListDefaultResponse
from openapi_server.models.virtual_hubs_update_tags_request import VirtualHubsUpdateTagsRequest
from openapi_server.models.vpn_gateway import VpnGateway


pytestmark = pytest.mark.asyncio

async def test_vpn_gateways_update_tags(client):
    """Test case for vpn_gateways_update_tags

    
    """
    vpn_gateway_parameters = openapi_server.VirtualHubsUpdateTagsRequest()
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/vpnGateways/{gateway_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', gateway_name='gateway_name_example'),
        headers=headers,
        json=vpn_gateway_parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

