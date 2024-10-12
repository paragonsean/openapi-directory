# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.p2_s_vpn_gateway import P2SVpnGateway
from openapi_server.models.p2_s_vpn_profile_parameters import P2SVpnProfileParameters
from openapi_server.models.p2s_vpn_gateways_list_default_response import P2sVpnGatewaysListDefaultResponse
from openapi_server.models.p2s_vpn_gateways_update_tags_request import P2sVpnGatewaysUpdateTagsRequest
from openapi_server.models.vpn_profile_response import VpnProfileResponse


pytestmark = pytest.mark.asyncio

async def test_p2s_vpn_gateways_generate_vpn_profile(client):
    """Test case for p2s_vpn_gateways_generate_vpn_profile

    
    """
    parameters = {"authenticationMethod":"EAPTLS"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/p2svpnGateways/{gateway_name}/generatevpnprofile'.format(resource_group_name='resource_group_name_example', gateway_name='gateway_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_p2s_vpn_gateways_get_p2s_vpn_connection_health(client):
    """Test case for p2s_vpn_gateways_get_p2s_vpn_connection_health

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/p2svpnGateways/{gateway_name}/getP2sVpnConnectionHealth'.format(resource_group_name='resource_group_name_example', gateway_name='gateway_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_p2s_vpn_gateways_update_tags(client):
    """Test case for p2s_vpn_gateways_update_tags

    
    """
    p2_s_vpn_gateway_parameters = openapi_server.P2sVpnGatewaysUpdateTagsRequest()
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/p2svpnGateways/{gateway_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', gateway_name='gateway_name_example'),
        headers=headers,
        json=p2_s_vpn_gateway_parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

